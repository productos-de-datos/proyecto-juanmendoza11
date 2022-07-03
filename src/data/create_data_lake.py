def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """
    # raise NotImplementedError("Implementar esta función")

    import os
    os.mkdir('data_lake')
    first_layer = ['landing', 'raw', 'cleansed', 'business']

    for i in first_layer:
        os.mkdir(os.path.join('data_lake', i))

    business_layer =[
        'business/reports',
        'business/reports/figures',
        'business/features',
        'business/forecasts',]

    
    for i in business_layer:
        os.mkdir(os.path.join("data_lake", i))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    create_data_lake()
