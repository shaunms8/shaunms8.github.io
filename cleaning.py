import pandas as pd


def validate_columns(df: pd.DataFrame, required_columns: list[str], dataset_name: str) -> None:
    """
    Check that a DataFrame contains the required columns.

    Args:
        df: The DataFrame being checked.
        required_columns: Columns that must exist in the DataFrame.
        dataset_name: Name of the dataset for clearer error messages.
    """
    missing_columns = [column for column in required_columns if column not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing columns in {dataset_name}: {missing_columns}")


def clean_crime_data(crime_df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and validate the Miami crime dataset.

    This function checks for required columns, converts the crime date to datetime,
    removes blank incident types, removes invalid dates, and drops duplicate rows.
    """
    if crime_df.empty:
        raise ValueError("Crime data is empty. Check the SQL query or database table.")

    required_columns = [
        "CrimeDate",
        "CrimeTime",
        "IncidentType",
        "BeatName",
        "Neighborhood",
        "CommissionDistrict",
    ]

    validate_columns(crime_df, required_columns, "crime data")

    crime_df = crime_df.copy()

    crime_df["CrimeDate"] = pd.to_datetime(crime_df["CrimeDate"], errors="coerce")
    crime_df["IncidentType"] = crime_df["IncidentType"].astype(str).str.strip()
    crime_df["BeatName"] = crime_df["BeatName"].astype(str).str.strip()
    crime_df["Neighborhood"] = crime_df["Neighborhood"].astype(str).str.strip()
    crime_df["CommissionDistrict"] = crime_df["CommissionDistrict"].astype(str).str.strip()

    crime_df = crime_df.dropna(subset=["CrimeDate"])
    crime_df = crime_df[crime_df["IncidentType"] != ""]
    crime_df = crime_df.drop_duplicates()

    return crime_df


def clean_storm_data(storm_df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and validate the Miami-Dade storm dataset.

    This function checks for required columns, converts the storm date to datetime,
    removes blank storm event types, removes invalid dates, and drops duplicate rows.
    """
    if storm_df.empty:
        raise ValueError("Storm data is empty. Check the SQL query or database table.")

    required_columns = [
        "StormDate",
        "EVENT_TYPE",
        "CZ_NAME",
    ]

    validate_columns(storm_df, required_columns, "storm data")

    storm_df = storm_df.copy()

    storm_df["StormDate"] = pd.to_datetime(storm_df["StormDate"], errors="coerce")
    storm_df["EVENT_TYPE"] = storm_df["EVENT_TYPE"].astype(str).str.strip()
    storm_df["CZ_NAME"] = storm_df["CZ_NAME"].astype(str).str.strip()

    storm_df = storm_df.dropna(subset=["StormDate"])
    storm_df = storm_df[storm_df["EVENT_TYPE"] != ""]
    storm_df = storm_df.drop_duplicates()

    return storm_df