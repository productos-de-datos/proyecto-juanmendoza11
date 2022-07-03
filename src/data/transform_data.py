def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.
"""

    import pandas as pd

    for j in range(1995, 2022):
        if j in range(1995,2000):
            df= pd.read_excel('data_lake/landing/{}.xlsx'.format(j), header=3)
            df.to_csv('data_lake/raw/{}.csv'.format(j), index=None)
        if j in range(2000, 2016):
            df = pd.read_excel('data_lake/landing/{}.xlsx'.format(j), header=2)
            df.to_csv('data_lake/raw/{}.csv'.format(j), index=None)
        if j in [2016, 2017]:
            df = pd.read_excel('data_lake/landing/{}.xls'.format(j), header=2)
            df.to_csv('data_lake/raw/{}.csv'.format(j), index=None)
        if j in range(2018, 2022):
            df = pd.read_excel('data_lake/landing/{}.xlsx'.format(j), header=0)
            df.to_csv('data_lake/raw/{}.csv'.format(j), index=None)
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()
