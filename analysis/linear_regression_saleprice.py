"""Fit a linear regression model for SalePrice in AmesHousingClean.csv."""

from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


CSV_PATH = Path(__file__).with_name("AmesHousingClean.csv")

# Exact column names from AmesHousingClean.csv.
NUMERIC_FEATURES = [
    "Year Built",
    "Gr Liv Area",
    "Bedroom AbvGr",
    "TotRms AbvGrd",
    "Garage Area",
    "Overall Qual",
    "Overall Cond",
]
CATEGORICAL_FEATURES = ["Garage Type", "Kitchen Qual"]
FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES
TARGET = "SalePrice"


def main() -> None:
    data = pd.read_csv(CSV_PATH)

    required_columns = FEATURES + [TARGET]
    missing_columns = [column for column in required_columns if column not in data.columns]
    if missing_columns:
        raise ValueError(f"Missing expected columns: {', '.join(missing_columns)}")

    X = data[FEATURES]
    y = pd.to_numeric(data[TARGET], errors="coerce")

    # Remove rows without a usable outcome; predictor missing values are imputed
    # within the pipeline after the train/test split.
    valid_target = y.notna()
    X = X.loc[valid_target]
    y = y.loc[valid_target]

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    preprocessing = ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, NUMERIC_FEATURES),
            ("categorical", categorical_pipeline, CATEGORICAL_FEATURES),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocessing", preprocessing),
            ("regression", LinearRegression()),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(f"Rows used: {len(y):,}")
    print("Predictors:", ", ".join(FEATURES))
    print(f"Test R-squared: {r2_score(y_test, predictions):.3f}")
    print(f"Test mean absolute error: ${mean_absolute_error(y_test, predictions):,.2f}")
    print(f"Test root mean squared error: ${mean_squared_error(y_test, predictions) ** 0.5:,.2f}")

    fitted_preprocessing = model.named_steps["preprocessing"]
    feature_names = fitted_preprocessing.get_feature_names_out()
    coefficients = model.named_steps["regression"].coef_
    coefficient_table = pd.DataFrame(
        {"Feature": feature_names, "Coefficient": coefficients}
    )
    coefficient_table["Abs coefficient"] = coefficient_table["Coefficient"].abs()
    coefficient_table = coefficient_table.sort_values("Abs coefficient", ascending=False)

    print(f"\nIntercept: ${model.named_steps['regression'].intercept_:,.2f}")
    print("\nModel coefficients (sorted by absolute value):")
    print(coefficient_table[["Feature", "Coefficient"]].to_string(index=False))
    print(
        "\nNumeric predictors were standardized, and categorical predictors were "
        "one-hot encoded. Coefficients describe model associations, not causation."
    )


if __name__ == "__main__":
    main()
