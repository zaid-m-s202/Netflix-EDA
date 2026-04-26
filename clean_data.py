import pandas as pd
data = pd.read_csv(r"netflix_titles.csv")
df = pd.DataFrame(data)
df.info()
#print(df.columns)
print(df.isnull().sum())
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")

df = df.dropna(subset = ['date_added']) 
df['rating'] = df['rating'].fillna("Unknown")
df = df.dropna(subset = ['duration'])

print(df.isnull().sum())

df.to_csv('cleaned_data.csv',index = False)
