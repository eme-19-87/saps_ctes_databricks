BASE_PATH="/Volumes/saps_ctes/bronze/source_system"

INGESTION_CONFIG=[
	{

		"source": "datosabiertos_ctes",
		"path":f"{BASE_PATH}/consultas_por_patologia.csv",
		"delimiter":",",
		"table": "datosctes_consultas_patologia"
	},
	{

		"source": "datosabiertos_ctes",
		"path":f"{BASE_PATH}/listado_saps.csv",
    "delimiter":",",
		"table": "datosctes_saps"
	},
	{

		"source": "datosabiertos_ctes",
		"path":f"{BASE_PATH}/inmunizaciones.csv",
    "delimiter":",",
		"table": "datosctes_inmunizaciones"
	},
    {

		"source": "datosabiertos_ctes",
		"path":f"{BASE_PATH}/tabla-salud-id_cie10.csv",
    "delimiter":",",
		"table": "datosctes_cie10"
	}


]