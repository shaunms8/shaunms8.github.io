import mysql.connector
import pandas as pd
from mysql.connector import Error
from config import DatabaseConfig


def create_connection(config: DatabaseConfig):
    """Create and return a MySQL database connection."""
    try:
        connection = mysql.connector.connect(
            host=config.host,
            port=config.port,
            user=config.user,
            password=config.password,
            database=config.database,
        )

        if connection.is_connected():
            return connection

        raise ConnectionError("Database connection was not established.")

    except Error as error:
        raise ConnectionError(f"MySQL connection failed: {error}") from error


def sql_to_dataframe(query: str, connection) -> pd.DataFrame:
    """Run a SQL query and return the result as a pandas DataFrame."""
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        cursor.close()
        return pd.DataFrame(rows, columns=columns)

    except Error as error:
        raise RuntimeError(f"SQL query failed: {error}") from error


def get_crime_data(connection) -> pd.DataFrame:
    """Retrieve Miami crime records for August 1, 2024 through October 31, 2024."""
    query = """
        SELECT
            DATE(CFSDate) AS CrimeDate,
            TIME(CFSDate) AS CrimeTime,
            IncidentType,
            BeatName,
            Neighborhood,
            CommissionDistrict
        FROM mpdcrimedata
        WHERE CFSDate >= '2024-08-01'
          AND CFSDate < '2024-11-01'
          AND IncidentType IS NOT NULL
          AND TRIM(IncidentType) <> '';
    """
    return sql_to_dataframe(query, connection)


def get_storm_data(connection) -> pd.DataFrame:
    """Retrieve Miami-Dade storm records for August 1, 2024 through October 31, 2024."""
    query = """
        SELECT
            STR_TO_DATE(
                CONCAT(BEGIN_YEARMONTH, RIGHT(CONCAT('0', BEGIN_DAY), 2)),
                '%Y%m%d'
            ) AS StormDate,
            EVENT_TYPE,
            CZ_NAME
        FROM stormevents2024
        WHERE TRIM(STATE) = 'FLORIDA'
          AND TRIM(CZ_NAME) LIKE '%MIAMI-DADE%'
          AND BEGIN_YEARMONTH BETWEEN 202408 AND 202410;
    """
    return sql_to_dataframe(query, connection)


def close_connection(connection) -> None:
    """Close the database connection if it is open."""
    if connection and connection.is_connected():
        connection.close()