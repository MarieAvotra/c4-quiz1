# Movie Dataset Analysis Project

## Description
This project provides a comprehensive analysis of a movie dataset using Python and pandas. The dataset includes various attributes such as ratings, revenue, release year, director, and actors. The analysis covers tasks like handling missing values, calculating summary statistics, identifying trends, and finding specific movie details based on various criteria.

## Project Structure

### Files
- **movie_dataset.csv**: The main dataset used for analysis.
- **project.py**: The Python script that performs data cleaning, data analysis, and summary generation.

### Main Features
1. **Data Loading and Initial Exploration**:
   - Load the dataset and display the first five rows, dataset summary, and info on missing values.

2. **Data Cleaning**:
   - Rename columns to remove spaces.
   - Handle missing values in "Metascore" and "Revenue (Millions)" columns.
   - Remove duplicate rows to avoid biased analysis.

3. **Analyses Conducted**:
   - **Highest Rated Movie**: Identify the movie with the maximum rating.
   - **Average Revenue**: Calculate the overall average revenue of movies in the dataset.
   - **Revenue (2015-2017)**: Average revenue of movies released between 2015 and 2017.
   - **Movies Released in 2016**: Count the number of movies released in 2016.
   - **Movies Directed by Christopher Nolan**: Count the movies directed by Christopher Nolan.
   - **Movies with High Ratings**: Count movies with a rating of at least 8.0.
   - **Christopher Nolan’s Median Rating**: Find the median rating of movies directed by Christopher Nolan.
   - **Year with Highest Average Rating**: Identify the year with the highest average rating.
   - **Percentage Increase in Movies (2006-2016)**: Calculate the percentage increase in movies made from 2006 to 2016.
   - **Most Common Actor**: Identify the actor who appears most frequently across movies.
   - **Unique Genres**: Find the unique genres present in the dataset.

## How to Run
1. Ensure Python 3 and pandas are installed.
2. Place `movie_dataset.csv` in the same directory as `project.py`.
3. Run the script using:
   ```bash
   python3 project.py
   ```

## Output
The script will output insights and statistics related to the dataset, including data summaries, counts, and specific details as outlined in the analysis sections.

## Requirements
- Python 3
- pandas

## Author
Avotra
