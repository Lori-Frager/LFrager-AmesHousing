"""Print summary statistics for selected variables in AmesHousingClean.csv."""

from pathlib import Path

import pandas as pd


CSV_PATH = Path(__file__).with_name("AmesHousingClean.csv")
VARIABLES = [
    "Year Built",
    "Gr Liv Area",
    "Bedroom AbvGr",
    "TotRms AbvGrd",
    "Garage Area",
]


def main() -> None:
    data = pd.read_csv(CSV_PATH)

    missing_columns = [column for column in VARIABLES if column not in data.columns]
    if missing_columns:
        raise ValueError(f"Missing expected columns: {', '.join(missing_columns)}")

    # describe() reports count, mean, standard deviation, min, quartiles, and max.
    print(data[VARIABLES].describe().to_string())


if __name__ == "__main__":
    main()
