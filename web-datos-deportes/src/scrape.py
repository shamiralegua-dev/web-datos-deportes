import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.bbc.com/sport/football"

def main():
    print("🔥 SCRAPING BBC SPORT 🔥")
    response = requests.get(URL, timeout=30)
    soup = BeautifulSoup(response.text, "html.parser")

    articulos = soup.find_all("a")

    data = []

    for art in articulos:
        titulo = art.get_text(strip=True)
        link = art.get("href")

        if titulo and link and "football" in link:
            if link.startswith("/"):
                link = "https://www.bbc.com" + link

            data.append({
                "titulo": titulo,
                "url": link
            })

    df = pd.DataFrame(data).drop_duplicates()
    df.to_csv("data/raw.csv", index=False, encoding="utf-8")

    print("FILAS:", len(df))
    print("Archivo creado: data/raw.csv")

if __name__ == "__main__":
    main()
