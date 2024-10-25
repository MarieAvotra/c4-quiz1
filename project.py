#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:24:35 2024

@author: sitraka
"""

print("PROJECT 1")
import pandas as pd

df= pd.read_csv("movie_dataset.csv")
print(df)

# 5 first rows
print("HEAD") 
print(df.head())

print("DESCRIBE")
print(df.describe())

print("INFO")
print(df.info())

print("MISSING")
#Summarise the number of missing values in each column
a=df.isnull(). sum()
print(a)

"""
The revenue (Millions) and Metascore's columns have missing value
Revenue:128(rows)
Metascore:64(rows)

print("DROPPED DUPLICATES")
#Remove duplicate if it exist 
df.drop_duplicates(inplace=True)
dropped_duplicates=df.reset_index(drop=True)
print(dropped_duplicates)
c=dropped_duplicates.shape
print(c)
print(dropped_duplicates.describe())
"""
#Prevent bias: 
print("RENAME")
#rename columns name which have spaces
df.columns=df.columns. str.replace(' ','_')
print(df.columns)

# 1)The highest rated movie in the dataset
"""
It concerns the Rating's columns 
(so we don't have to drop the Dataset here for 
 avoiding to delete the max value of Rating's columns')
"""
#Find the maximum rating in the dataset
print("MAX")
max_voting=df['Rating']. max()
print(max_voting)

#Find the row corresponding to the max rating
print("HIGHEST RATE") 
highest_rated_movie=df[df['Rating']== max_voting]
print(highest_rated_movie)


# 2)The average revenue of all movies in the dataset 
"""
It concerns the Revenue_(Millions)'s columns 
so we are going to fill the missing value in the 
Metascore's rows then drop the the missing value in 
the Revenue_(Millions)'s columns
"""

#Filling the missing value in the Metascore's rows 
#with his average value 
print("FILL")
df['Metascore']=df['Metascore'].fillna(df['Metascore'].mean(), axis=0)
print(df.describe())

#drop the the missing value in 
#the Revenue_(Millions)'s columns
"""
print("DROP")
#Drop the rows which have missing values
df.dropna(inplace= True)
dropped_rows=df.reset_index(drop=True)
print(dropped_rows)
b=dropped_rows.shape
print(b)
print(dropped_rows.describe())
"""
print("DROP")
#Drop the rows which have missing values
dropped_rows=df.dropna(axis=0)
print(dropped_rows)
b=dropped_rows.shape
print(b)
print(dropped_rows.describe())

#The average revenue of all movies in the dataset 
print("REVENUES AVERAGE")
mean_revenue=dropped_rows['Revenue_(Millions)'].mean()
print(mean_revenue)


# 3)Revenue_(Millions)'s average from 2015-2017
print("FROM 2015 TO 2017")
filtered_df=dropped_rows[(dropped_rows['Year']>=2015) & (dropped_rows['Year']<=2017)]
mean_revenue1=filtered_df['Revenue_(Millions)'].mean()
print(mean_revenue1)


# 4)Released movie in 2016
print("MOVIES IN 2016")
movie_in_2016=df[df['Year']==2016]
c=movie_in_2016.shape[0]
print(c)


# 5)Directed movies by Christopher Nolan
print("Christopher Nolan")
movie_by_Christopher=df[df['Director']=="Christopher Nolan"]
d=movie_by_Christopher.shape[0]
print(d)

# 6)Movies which have a rating of at least 8.0
print("The 8.0 RATING")
specifed_rating_movies=df[df['Rating']>=8.0]
e=specifed_rating_movies.shape[0]
print(e)

# 7) The median rating of movies directed by Christopher Nolan
print("Christopher Nolan's median rating of movie")
cn_median_rating=df[df['Director']=="Christopher Nolan"]['Rating'].median()
print(cn_median_rating)


# 8)The year with the highest average rating
print("Year with the highest average rating")
#Group the Dataset by year and calculate the mean rating for each year
average_rating_by_year= df.groupby('Year')['Rating'].mean()
#Find the year with the highest average rating
specific_year= average_rating_by_year.idxmax()
print(specific_year)


# 9) The % increase in number of movies made between 2006 and 2016
print("PERCENTAGE")
#Find and selecte the movie between 2006 and 2016
filtered_movies_one= df[df['Year']==2006]

filtered_movies_two= df[df['Year']==2016]

#The number of movies (number of rows) for each year
movies_by_year_one= filtered_movies_one.shape[0]
movies_by_year_two= filtered_movies_two.shape[0]
percentage = (movies_by_year_two - movies_by_year_one)*100/movies_by_year_one
print(f"percentage increse between 2006 and 2016 = {percentage}")
    
# 10)The most common actor in all the movies
print("COMMON ACTOR")
#Since there are many values in (i,j), we have to separate one by one
#and flat the rows 
all_actors = df['Actors'].str.split(', ').explode()

#Count the occurrences of each actor
actor_counts = all_actors.value_counts()

#Get the most common actor
most_common_actor = actor_counts.idxmax()
print(most_common_actor)

# 11)The unique genres are there in the dataset
print("Unique genre")
#Identify the genres individually
all_genre = df['Genre'].str.split(',').explode()
print(all_genre)

#Count the occurrences of each genre
number_unique_genre = all_genre.unique().shape[0]
print(number_unique_genre)





