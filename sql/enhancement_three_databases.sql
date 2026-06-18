USE dat375;

DROP VIEW IF EXISTS clean_miami_crime;

CREATE VIEW clean_miami_crime AS
SELECT
    DATE(STR_TO_DATE(CFSDate, '%Y-%m-%d %H:%i:%s.%f')) AS crime_date,
    TIME(STR_TO_DATE(CFSDate, '%Y-%m-%d %H:%i:%s.%f')) AS crime_time,
    TRIM(IncidentType) AS incident_type,
    TRIM(BeatName) AS beat_name,
    TRIM(Neighborhood) AS neighborhood,
    TRIM(CommissionDistrict) AS commission_district,
    CAST(NULLIF(TRIM(Longitude), '') AS DECIMAL(10, 7)) AS longitude,
    CAST(NULLIF(TRIM(Latitude), '') AS DECIMAL(10, 7)) AS latitude
FROM mpdcrimedata
WHERE CFSDate IS NOT NULL
  AND STR_TO_DATE(CFSDate, '%Y-%m-%d %H:%i:%s.%f') >= '2024-08-01'
  AND STR_TO_DATE(CFSDate, '%Y-%m-%d %H:%i:%s.%f') < '2024-11-01'
  AND IncidentType IS NOT NULL
  AND TRIM(IncidentType) <> '';

DROP VIEW IF EXISTS clean_miami_storms;

CREATE VIEW clean_miami_storms AS
SELECT
    STR_TO_DATE(
        CONCAT(BEGIN_YEARMONTH, LPAD(BEGIN_DAY, 2, '0')),
        '%Y%m%d'
    ) AS storm_date,
    TRIM(EVENT_TYPE) AS event_type,
    TRIM(CZ_NAME) AS county_zone,
    TRIM(STATE) AS state_name,
    NULLIF(TRIM(MAGNITUDE), '') AS magnitude
FROM stormevents2024
WHERE TRIM(STATE) = 'FLORIDA'
  AND TRIM(CZ_NAME) LIKE '%MIAMI-DADE%'
  AND BEGIN_YEARMONTH BETWEEN 202408 AND 202410
  AND EVENT_TYPE IS NOT NULL
  AND TRIM(EVENT_TYPE) <> '';

DROP VIEW IF EXISTS daily_crime_summary;

CREATE VIEW daily_crime_summary AS
SELECT
    crime_date AS summary_date,
    COUNT(*) AS daily_crime_count,
    COUNT(DISTINCT incident_type) AS unique_incident_types
FROM clean_miami_crime
GROUP BY crime_date;

DROP VIEW IF EXISTS daily_storm_summary;

CREATE VIEW daily_storm_summary AS
SELECT
    storm_date AS summary_date,
    COUNT(*) AS storm_event_count,
    COUNT(DISTINCT event_type) AS unique_storm_types,
    GROUP_CONCAT(DISTINCT event_type ORDER BY event_type SEPARATOR ', ') AS storm_event_types
FROM clean_miami_storms
GROUP BY storm_date;

DROP TABLE IF EXISTS miami_crime_storm_summary;

CREATE TABLE miami_crime_storm_summary AS
SELECT
    c.summary_date,
    c.daily_crime_count,
    c.unique_incident_types,
    COALESCE(s.storm_event_count, 0) AS storm_event_count,
    COALESCE(s.unique_storm_types, 0) AS unique_storm_types,
    COALESCE(s.storm_event_types, 'No Storm Event') AS storm_event_types,
    CASE
        WHEN COALESCE(s.storm_event_count, 0) > 0 THEN 'Storm Day'
        ELSE 'No Storm Day'
    END AS storm_day_flag
FROM daily_crime_summary c
LEFT JOIN daily_storm_summary s
    ON c.summary_date = s.summary_date
ORDER BY c.summary_date;

CREATE INDEX idx_miami_summary_date
ON miami_crime_storm_summary(summary_date);

-- =====================================================
-- Validation Queries
-- =====================================================

SELECT COUNT(*) AS clean_crime_records
FROM clean_miami_crime;

SELECT COUNT(*) AS clean_storm_records
FROM clean_miami_storms;

SELECT COUNT(*) AS combined_summary_records
FROM miami_crime_storm_summary;

SELECT
    storm_day_flag,
    COUNT(*) AS day_count,
    ROUND(AVG(daily_crime_count), 2) AS avg_daily_crime,
    MAX(daily_crime_count) AS max_daily_crime
FROM miami_crime_storm_summary
GROUP BY storm_day_flag;

SELECT *
FROM miami_crime_storm_summary
ORDER BY summary_date;