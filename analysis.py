import numpy as np
import pandas as pd
from scipy.stats import ttest_ind


START_DATE = "2024-08-01"
END_DATE = "2024-10-31"


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