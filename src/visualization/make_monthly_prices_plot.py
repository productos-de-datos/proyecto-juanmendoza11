def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios mensuales.

    Usando el archivo data_lake/business/precios-mensuales.csv, crea un grafico de
    lines que representa los precios promedios mensuales.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/monthly_prices.png.
    """
    #raise NotImplementedError("Implementar esta función")
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    df = pd.read_csv('data_lake/business/precios-mensuales.csv')
    monthly_prices_plot = df.plot(x='fecha', y = 'precio', kind = 'line').get_figure()
    monthly_prices_plot.savefig('data_lake/business/reports/figures/monthly_prices.png')

if __name__ == "__main__":
    import doctest
    make_monthly_prices_plot()
    doctest.testmod()