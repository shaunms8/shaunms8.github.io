from config import load_config
from database import (
    create_connection,
    close_connection,
    get_crime_data,
    get_storm_data,
)
from cleaning import clean_crime_data, clean_storm_data
from analysis import (
    create_daily_summary,
    summarize_storm_day_comparison,
    calculate_correlation,
    run_t_test,
    rank_storm_crime_risk,
)
from visualization import create_crime_storm_chart
from reporting import export_daily_summary, export_text_report


def main() -> None:
    """
    Run the Miami Crime and Storm Data Analysis workflow.

    This function controls the full software flow:
    1. Load database configuration
    2. Connect to MySQL
    3. Retrieve crime and storm data
    4. Clean and validate the data
    5. Analyze daily crime and storm activity
    6. Create visualizations
    7. Export reports
    8. Close the database connection
    """
    connection = None

    try:
        print("Loading configuration...")
        config = load_config()

        print("Connecting to MySQL database...")
        connection = create_connection(config)

        print("Retrieving crime data...")
        crime_data = get_crime_data(connection)

        print("Retrieving storm data...")
        storm_data = get_storm_data(connection)

        print("Cleaning crime data...")
        clean_crime = clean_crime_data(crime_data)

        print("Cleaning storm data...")
        clean_storms = clean_storm_data(storm_data)

        print("Creating daily summary...")
        daily_summary = create_daily_summary(clean_crime, clean_storms)

        print("Ranking storm/crime risk dates...")
        risk_rankings = rank_storm_crime_risk(daily_summary)

        print("\nTop Ranked Storm/Crime Risk Dates:")
        print(risk_rankings.head(10))

        risk_rankings.to_csv(
            "output/reports/storm_crime_risk_rankings.csv",
            index=False
        )

        print("Running analysis...")
        storm_day_summary = summarize_storm_day_comparison(daily_summary)
        correlation = calculate_correlation(daily_summary)
        t_stat, p_value = run_t_test(daily_summary)

        print("Exporting daily summary CSV...")
        export_daily_summary(
            daily_summary,
            "output/reports/miami_daily_crime_storm_summary.csv"
        )

        print("Creating visualization...")
        create_crime_storm_chart(
            daily_summary,
            "output/charts/miami_crime_storm_activity.png"
        )

        print("Exporting text report...")
        export_text_report(
            storm_day_summary,
            correlation,
            t_stat,
            p_value,
            "output/reports/miami_crime_storm_report.txt"
        )

        print("\nAnalysis completed successfully.")
        print("Files created:")
        print("- output/reports/miami_daily_crime_storm_summary.csv")
        print("- output/reports/storm_crime_risk_rankings.csv")
        print("- output/charts/miami_crime_storm_activity.png")
        print("- output/reports/miami_crime_storm_report.txt")

    except Exception as error:
        print("\nAnalysis failed.")
        print(f"Error: {error}")

    finally:
        print("Closing database connection...")
        close_connection(connection)


if __name__ == "__main__":
    main()