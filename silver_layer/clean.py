from pyspark.sql.functions import when, to_date, lit
import re

FECHA_NULA = lit("1900-01-01").cast("date")

def normalizar_fecha_spark(c):
    return (
        when(c.isNull(), FECHA_NULA)

        .when(
            c.rlike(r"^\d{2}-\d{2}$") |
            c.rlike(r"^\d{2}-\d{4}$") |
            c.rlike(r"^\d{4}-\d{2}$"),
            FECHA_NULA
        )

        .when(
            c.rlike(r"^\d{2}-\d{2}-\d{4}"),
            to_date(c, "dd-MM-yyyy")
        )

        .when(
            c.rlike(r"^\d{4}-\d{2}-\d{2}"),
            to_date(c, "yyyy-MM-dd")
        )

        .otherwise(FECHA_NULA)
    )


def normalizar_nombre_columna(nombre):
    nombre = nombre.strip().lower()
    nombre = re.sub(r"\s+", "_", nombre)      # múltiples espacios → _
    nombre = re.sub(r"[^a-z0-9_]", "", nombre) # elimina caracteres raros
    return nombre