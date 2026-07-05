Netflix Movies and TV Shows Data Analysis Project
Dataset Used : Netflix Movies and TV Shows Dataset downloaded from Kaggle.

Data Cleaning

 Before performing analysis, I cleaned the dataset to handle missing values and ensure better accuracy.

1. Checking Missing Values

I used the isnull() method to identify missing values present in different columns of the dataset.

2. Handling Missing Values

Several columns contained the missing data so i handled them based on the nature of data
-For the columns like columns director, rating, cast and country i replaced the null values using unknown using fillna() method.
-And for null data present in columns like date_added and duration i just dropped them as it could have caused problem in future while performing date analysis.
Exploratory Data Analysis (EDA)
1. Movies vs TV Shows Analysis

My first step was to determine the proportion of Movies vs TV Shows available on Netflix.

Result:
Movies → ~69.7%
TV Shows → ~30.3%

This showed that Netflix's catalog is heavily dominated by movies.

2. Genre Analysis

I analyzed the listed_in column to identify the most common genres available on Netflix.

This step was challenging because:

multiple genres were stored in a single row
I had to split the genres
remove unnecessary labels
then rank the top genres

Top genres included:

International Movies
Dramas
Comedies
International TV Shows
Documentaries

3. Country-wise Analysis

I identified the top countries producing Netflix content.

Top countries included:

United States
India
United Kingdom
Canada

4. Release Year Analysis

I analyzed which years had the highest number of content released.

This helped identify periods where content production was highest.

5. Netflix Content Addition Analysis

I extracted the year from the date_added column and analyzed which years Netflix added the most content to its platform.

This helped understand Netflix’s expansion period.

Challenges Faced :
Handling missing values properly
Splitting multiple genres stored in a single column
Flattening nested lists
Removing unnecessary values
Working with date formats
