import pandas as pd

def analisis_estadistico(valores):
    
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

# Importar el archivo CSV
df_alumnos = pd.read_csv("alumnos.csv")

# Obtener los valores de la columna "fi" del DataFrame
valores_alumnos = df_alumnos["fi"].tolist()

# Llamar a la función analisis_estadistico con los valores de alumnos
results = analisis_estadistico(valores_alumnos)
print(results)
