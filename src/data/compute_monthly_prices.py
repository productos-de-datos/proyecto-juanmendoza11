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
    
    df = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    df['fecha'] = pd.to_datetime(df['fecha'])
    df = df.set_index('fecha').resample("M")['precio'].mean()
    df.to_csv('data_lake/business/precios-mensuales.csv', index=True)

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    compute_monthly_prices()
    doctest.testmod()
