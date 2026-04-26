import pandas as pd
data = pd.read_csv(r"cleaned_data.csv")
df = pd.DataFrame(data)
#movie vs TV Show analysis
count = df['type'].value_counts()
total = count['Movie']+count['TV Show']

movie_prcnt = ( count['Movie'] / total )*100
show_prcnt = (count['TV Show'] / total)*100
print(f"Movie percent :-{movie_prcnt}")
print(f"Show percent :-{show_prcnt}")

#genre analysis
df['listed_in'] = df['listed_in'].str.split(", ")
listed_type = []

for i in range(len(df)):
    listed_type.extend(df.loc[i,'listed_in'])

listed2_type = []
for val in listed_type :
    if (val != "Movies" and val != "TV Shows"):
        listed2_type.append(val)

#print(listed_type)
genre_data = {"list" : listed2_type }
genre_df = pd.DataFrame(genre_data)
print(genre_df['list'].value_counts())

#country analysis
df['country'] = df['country'].astype(str)
df['country'] = df['country'].str.split(", ")

country_list = []
for i in range(len(df)):
    country_list.extend(df.loc[i,'country'])

country_data = {"countries" : country_list}
country_df = pd.DataFrame(country_data)
print(country_df.value_counts().head(10))

#release year analysis
year_list = []
for i in range (len(df)):
    year_list.append(df.loc[i,'release_year'])

release_year_data = {
    "years"  : year_list
}
release_year_df = pd.DataFrame(release_year_data)
print(release_year_df['years'].value_counts().head(20))

#to check in which year most content was addded to netflix

df['year_added'] = pd.to_datetime(df['date_added'], errors='coerce').dt.year
print(df['year_added'].value_counts())