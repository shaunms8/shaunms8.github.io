import numpy as np
import pandas as pd
from scipy.stats import ttest_ind


START_DATE = "2024-08-01"
END_DATE = "2024-10-31"

def assign_risk_level(risk_score):
    """
    Assigns a readable risk level based on the calculated risk score.

    Args:
        risk_score (float): The calculated storm/crime risk score.

    Returns:
        str: Risk level label.
    """
    if risk_score >= 2.0:
        return "High"
    elif risk_score >= 1.0:
        return "Moderate"
    else:
        return "Low"
    
def calculate_risk_score(crime_count, baseline_crime, storm_count):
    """
    Calculates a risk score for a date based on crime activity and storm activity.

    The score increases when crime count is above the baseline and when storm
    events are present on the same date.

    Args:
        crime_count (int): Number of crime incidents on the date.
        baseline_crime (float): Average daily crime count.
        storm_count (int): Number of storm events on the date.

    Returns:
        float: Calculated risk score.
    """
    if baseline_crime <= 0:
        return 0.0

    crime_factor = crime_count / baseline_crime
    storm_factor = storm_count

    return round(crime_factor + storm_factor, 2)

def rank_storm_crime_risk(daily_summary):
    """
    Ranks dates where storm activity overlaps with higher-than-normal crime activity.

    This function represents the Category Two Algorithms and Data Structures enhancement.
    It uses dictionaries, a set, a list, and a pandas DataFrame to identify and rank
    dates with both storm activity and elevated crime counts.

    Args:
        daily_summary (DataFrame): DataFrame with Date, CrimeCount, and StormCount columns.

    Returns:
        DataFrame: Ranked dates with crime count, storm count, risk score, and risk level.
    """
    required_columns = {"Date", "CrimeCount", "StormCount"}

    if not required_columns.issubset(daily_summary.columns):
        missing = required_columns - set(daily_summary.columns)
        raise ValueError(f"daily_summary is missing required columns: {missing}")

    daily_summary = daily_summary.copy()
    daily_summary["Date"] = pd.to_datetime(daily_summary["Date"])

    crime_by_day = dict(zip(daily_summary["Date"], daily_summary["CrimeCount"]))
    storm_by_day = dict(zip(daily_summary["Date"], daily_summary["StormCount"]))

    storm_dates = set(
        daily_summary.loc[daily_summary["StormCount"] > 0, "Date"]
    )

    baseline_crime = daily_summary["CrimeCount"].mean()

    ranked_results = []

    for current_date in daily_summary["Date"]:
        crime_count = crime_by_day.get(current_date, 0)
        storm_count = storm_by_day.get(current_date, 0)

        if current_date in storm_dates and crime_count > baseline_crime:
            risk_score = calculate_risk_score(
                crime_count=crime_count,
                baseline_crime=baseline_crime,
                storm_count=storm_count
            )

            ranked_results.append({
                "Date": current_date,
                "CrimeCount": crime_count,
                "StormCount": storm_count,
                "BaselineCrime": round(baseline_crime, 2),
                "RiskScore": risk_score,
                "RiskLevel": assign_risk_level(risk_score)
            })

    ranked_df = pd.DataFrame(ranked_results)

    if ranked_df.empty:
        return pd.DataFrame(
            columns=[
                "Date",
                "CrimeCount",
                "StormCount",
                "BaselineCrime",
                "RiskScore",
                "RiskLevel"
            ]
        )

    ranked_df = ranked_df.sort_values(
        by="RiskScore",
        ascending=False
    ).reset_index(drop=True)

    return ranked_df


def create_daily_summary(crime_df: pd.DataFrame, storm_df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate cleaned crime and storm datasets into one daily summary table.

    The output contains one row for each date from August 1, 2024 through
    October 31, 2024, with daily crime counts, storm counts, and a storm-day label.
    """
    daily_crime = (
        crime_df.groupby("CrimeDate")
        .size()
        .reset_index(name="CrimeCount")
    )

    daily_storm = (
        storm_df.groupby("StormDate")
        .size()
        .reset_index(name="StormCount")
    )

    date_range = pd.DataFrame({
        "Date": pd.date_range(start=START_DATE, end=END_DATE, freq="D")
    })

    daily_summary = date_range.merge(
        daily_crime,
        left_on="Date",
        right_on="CrimeDate",
        how="left"
    )

    daily_summary = daily_summary.merge(
        daily_storm,
        left_on="Date",
        right_on="StormDate",
        how="left"
    )

    daily_summary = daily_summary.drop(columns=["CrimeDate", "StormDate"])

    daily_summary["CrimeCount"] = daily_summary["CrimeCount"].fillna(0).astype(int)
    daily_summary["StormCount"] = daily_summary["StormCount"].fillna(0).astype(int)

    daily_summary["StormDay"] = np.where(
        daily_summary["StormCount"] > 0,
        "Storm Day",
        "No Storm Day"
    )

    return daily_summary


def summarize_storm_day_comparison(daily_summary: pd.DataFrame) -> pd.DataFrame:
    """
    Compare crime counts on storm days and non-storm days.
    """
    if daily_summary.empty:
        raise ValueError("Daily summary is empty. Cannot summarize results.")

    return (
        daily_summary.groupby("StormDay")["CrimeCount"]
        .agg(["count", "mean", "median", "max"])
        .round(2)
    )


def calculate_correlation(daily_summary: pd.DataFrame) -> float:
    """
    Calculate the correlation between daily crime count and daily storm count.
    """
    if daily_summary.empty:
        raise ValueError("Daily summary is empty. Cannot calculate correlation.")

    correlation = daily_summary["CrimeCount"].corr(daily_summary["StormCount"])

    if pd.isna(correlation):
        return 0.0

    return round(correlation, 4)


def run_t_test(daily_summary: pd.DataFrame) -> tuple[float, float]:
    """
    Run an independent t-test comparing crime counts on storm days
    and non-storm days.
    """
    if daily_summary.empty:
        raise ValueError("Daily summary is empty. Cannot run t-test.")

    crime_on_storm_days = daily_summary.loc[
        daily_summary["StormCount"] > 0,
        "CrimeCount"
    ]

    crime_on_nonstorm_days = daily_summary.loc[
        daily_summary["StormCount"] == 0,
        "CrimeCount"
    ]

    if crime_on_storm_days.empty or crime_on_nonstorm_days.empty:
        return 0.0, 1.0

    t_stat, p_value = ttest_ind(
        crime_on_storm_days,
        crime_on_nonstorm_days,
        equal_var=False,
        nan_policy="omit"
    )

    return round(t_stat, 4), round(p_value, 4)