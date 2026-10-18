"""Plot a histogram of SalePrice from AmesHousingClean.csv."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


CSV_PATH = Path(__file__).with_name("AmesHousingClean.csv")
OUTPUT_PATH = Path(__file__).with_name("SalePriceHistogram.png")


def main() -> None:
    data = pd.read_csv(CSV_PATH)

    if "SalePrice" not in data.columns:
        raise ValueError("The CSV file does not contain a 'SalePrice' column.")

    sale_prices = pd.to_numeric(data["SalePrice"], errors="coerce").dropna()

    plt.hist(sale_prices, bins=30, edgecolor="black")
    plt.title("Distribution of Sale Prices")
    plt.xlabel("Sale Price ($)")
    plt.ylabel("Number of Houses")
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH, dpi=300)
    plt.show()


if __name__ == "__main__":
    main()
