import pandas as pd


# Ordenar 

def ordenar_csv(file_path, output_path):

    df = pd.read_csv(file_path)
    df = df.map(lambda x: x.lower() if isinstance(x, str) else x)

    df_ordenado = df.sort_values(by='id_mascota')
    
    # Guardar en nuevo archivo CSV
    df_ordenado.to_csv(output_path, index=False)

# ordenar_csv('./data/raw/mascotas.csv', './data/processed/datos_ordenados.csv')
    

def duplicados_csv(file_path, output_path):

    df = pd.read_csv(file_path)

    # Eliminar filas duplicadas basándose en la columna id_mascota
    df_sin_duplicados = df.drop_duplicates(subset='id_mascota')
    
    # Guardar el DataFrame sin duplicados en un nuevo archivo CSV
    df_sin_duplicados.to_csv(output_path, index=False)
    
# duplicados_csv('./data/processed/datos_ordenados.csv', './data/processed/datos_sin_duplicados.csv')