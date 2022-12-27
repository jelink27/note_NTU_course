import pandas as pd

#sort by index

movie_ratings = [9.0, 8.9, 8.8, 8.7]
movie_titles = ["The Dark Knight", "Schindler's List", "Forrest Gump", "Inception"]
release_years = [2008, 1993, 1994, 2010]
df = pd.DataFrame()
df["title"] = movie_titles
df["rating"] = movie_ratings
df["release_year"] = release_years
df.sort_index() # default: ascending
df.sort_index(ascending=False)
print(df)

#sort by value

df.sort_values("title")
df.sort_values("release_year")
df.sort_values("release_year", ascending=False)
