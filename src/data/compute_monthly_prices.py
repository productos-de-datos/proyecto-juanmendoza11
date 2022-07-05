def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    #raise NotImplementedError("Implementar esta función")
    import pandas as pd
    
    #Se usa pd para leer el archivo limpio, luego se computa la media del precio mensual. Se transfiere el archivo a la capa business. 
    df = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    df['fecha'] = pd.to_datetime(df['fecha'])
    df = df.set_index('fecha').resample("M")['precio'].mean()
    df.to_csv('data_lake/business/precios-mensuales.csv', index=True)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    compute_monthly_prices()
