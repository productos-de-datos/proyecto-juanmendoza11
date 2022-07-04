def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score
    import pandas as pd
    import pickle

    #Se crea un modelo de regresion lineal simple donde la variable explicada es el precio en funcion del tiempo. Serie de tiempo
    df = pd.read_csv("data_lake/business/features/precios-diarios.csv", encoding = 'utf-8', sep=',')

    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')
    df['year'], df['month'], df['day'] = \
        df['Fecha'].dt.year, df['fecha'].dt.month, df['fecha'].dt.day
    
    fechas = df.copy().drop('fecha', axis=1)
    precios = x_total.pop('precio')
    
    x_train = fechas[:round(fechas.shape[0]*0.75)]
    x_test = fechas[round(fechas.shape[0]*0.75):]
    y_train = precios[:round(fechas.shape[0]*0.75)]
    y_test = precios[round(fechas.shape[0]*0.75):]
    
    glm = LinearRegression()
    glm.fit(x_train, y_train)
    
    r2_score(y_test,regression.predict(x_test))

    pickle.dump(glm, open('src/models/precios-diarios.pkl', 'wb'))
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()
