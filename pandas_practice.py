import pandas as pd 

movie_ratings = [9.0, 8.9, 8.8, 8.7]
movie_titles = ["The Dark Knight", "Schindler's List", "Forrest Gump", "Inception"]

#create Dataframe

data = pd.DataFrame()
data['movie_titles'] = movie_titles
data['movie_ratings'] = movie_ratings

print(data.index)
print(data['movie_titles'])
print(data['movie_ratings'])
print(data.columns)
print(type(data['movie_titles']))



#index

odds_index = pd.Index([1,3,5,7,9]) #odd
primes_index = pd.Index([2,3,5,7]) #primes

print(odds_index & primes_index) #交集 odd and primes
print(odds_index | primes_index) #連集 odd or primes
print(odds_index ^ primes_index) #XOR 兩個集合差異的數
