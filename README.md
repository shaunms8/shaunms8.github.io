# Miami Crime and Storm Data Analysis System

## Project Overview

This project analyzes Miami crime data and Miami-Dade storm event data to examine whether storm activity overlaps with changes in daily crime activity. The analysis focuses on the date range of August 1, 2024 through October 31, 2024.

The project was enhanced for CS 499 Category One: Software Design and Engineering. The original artifact was notebook-based, and this enhanced version redesigns the workflow into a modular Python project.

## Code Review Video

The CS 499 code review video reviews the original Miami Crime and Storm Data Analysis System artifact, explains code review findings, and describes planned enhancements for software design and engineering, algorithms and data structures, and databases.

Video link: [Code Review Video] https://youtu.be/gVhiYFHuaxI

## Enhancement Category

Category One: Software Design and Engineering

## Enhancement Summary

The original project was completed through a Jupyter Notebook-style workflow. While the original version performed the analysis, the code was less modular and harder to maintain, test, reuse, or expand.

This enhanced version separates the project into individual Python modules:

- `config.py` handles configuration and environment variables.
- `database.py` handles MySQL connection and SQL queries.
- `cleaning.py` handles data validation and cleaning.
- `analysis.py` handles data aggregation and statistical analysis.
- `visualization.py` creates and saves the chart.
- `reporting.py` exports the CSV and text report.
- `main.py` controls the full program workflow.

## Project Structure

```text
miami_crime_storm_analysis/
├── main.py
├── config.py
├── database.py
├── cleaning.py
├── analysis.py
├── visualization.py
├── reporting.py
├── requirements.txt
├── README.md
├── .env
└── output/
    ├── charts/
    └── reports/

