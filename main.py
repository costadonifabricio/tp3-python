import pandas as pd

def analisis_estadistico(valores):
    # Validar que la lista de valores no esté vacía
    if not valores:
        return ("La lista de valores está vacía")
    # Validar que la lista de valores tenga solo números
    if not all(isinstance(x, (int, float)) for x in valores):
        return ("La lista de valores contiene elementos no numéricos.")
    # Validar que el argumento sea una lista
    if not isinstance(valores, list):
        return ("El argumento no es una lista.")
    # Crear un DataFrame a partir de la lista de valores
    df = pd.DataFrame(valores, columns=["fi"])
    
    # Calcular Fi (frecuencia acumulada)
    df["Fi"] = df["fi"].cumsum()
    
    # Calcular fri (frecuencia relativa)
    df["fri"] = df["fi"] / df["fi"].sum()
    
    # Calcular Fri (frecuencia relativa acumulada)
    df["Fri"] = df["fri"].cumsum()
    
    # Calcular pi% (probabilidad)
    df["pi%"] = df["fri"] * 100
    
    # Calcular Pi% (probabilidad acumulada)
    df["Pi%"] = df["Fri"] * 100
    
    return df

# Edades de alumnos
df_alumnos = [
    1, 9, 4, 3, 4, 1, 0 ,1, 0, 0, 2, 2, 1, 0, 0, 0, 2 
]


# Llamar a la función analisis_estadistico con los valores de alumnos
results = analisis_estadistico(df_alumnos).round(2)
print(results)
