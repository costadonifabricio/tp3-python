import pandas as pd

def analisis_estadistico(valores):

    # Crear un DataFrame a partir de la lista de valores
    df = pd.DataFrame(valores, columns=["fi"])
    
    # Calcular Fi (frecuencia acumulada)
    df["Fi"] = df["fi"].cumsum()
    
    # Calcular fri (frecuencia relativa)
    df["fri"] = (df["fi"] / df["fi"].sum())
    
    # Calcular Fri (frecuencia relativa acumulada)
    df["Fri"] = df["fri"].cumsum()
    
    # Calcular pi% (probabilidad)
    df["pi%"] = df["fri"] * 100
    
    # Calcular Pi% (probabilidad acumulada)
    df["Pi%"] = df["Fri"] * 100
    
    # Almacenar los resultados en un diccionario
    results = {
        "fi": df["fi"],
        "Fi": df["Fi"],
        "fri": df["fri"],
        "Fri": df["Fri"],
        "pi%": df["pi%"],
        "Pi%": df["Pi%"],
    }
    return results

# Caso de Prueba con el fi de edades del excel cargados manuealmente
valores_ejemplo = [1, 9, 4, 3, 4, 1, 0, 1, 0, 0
                    , 2, 2, 1, 0, 0, 0, 2]
results = analisis_estadistico(valores_ejemplo)
print(results)


