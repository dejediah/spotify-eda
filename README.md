# Spotify Listening Analytics

## Overview

What can 8+ years of personal Spotify listening data reveal about how my
listening behavior and musical taste evolved over time?

This project analyzes my Spotify listening history from 2018–2026 to
explore changes in listening volume, artist discovery, artist retention,
and listening concentration. The project combines Python, SQLite, SQL,
and Power BI to build an end-to-end analytics workflow from raw listening
records to interactive visualizations.

## Key Findings

- **41.4% artist retention:** 41.4% of artists discovered became repeat
  artists in subsequent years, suggesting that a substantial portion of
  new discoveries became part of my longer-term listening ecosystem.
- **41% increase in listening:** Annual listening increased from 244 hours
  in 2019 to 344 hours in 2025, while average listening-event duration
  remained close to 3 minutes.
- **Broad listening profile:** My Top 5 artists accounted for less than
  32% of annual listening in most years, with the remaining listening
  distributed across a much wider artist pool.
- **Changing discovery behavior:** Artist discovery rate declined from
  82.1% in 2019 to 40.9% in 2025, while the overall number of artists
  listened to continued to grow.

## Questions

This project explores several questions:

1. How has my listening activity changed over time?
2. Has increased listening been driven by frequency or longer sessions?
3. How concentrated is my listening around my favorite artists?
4. How frequently do newly discovered artists become repeat listens?
5. Has my musical breadth changed as my listening history accumulated?
6. Which artists and songs defined different periods of my listening?

## Methodology

### Data Pipeline

Spotify Listening History
↓
Python data cleaning
↓
SQLite database
↓
SQL aggregation and analysis
↓
Exploratory analysis in Python
↓
Power BI dashboard

### Tools

- **Python** — data cleaning, transformation, and exploratory analysis
- **Pandas** — data manipulation and aggregation
- **SQLite** — structured storage and querying
- **SQL** — analytical queries and aggregations
- **Power BI** — interactive visualization and dashboarding
- **Jupyter Notebook** — exploratory analysis

## Analysis

### Listening Activity

[powerbi screenshot to be added]

Analysis of total listening hours, active listening days, and individual
play duration across each year.

### Artist Discovery & Retention

[table screenshot to be added]

Analysis of new versus returning artists and the proportion of discovered
artists that became recurring parts of my listening history.

### Listening Concentration

[table screenshot to be added]

Comparison of Top 5 artist listening against the rest of the artist
ecosystem to measure how concentrated or distributed listening was.

### Artist & Song Evolution

[table screenshot to be added]

Exploration of the artists and songs that shaped each period of the
dataset.

## Power BI Dashboard

[dashboard screenshots to be added]

The Power BI dashboard presents the main findings through interactive
visualizations, allowing listening behavior to be explored across years,
artists, and other dimensions.
