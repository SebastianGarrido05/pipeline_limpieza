import pandas as pd
from conexion import conectar

def cargar_csv(ruta_csv):

    conn = conectar()
    cursor = conn.cursor()

    df = pd.read_csv(ruta_csv)

    for _, fila in df.iterrows():

        cursor.execute("""
        INSERT INTO mascotas(
            id_mascota,
            nombre,
            especie,
            raza,
            edad_anos,
            peso_kg,
            fecha_consulta,
            dueno_nombre,
            dueno_email,
            motivo_consulta,
            costo_consulta,
            rango_peso,
            especie_no_info,
            especie_gato,
            especie_loro,
            especie_perro,
            especie_pez,
            anos_cliente
        )
        VALUES (
            %s,%s,%s,%s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,%s,%s,%s,%s
        )
        """,
        (
            fila["id_mascota"],
            fila["nombre"],
            fila["especie"],
            fila["raza"],
            fila["edad_anos"],
            fila["peso_kg"],
            None,
            fila["dueno_nombre"],
            fila["dueno_email"],
            fila["motivo_consulta"],
            fila["costo_consulta"],
            fila["rango_peso"],
            bool(fila["especie_No_Info"]),
            bool(fila["especie_gato"]),
            bool(fila["especie_loro"]),
            bool(fila["especie_perro"]),
            bool(fila["especie_pez"]),
            None
        ))

    conn.commit()

    cursor.close()
    conn.close()

    print("Datos cargados correctamente")