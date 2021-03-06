def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    import glob
    import pandas as pd
    
    #Se crea una variable con todos los archivos csv.
    ruta = glob.glob(r'data_lake/raw/*.csv')

    #se crea un bucle para tomar los archivos csv y transporner las horas (24) para unificar bajo las tres columnas [fecha, hora y precio]
    for i, archivo in enumerate(ruta):
        if i == 0:
            inicial = pd.read_csv(archivo, index_col=None, header=0)
            hours = inicial.iloc[:, :25]
            hours.columns = ['fecha']+[('0'+str(i))[-2:] for i in range(24)]
            inicial_transform = hours.melt(id_vars='fecha', var_name='hora', value_name='precio')
            final = inicial_transform
        else:
            inicial = pd.read_csv(archivo, index_col=None, header=0)
            hours = inicial.iloc[:, :25]
            hours.columns = ['fecha']+[('0'+str(i))[-2:] for i in range(24)]
            inicial_transform = hours.melt(id_vars='fecha', var_name='hora', value_name='precio')
            final = pd.concat([final, inicial_transform])
    final.to_csv('data_lake/cleansed/precios-horarios.csv', index=None)

    
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    clean_data()
