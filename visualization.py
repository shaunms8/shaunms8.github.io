from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def create_crime_storm_chart(daily_summary: pd.DataFrame, output_path: str) -> None:
    """
    Create and save a line chart comparing daily crime counts and storm counts.

    Args:
        daily_summary: DataFrame containing Date, CrimeCount, and StormCount columns.
        output_path: File path where the chart image will be saved.
    """
    if daily_summary.empty:
        raise ValueError("Daily summary is empty. Cannot create visualization.")

    required_columns = ["Date", "CrimeCount", "StormCount"]
    missing_columns = [
        column for column in required_columns
        if column not in daily_summary.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing columns for visualization: {missing_columns}")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(
        daily_summary["Date"],
        daily_summary["CrimeCount"],
        label="Crime Count"
    )

    ax.plot(
        daily_summary["Date"],
        daily_summary["StormCount"],
        label="Storm Count"
    )

    ax.set_title("Miami Daily Crime and Storm Activity")
    ax.set_xlabel("Date")
    ax.set_ylabel("Daily Count")
    ax.legend()
    ax.grid(True)

    fig.autofmt_xdate()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)