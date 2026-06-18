from pathlib import Path

import pandas as pd


def export_daily_summary(daily_summary: pd.DataFrame, output_path: str) -> None:
    """
    Export the daily crime and storm summary dataset to a CSV file.

    Args:
        daily_summary: DataFrame containing the final daily summary.
        output_path: File path where the CSV file will be saved.
    """
    if daily_summary.empty:
        raise ValueError("Daily summary is empty. Cannot export CSV.")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    daily_summary.to_csv(output_path, index=False)


def export_text_report(
    storm_day_summary: pd.DataFrame,
    correlation: float,
    t_stat: float,
    p_value: float,
    output_path: str
) -> None:
    """
    Export a text report summarizing the Miami crime and storm analysis.

    Args:
        storm_day_summary: Summary table comparing storm days and non-storm days.
        correlation: Correlation between daily crime counts and storm counts.
        t_stat: T-test statistic.
        p_value: T-test p-value.
        output_path: File path where the text report will be saved.
    """
    if storm_day_summary.empty:
        raise ValueError("Storm day summary is empty. Cannot export report.")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    report = f"""
Miami Crime and Storm Data Analysis Report

Analysis Period:
August 1, 2024 through October 31, 2024

Purpose:
This report compares Miami crime activity with Miami-Dade storm event activity to determine whether storm days show different crime patterns than non-storm days.

Storm Day Crime Summary:
{storm_day_summary.to_string()}

Correlation Between Daily Crime Count and Daily Storm Count:
{correlation}

T-Test Results:
t-statistic: {t_stat}
p-value: {p_value}

Interpretation:
The correlation value shows the strength and direction of the relationship between daily crime counts and storm event counts. A value close to 0 suggests little or no linear relationship. A positive value suggests crime counts increase as storm counts increase, while a negative value suggests crime counts decrease as storm counts increase.

The t-test compares average crime counts on storm days and non-storm days. A lower p-value may suggest a more meaningful difference between the two groups, while a higher p-value suggests the difference may not be statistically significant.

Software Design Enhancement:
This report was generated as part of the Category One Software Design and Engineering enhancement. The original notebook-based workflow was redesigned into a modular Python project with separate files for configuration, database access, cleaning, analysis, visualization, and reporting.
"""

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report.strip())