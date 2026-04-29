import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Python Programs\Projects\ntflxprjct\cleaned_data.csv")
df = pd.DataFrame(data)

#movie vs TV Show analysis
count = df['type'].value_counts()

plt.pie(count.values, labels = count.index, autopct = '%1.1f%%',colors = ['darkblue','lightblue'])
plt.title('Movies Vs TV Shows')
#plt.savefig("visual_reports/Movies Vs TV Shows.png", dpi = 300 , bbox_inches = 'tight')

#Rating analysis
type_count = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(type_count.values, labels = type_count.index,autopct = '%1.1f%%', colors = ['orange','red'])
plt.title("rating composition")
plt.tight_layout()
#plt.savefig("visual_reports/Rating composition.png")


#Movie Duration Analysis
movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace("min"," ").astype(int)

plt.figure(figsize= (8,6))
plt.hist(movie_df['duration_int'], bins = 30, color = 'purple', edgecolor = 'black')
plt.xlabel("Duration of movies")
plt.ylabel("No. of movies")
plt.title('Movie Durations Analysis')
plt.tight_layout()
#plt.savefig('visual_reports/Movie Durations Analysis.png')

#Movies distribution over years
release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize = (10,8))
plt.bar(release_counts.index, release_counts.values, color = 'red')
plt.xlabel('Release Years')
plt.ylabel('No. of movies')
plt.title("Movies released yearwise")
plt.tight_layout()
#plt.savefig("visual_reports/Movies released yearwise.png")

#Top 10 countries in producing shows till 2023
country_counts = df['country'].value_counts().head(10)
plt.figure(figsize = (10,8))
plt.barh(country_counts.index, country_counts.values, color = 'red')
plt.ylabel('Name of Country')
plt.xlabel('No. of Movies Released by Country')
plt.title('Top 10 Countries in content')

plt.tight_layout()
#plt.savefig('visual_reports/Top 10 countries in content.png')

#Movies and TV shows released over year.
content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)
fig , ax = plt.subplots(1,2, figsize = (12,5))

ax[0].plot(content_by_year.index , content_by_year['Movie'])
ax[0].set_xlabel('Year')
ax[0].set_ylabel('No. of movies')
ax[0].set_title('No, of movies released a year')

ax[1].plot(content_by_year.index , content_by_year['TV Show'])
ax[1].set_xlabel('Year')
ax[1].set_ylabel('No. of TV Shows')
ax[1].set_title('No, of TV Shows released a year')

plt.suptitle('Movies and TV shows released over year.')
plt.tight_layout()
#plt.savefig('visual_reports/Movies and TV shows released over year.png')
plt.show()  