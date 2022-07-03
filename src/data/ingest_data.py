"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    #raise NotImplementedError("Implementar esta función")

    import requests
    ruta = "https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/"

    for ano in range(1995, 2022):
        if ano in [2016,2017]:
            url = ruta + "{}.xls?raw=true".format(ano)
            file = requests.get(url, allow_redirects=True)
            open('data_lake/landing/{}.xls'.format(ano),"wb").write(file.content)
        else:
            url = ruta + "{}.xlsx?raw=true".format(ano)
            file = requests.get(url, allow_redirects=True)
            open('data_lake/landing/{}.xls'.format(ano),"wb").write(file.content)



if __name__ == "__main__":
    import doctest

    doctest.testmod()
