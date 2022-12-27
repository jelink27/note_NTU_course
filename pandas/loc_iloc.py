import pandas as pd

movie_ratings = [9.0, 8.9, 8.8, 8.7]
movie_titles = ["The Dark Knight", "Schindler's List", "Forrest Gump", "Inception"]
release_years = [2008, 1993, 1994, 2010]
df = pd.DataFrame()
df["rating"] = movie_ratings
df["release_year"] = release_years
df.index = movie_titles
df.loc[["The Dark Knight", "Inception"], ["rating", "release_year"]] #只找前面兩部的rating跟release_year loc寫法為row,column


print(df[df['release_year'] > 2000]) #也適用華麗索引跟廣播 可用來當遮罩

dd = df[df['movie_titles'] == 'The Dark Knight']
print(dd)

print(df.iloc[0:2,0:3])
