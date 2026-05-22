# pipeline_limpieza
# ESTE README.md SE REALIZÓ CON IA POR FALTA DE TIEMPO

## Descripción

Este proyecto implementa un pipeline de limpieza y transformación de datos utilizando Python y Pandas.

El objetivo es procesar un dataset de mascotas veterinarias, corrigiendo inconsistencias, eliminando duplicados y generando nuevas variables útiles para análisis posteriores.

---

# Estructura del Proyecto

```bash
pipeline_limpieza/
│
├── data/
│   ├── raw/
│   │   └── mascotas.csv
│   │
│   └── processed/
│       └── mascotas_final.csv
│
├── funciones.py
├── main.py
└── README.md
```

---

# Tecnologías Utilizadas

* Python 3
* Pandas
* Logging

---

# Procesos de Limpieza Realizados

## Normalización de texto

* Conversión de texto a minúsculas
* Eliminación de espacios innecesarios

---

## Eliminación de filas vacías

Se eliminan registros que contienen únicamente el ID de mascota y no poseen información relevante.

---

## Manejo de datos faltantes

Los valores nulos son reemplazados por:

```python
'No_Info'
```

---

## Estandarización de especies

Se normalizan nombres inconsistentes:

| Valor Original | Valor Final |
| -------------- | ----------- |
| cat            | gato        |
| gata           | gato        |
| dog            | perro       |
| perra          | perro       |

---

## Eliminación de duplicados

Se eliminan registros duplicados utilizando:

```python
dueño_email
```

como identificador único.

---

# Feature Engineering

## Rango de Peso

Se crea la columna:

```python
rango_peso
```

Clasificación:

| Peso       | Categoría |
| ---------- | --------- |
| < 4 kg     | bajo      |
| 4 - 15 kg  | normal    |
| 15 - 40 kg | alto      |
| > 40 kg    | obeso     |

---

## Codificación One-Hot

La columna:

```python
especie
```

es transformada usando:

```python
pd.get_dummies()
```

Generando columnas como:

* especie_gato
* especie_perro
* especie_pez

---

## Cálculo de años como cliente

Se calcula la antigüedad del cliente utilizando la fecha de su primera consulta registrada.

Nueva columna generada:

```python
años_cliente
```

---

# Logging

El pipeline incorpora logging para registrar:

* Lectura de archivos
* Limpieza de datos
* Transformaciones
* Exportación final

Ejemplo:

```text
2026-05-22 22:10:01 - INFO - Leyendo CSV...
2026-05-22 22:10:01 - INFO - Eliminando duplicados...
2026-05-22 22:10:01 - INFO - Exportando dataset limpio...
```

---

# Ejecución

## Ejecutar pipeline

```bash
python main.py
```

---

# Output

El dataset limpio se exporta automáticamente en:

```bash
data/processed/mascotas_final.csv
```

---

# Posibles Mejoras Futuras

* Validación automática de emails
* Detección de outliers extremos
* Dashboard de visualización
* Integración con base de datos
* Tests automatizados

---

# Autor

Sebastián Garrido y Dylan Cruz
