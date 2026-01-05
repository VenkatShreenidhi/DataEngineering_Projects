# Spotify Music Analytics ETL Pipeline

## Overview
This project implements an end-to-end **ETL (Extract, Transform, Load) pipeline** for Spotify music analytics data (2015–2025).  
The goal is to ingest raw data, apply data cleaning and transformation logic, enforce data quality rules, and load analytics-ready data into a MySQL database.

The project is designed to reflect **real-world data engineering practices**, including modular pipeline design, SQL-based validation, and proper repository structure.

---

## Architecture
→ Raw CSV Data  
→ Extract (Python)  
→ Transform (Pandas)  
→ Load (MySQL via SQLAlchemy)  
→ Validation & Insights (SQL)

---

## Project Structure

<img width="504" height="474" alt="image" src="https://github.com/user-attachments/assets/a7d7d06f-f9f4-4a9e-ae2a-984b13442ccc" />





---

## ETL Workflow

### Extract
- Reads raw Spotify CSV data from local storage
- Performs basic file validation
- No transformations applied at this stage

### Transform
- Standardizes column names
- Removes duplicate records
- Drops rows missing **primary identifiers** (`track_name`, `artist_name`)
- Handles descriptive metadata (e.g., missing album names)
- Converts and validates numeric fields
- Feature engineering:
  - Track duration (ms → minutes)
  - Popularity buckets (low / medium / high)
  - Release year extraction

### Load
- Loads cleaned data into MySQL using SQLAlchemy
- Batch inserts for efficiency
- Idempotent loads using table replacement
- Database-level constraints applied for data integrity

---

## Data Quality & Validation
Data quality is enforced at **multiple layers**:
- Transformation logic removes invalid records
- MySQL `NOT NULL` constraints protect critical fields
- SQL validation queries verify:
  - Row counts
  - NULL violations
  - Value ranges
  - Data consistency

Validation queries are available in `SQL/01_validation.sql`.

---

## Analytics Insights
The dataset supports downstream analytics such as:
- Popularity trends over time
- Distribution of tracks across popularity buckets
- Explicit vs non-explicit track performance
- High-level catalog composition analysis

Example insight queries are available in `SQL/02_insights.sql`.

---

## Tech Stack
- Python
- Pandas
- SQLAlchemy
- MySQL
- SQL
- Git

---

## How to Run

From inside the `SPOTIFY` directory:

```bash
python -m src.extract
python -m src.transform
python -m src.load


