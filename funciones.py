import pandas as pd
import logging
from datetime import datetime

# login
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def procesar_csv(file_path, output_path):

    logging.info("Leyendo CSV...")
    df = pd.read_csv(file_path)

    logging.info("Normalizando texto...")
    df = df.map(lambda x: x.lower().strip() if isinstance(x, str) else x)

    logging.info("Ordenando por id_mascota...")
    df = df.sort_values(by='id_mascota')

    logging.info("Eliminando filas completamente vacías...")
    df = df.dropna(
        subset=[
            'nombre','especie','raza','edad_anos',
            'peso_kg','fecha_consulta','dueno_nombre',
            'dueno_email','motivo_consulta','costo_consulta'
        ],
        how='all'
    )

    logging.info("Rellenando datos faltantes...")
    columnas_texto = [
    'nombre',
    'especie',
    'raza',
    'dueno_nombre',
    'dueno_email',
    'motivo_consulta']

    for col in columnas_texto:
        df[col] = df[col].fillna('No_Info')

    logging.info("Normalizando especies...")
    df['especie'] = df['especie'].replace({
        'cat': 'gato',
        'gata': 'gato',
        'dog': 'perro',
        'perra': 'perro'
    })

    logging.info("Eliminando duplicados...")
    df = df.drop_duplicates(subset='dueno_email')

    # RANGO PESO

    logging.info("Creando columna rango_peso...")

    def clasificar_peso(peso):

        try:
            peso = float(peso)

            if peso < 4:
                return 'bajo'

            elif peso < 15:
                return 'normal'

            elif peso < 40:
                return 'alto'

            else:
                return 'obeso'

        except:
            return 'No_Info'

    df['rango_peso'] = df['peso_kg'].apply(clasificar_peso)


    # GET DUMMIES

    logging.info("Codificando especie con get_dummies...")

    dummies = pd.get_dummies(df['especie'], prefix='especie')

    df = pd.concat([df, dummies], axis=1)


    # AÑOS CLIENTE

    logging.info("Calculando años_cliente...")

    df['fecha_consulta'] = pd.to_datetime(
        df['fecha_consulta'],
        format='%d-%m-%Y',
        errors='coerce'
    )

    primera_visita = df.groupby('dueno_email')['fecha_consulta'].transform('min')

    fecha_actual = pd.Timestamp.today()

    df['años_cliente'] = (
        (fecha_actual - primera_visita).dt.days / 365
    ).round(1)


    # FORMATO FECHA

    logging.info("Formateando fechas...")

    df['fecha_consulta'] = df['fecha_consulta'].dt.strftime('%d-%m-%Y')


    # EXPORTAR

    logging.info("Exportando dataset limpio...")

    df.to_csv(output_path, index=False)

    logging.info("Proceso terminado correctamente.")


# Ordenar 
def ordenar_csv(file_path, output_path):

    df = pd.read_csv(file_path)
    df = df.map(lambda x: x.lower() if isinstance(x, str) else x)

    df_ordenado = df.sort_values(by='id_mascota')

    # Borra la unica fila que no tiene nada mas que el id
    df_ordenado = df_ordenado.dropna(subset=['nombre','especie','raza','edad_anos','peso_kg','fecha_consulta','dueno_nombre','dueno_email','motivo_consulta','costo_consulta'], how='all')
    
    df_ordenado = df_ordenado.fillna('No_Info')

    df_ordenado['especie'] = df_ordenado['especie'].str.strip().replace({
        'cat': 'gato',
        'gata': 'gato',
        'dog': 'perro',
        'perra': 'perro'
    })
    
    # Guardar en nuevo archivo CSV
    df_ordenado.to_csv(output_path, index=False)



# ordenar_csv('./data/raw/mascotas.csv', './data/processed/datos_ordenados.csv')
    
def formato_csv(file_path, output_path):

    df = pd.read_csv(file_path)

    # Convertir la columna fecha_consulta a formato dd-mm-yyyy
    df['fecha_consulta'] = pd.to_datetime(df['fecha_consulta'], errors='coerce').dt.strftime('%d-%m-%Y')
    

    # Guardar el DataFrame con el formato corregido en un nuevo archivo CSV
    df.to_csv(output_path, index=False)

    # tabular cada dato y nombre columna en minuscula y sin espacios al principio ni al final
    df.columns = df.columns.str.strip().str.lower()
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].str.strip()


def duplicados_csv(file_path, output_path):

    df = pd.read_csv(file_path)

    # Eliminar filas duplicadas basándose en la columna dueño_email (se hace así ya que nadie puede tener el mismo email)
    df_sin_duplicados = df.drop_duplicates(subset='dueño_email')
    
    # Guardar el DataFrame sin duplicados en un nuevo archivo CSV
    df_sin_duplicados.to_csv(output_path, index=False)
    
# duplicados_csv('./data/processed/datos_ordenados.csv', './data/processed/datos_sin_duplicados.csv')


# ============================================================
# ============= CLASE 29/05/2026 // VALIDACIONES =============
# ============================================================


def val_Estructural (file_path):
    df = pd.read_csv(file_path)
    
    # razas_validadas = ["perro", "gato", "conejo", "pez", "loro"]
    
    sin_nulos = df["id_mascota"].notnull().all()
    
    es_int = pd.to_numeric(df["id_mascota"], errors="coerce").apply(
        lambda x: float(x).is_integer() if pd.notnull(x) else False).all()
    
    if sin_nulos and es_int:
        return logging.info("Validacion de peso no asegurada")
    else:
        print("La columna NO es válida")


def val_Semantica(file_path):

    df = pd.read_csv(file_path)

    df["peso_kg"] = pd.to_numeric(df["peso_kg"], errors="coerce")

    perros_incorrectos = df[
        (df["especie"] == "perro") &
        (df["rango_peso"] == "obeso") &
        (df["peso_kg"] <= 30)
    ]

    if perros_incorrectos.empty:
        logging.info("Validación de obesidad en perros correcta")
    else:
        logging.warning(
            f"Se encontraron {len(perros_incorrectos)} perros marcados como obesos con peso <= 30 kg"
        )

    gatos_incorrectos = df[
        (df["especie"] == "gato") &
        (df["rango_peso"] == "obeso") &
        (df["peso_kg"] <= 6)
    ]

    if gatos_incorrectos.empty:
        logging.info("Validación de obesidad en gatos correcta")
    else:
        logging.warning(
            f"Se encontraron {len(gatos_incorrectos)} gatos marcados como obesos con peso <= 6 kg"
        )