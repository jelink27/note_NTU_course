import pandas as pd
import sqlite3

# Creating a demo.db database in working directory
conn = sqlite3.connect('demo.db')
# Importing a table
movie_ratings = [9.0, 8.9, 8.8, 8.7]
movie_titles = ["The Dark Knight", "Schindler's List", "Forrest Gump", "Inception"]
df = pd.DataFrame()
df["title"] = movie_titles
df["rating"] = movie_ratings
df.to_sql("movies", index=False, con=conn, if_exists='replace')
# Importing data from demo.movies
query_str = """
SELECT *
    FROM movies
    WHERE rating < 9.0;
"""
print(pd.read_sql(query_str, con=conn))
