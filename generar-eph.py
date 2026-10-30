import numpy as np
import pandas as pd

# Semilla para que a todos les de igual
np.random.seed(42)
n_registros = 1000

# 1. DATOS DEL HOGAR
codusu_list = [f"HOG_EPH_2026_{i:04d}" for i in range(1, n_registros + 1)]

# Regiones INDEC con porcentajes reales
regiones = np.random.choice([1, 40, 41, 42, 43, 44], 
                            size=n_registros, 
                            p=[0.35, 0.15, 0.15, 0.10, 0.15, 0.10])

# Cantidad de personas por hogar
integrantes = np.random.poisson(lam=2.3, size=n_registros) + 1

# 2. NIVEL EDUCATIVO DEL JEFE
nivel_ed = np.random.choice([1, 2, 3, 4, 5, 9], 
                            size=n_registros, 
                            p=[0.08, 0.22, 0.30, 0.25, 0.13, 0.02])

# 3. INGRESO TOTAL FAMILIAR
itf_base = np.random.lognormal(mean=11.5, sigma=0.6, size=n_registros)
df_temp = pd.DataFrame({"nivel": nivel_ed, "base": itf_base})
multiplicador = {1:0.7, 2:0.85, 3:1.0, 4:1.2, 5:1.8, 9:1.0}
df_temp["itf"] = df_temp.apply(lambda x: x["base"] * multiplicador[x["nivel"]], axis=1)

# Crear tabla final
df = pd.DataFrame({
    "CODUSU": codusu_list,
    "REGION": regiones,
    "CANT_PERSONAS": integrantes,
    "NIVEL_ED_JEFE": nivel_ed,
    "ITF": df_temp["itf"].round(2)
})

# Guardar
df.to_csv("EPH_sintetica_oficial_2026.csv", index=False)
print("¡Archivo creado con exito! 1000 hogares")
print(df.head())
