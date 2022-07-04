def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    import pickle
    import numpy as np
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    from sklearn.ensemble import RandomForestRegressor

    
    
    #Se crea un modelo de regresion lineal simple donde la variable explicada es el precio en funcion del tiempo. Serie de tiempo
    df = pd.read_csv("data_lake/business/features/precios-diarios.csv", encoding = 'utf-8', sep=',')

    df["fecha"] = pd.to_datetime(df["fecha"]).dt.strftime('%Y%m%d')
    fecha = np.array(df['fecha']).reshape(-1,1)
    precio = np.array(df['precio']).reshape(-1,1)
    
    (X_train, X_test, y_train, y_test,) = train_test_split(fecha, precio, test_size=0.25, random_state=100000,)
    glm = RandomForestRegressor(n_estimators=100, max_features='sqrt', n_jobs=-1, oob_score = True, random_state = 100000)
    glm.fit(X_train,y_train)

    pickle.dump(glm, open('src/models/precios-diarios.pickle', 'wb'))

    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()
