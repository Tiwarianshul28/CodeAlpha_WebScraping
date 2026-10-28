
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Demo website for practicing web scraping
url = "https://books.toscrape.com/"

try:
    response = requests.get(
        url,
        timeout=15,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for book in soup.select("article.product_pod"):
        title_tag = book.select_one("h3 a")
        price_tag = book.select_one(".price_color")
        rating_tag = book.select_one("p.star-rating")

        if title_tag and price_tag:
            books.append({
                "Title": title_tag.get("title", title_tag.get_text(strip=True)),
                "Price": price_tag.get_text(strip=True),
                "Rating": (
                    rating_tag.get("class", ["Unknown"])[1]
                    if rating_tag and len(rating_tag.get("class", [])) > 1
                    else "Unknown"
                )
            })

    if books:
        df = pd.DataFrame(books)
        df.to_csv("books_data.csv", index=False)

        print("Web scraping completed successfully!")
        print(f"Total books extracted: {len(df)}")
        print("\nFirst 5 records:")
        print(df.head())
        print("\nData saved to books_data.csv")
    else:
        print("No books found. Please check the website structure.")

except requests.RequestException as error:
    print("Website request failed:", error)
