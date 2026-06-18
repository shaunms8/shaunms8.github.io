# Miami Crime and Storm Data Analysis System

## Project Overview

This project analyzes Miami crime data and Miami-Dade storm event data to examine whether storm activity overlaps with changes in daily crime activity. The analysis focuses on the date range of August 1, 2024 through October 31, 2024.

The project was enhanced for CS 499 Category One: Software Design and Engineering. The original artifact was notebook-based, and this enhanced version redesigns the workflow into a modular Python project.

Repository: [CS 499 Capstone GitHub Repository](github.com/shaunms9/shaunms8.github.io)

## Code Review Video

The CS 499 code review video reviews the original Miami Crime and Storm Data Analysis System artifact, explains code review findings, and describes planned enhancements for software design and engineering, algorithms and data structures, and databases.

Video link: [Code Review Video](https://youtu.be/gVhiYFHuaxI)

# Enhancement Categories

## Category One: Software Design and Engineering

Enhancement Summary

The original project was completed through a Jupyter Notebook-style workflow. While the original version performed the analysis, the code was less modular and harder to maintain, test, reuse, or expand.

This enhanced version separates the project into individual Python modules:

- `config.py` handles configuration and environment variables.
- `database.py` handles MySQL connection and SQL queries.
- `cleaning.py` handles data validation and cleaning.
- `analysis.py` handles data aggregation and statistical analysis.
- `visualization.py` creates and saves the chart.
- `reporting.py` exports the CSV and text report.
- `main.py` controls the full program workflow.

## Category Two: Algorithms and Data Structures

Enhancement Summary

For the algorithms and data structures enhancement, I added a risk-ranking algorithm that compares daily Miami crime counts with Miami-Dade storm event counts. The algorithm uses pandas DataFrames for grouped daily summaries, dictionaries for fast date-based lookup, a set for efficient storm-date matching, and a list of dictionaries to build ranked output records.

The algorithm calculates the average daily crime count as a baseline. It then checks each date in the selected range and identifies dates where storm activity occurred and crime activity was above the baseline. For those dates, the program calculates a risk score, assigns a risk level, sorts the dates by highest risk score, and exports the results to a CSV file.

This enhancement demonstrates algorithmic thinking because it goes beyond displaying data and creates a repeatable process for identifying dates where crime and storm activity overlap in a meaningful way.

## Category Three: Databases

Enhancement Summary

For the database enhancement, I improved the MySQL portion of the Miami Crime and Storm Data Analysis System. The original project pulled raw crime and storm records into Python and performed much of the filtering, grouping, and merging in pandas. The enhanced version adds reusable SQL views and a combined summary table that prepare the data directly in MySQL before it is used in Python.

This enhancement includes:
- A clean Miami crime view filtered to the selected date range
- A clean Miami-Dade storm event view
- Daily crime and storm aggregation queries
- A combined `miami_crime_storm_summary` table
- SQL validation queries
- Updated Python database access that reads from the enhanced summary table

This demonstrates relational querying, filtering, joining, aggregation, database validation, and secure database-to-Python integration.

## CS 499 Narratives

The following narratives document the completed enhancements for the Miami Crime and Storm Data Analysis System. Each narrative explains the purpose of the enhancement, the technical improvements made, and how the work aligns with the CS 499 course outcomes.

- [Milestone Two Narrative: Software Engineering and Design](narratives/CS%20499%20Milestone%20Two%20Narrative.docx)
- [Milestone Three Narrative: Algorithms and Data Structures](narratives/CS%20499%20Milestone%20Three%20Narrative.docx)
- [Milestone Four Narrative: Databases](narratives/CS%20499%20Milestone%20Four%20Narrative.docx)

## Project Structure

miami_crime_storm_analysis/
├── database/
│   └── dat375_export.sql
├── narratives/
│   ├── CS 499 Milestone Two Narrative.docx
│   ├── CS 499 Milestone Three Narrative.docx
│   └── CS 499 Milestone Four Narrative.docx
├── original_artifact/
│   ├── dat375mod4Project_shaunSanders.ipynb
│   └── README.md
├── output/
│   ├── charts/
│   │   └── miami_crime_storm_activity.png
│   └── reports/
│       ├── miami_daily_crime_storm_summary.csv
│       ├── storm_crime_risk_rankings.csv
│       └── miami_crime_storm_report.txt
├── sql/
│   └── enhancement_three_databases.sql
├── .gitignore
├── analysis.py
├── cleaning.py
├── config.py
├── database.py
├── main.py
├── README.md
├── reporting.py
├── requirements.txt
└── visualization.py