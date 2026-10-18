"""Predict whether a home sells above the median SalePrice."""

from pathlib import Path
from math import exp

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


CSV_PATH = Path(__file__).with_name("AmesHousingClean.csv")

# These names match the column headers in AmesHousingClean.csv.
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


def main() -> None:
    data = pd.read_csv(CSV_PATH)

    required_columns = FEATURES + ["SalePrice"]
    missing_columns = [column for column in required_columns if column not in data.columns]
    if missing_columns:
        raise ValueError(f"Missing expected columns: {', '.join(missing_columns)}")

    # Compute the threshold from the dataset. Ties at the median are classified
    # as "At or below median"; only prices strictly greater than it are "Above median".
    median_price = data["SalePrice"].median()
    data["AboveMedian"] = (data["SalePrice"] > median_price).astype(int)

    X = data[FEATURES]
    y = data["AboveMedian"]

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
            ("classifier", LogisticRegression(max_iter=2000)),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(f"Median SalePrice: ${median_price:,.0f}")
    print("Target: 1 = Above median; 0 = At or below median")
    print(f"Homes above median: {(y == 1).sum():,}")
    print(f"Homes at or below median: {(y == 0).sum():,}")
    print(f"Test accuracy: {accuracy_score(y_test, predictions):.3f}")
    print("\nConfusion matrix (rows = actual, columns = predicted; 0 then 1):")
    print(confusion_matrix(y_test, predictions))
    print("\nClassification report:")
    print(
        classification_report(
            y_test,
            predictions,
            labels=[0, 1],
            target_names=["At or below median", "Above median"],
            zero_division=0,
        )
    )

    # Positive coefficients indicate higher odds of being above the median;
    # negative coefficients indicate lower odds, holding other model inputs fixed.
    fitted_preprocessing = model.named_steps["preprocessing"]
    feature_names = fitted_preprocessing.get_feature_names_out()
    coefficients = model.named_steps["classifier"].coef_[0]
    effects = pd.DataFrame({"Feature": feature_names, "Coefficient": coefficients})
    effects["Odds ratio"] = effects["Coefficient"].map(exp)
    effects["Abs coefficient"] = effects["Coefficient"].abs()
    effects = effects.sort_values("Abs coefficient", ascending=False)

    print("\nModel feature effects (sorted by absolute coefficient):")
    print(effects[["Feature", "Coefficient", "Odds ratio"]].to_string(index=False))
    print("\nCoefficient note: numeric features were standardized; categorical features were one-hot encoded.")


if __name__ == "__main__":
    main()
