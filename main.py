import funciones as func

# funciones Antiguas
# func.ordenar_csv('./data/raw/mascotas.csv', './data/processed/datos_ordenados.csv')

# func.formato_csv('./data/processed/datos_ordenados.csv', './data/processed/datos_ordenados.csv')

# func.duplicados_csv('./data/processed/datos_ordenados.csv', './data/processed/datos_sin_duplicados.csv')

# Funcion Vigente
func.procesar_csv('./data/raw/mascotas.csv','./data/processed/mascotas_final.csv')

func.val_Estructural('./data/processed/mascotas_final.csv')
func.val_Semantica('./data/processed/mascotas_final.csv')