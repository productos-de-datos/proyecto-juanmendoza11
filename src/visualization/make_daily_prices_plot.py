def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.
    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.
    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.
    """
    import matplotlib.pyplot as plt
    import pandas as pd
    
    # Se crea la grafica de precios diarios y se transfiere a la capa business.
    df = pd.read_csv('data_lake/business/precios-diarios.csv')
    plot = df.plot(x='fecha', y = 'precio', kind = 'line').get_figure()
    plot.savefig('data_lake/business/reports/figures/daily_prices.png')

    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    make_daily_prices_plot()