import pandas as pd
import re

def limpiar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r"[^\w\s]", "", texto)
    return texto

def main():
    print("Procesando datos...")

    df = pd.read_csv("data/raw.csv")

    # Limpieza básica
    df = df.dropna()
    df["longitud_titulo"] = df["titulo"].apply(len)

    df.to_csv("data/clean.csv", index=False, encoding="utf-8")

    # Resumen: top palabras
    palabras = (
        df["titulo"]
        .apply(limpiar_texto)
        .str.split()
        .explode()
    )

    resumen = palabras.value_counts().head(20).reset_index()
    resumen.columns = ["palabra", "frecuencia"]

    resumen.to_csv("data/summary.csv", index=False, encoding="utf-8")

    print("Archivos creados:")
    print("- data/clean.csv")
    print("- data/summary.csv")

if __name__ == "__main__":
    main()
 