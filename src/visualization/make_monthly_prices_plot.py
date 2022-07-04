def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios mensuales.

    Usando el archivo data_lake/business/precios-mensuales.csv, crea un grafico de
    lines que representa los precios promedios mensuales.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/monthly_prices.png.
    """
    #raise NotImplementedError("Implementar esta función")
    
    import pandas as pd

    daily_prices = pd.read_csv(
        'data_lake/business/precios-mensuales.csv', index_col=None, header=0)
    daily_prices.plot.line(x='Fecha', y='Precio').get_figure().savefig(
        'data_lake/business/reports/figures/monthly_prices.png')

if __name__ == "__main__":
    import doctest
    make_monthly_prices_plot()
    doctest.testmod()