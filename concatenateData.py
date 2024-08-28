import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


# nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


def calculate_relevance_score(text):

    if isinstance(text, str):
        # Calculate sentiment score using VADER
        sentiment_score = sid.polarity_scores(text)['compound']
        # Normalize sentiment score to range [0, 1]
        normalized_score = (sentiment_score + 1) / 2  
        return normalized_score
    else:
      
        return 0  

def sort_and_select_top_comments(df):
    # Sort comments by relevance score
    df['relevance_score'] = df['comment'].apply(calculate_relevance_score)
    df_sorted = df.sort_values(by='relevance_score', ascending=False)
 
    top_comments = df_sorted.head(12500)
    return top_comments[['Date', 'User', 'comment']]

def sort_and_select_top_comments(df):
    # Randomly select 12,500 comments
    top_comments = df.sample(n=12500, random_state=42)  
    return top_comments[['Date', 'User', 'comment']]


cleaned_file_paths = ['cleanedGooglePixelComments_2020_V2.csv','cleanedGooglePixelComments_2021_V2.csv','cleanedGooglePixelComments_2022_V2.csv','cleanedGooglePixelComments_2023_V2.csv']


top_comments_list = []


for cleaned_file_path in cleaned_file_paths:
    try:
       
        df_cleaned = pd.read_csv(cleaned_file_path, sep=';', encoding="latin1")

       
        top_comments = sort_and_select_top_comments(df_cleaned)

        top_comments_list.append(top_comments)
    
    except FileNotFoundError:
        print(f"File not found: {cleaned_file_path}")


df_combined_top_comments = pd.concat(top_comments_list)

output_combined_top_file = 'combined_top_comments.csv'
df_combined_top_comments.to_csv(output_combined_top_file, index=False, sep=";")
num_of_rows = df_combined_top_comments.shape[0]
print("New data set saved as:", output_combined_top_file)
print("Number of rows of the new data set:", num_of_rows)
