# import pandas as pd
# from textblob import TextBlob
# import matplotlib.pyplot as plt
# import seaborn as sns
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

# # Load the cleaned CSV file
# input_file_path = 'combined_top_comments.csv'
# df = pd.read_csv(input_file_path, header=None, names=['comment'])

# # Perform sentiment analysis on each comment
# def analyze_sentiment(comment):
#     analysis = TextBlob(str(comment))
#     return analysis.sentiment.polarity

# df['Sentiment'] = df['comment'].apply(analyze_sentiment)

# # Plot the distribution of sentiment scores
# plt.figure(figsize=(10, 6))
# sns.histplot(df['Sentiment'], bins=30, kde=True, color='skyblue')
# plt.title('Distribuția Scorurilor ')
# plt.xlabel('Scor de sentiment')
# plt.ylabel('Frecventa')
# plt.grid(True)
# plt.savefig("Distribution.png")

# # Plot a pie chart to show the percentage of positive, negative, and neutral comments
# positive_comments = df[df['Sentiment'] > 0].shape[0]
# negative_comments = df[df['Sentiment'] < 0].shape[0]
# neutral_comments = df[df['Sentiment'] == 0].shape[0]
# labels = ['Positive', 'Negative', 'Neutral']
# sizes = [positive_comments, negative_comments, neutral_comments]
# colors = ['lightgreen', 'lightcoral', 'lightskyblue']

# plt.figure(figsize=(8, 6))
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
# plt.title('Sentiment Analysis: Piechart')
# plt.axis('equal')
# plt.savefig("pieChart.png")




# # Load the cleaned comments from the CSV file
# cleaned_comments = pd.read_csv('combined_top_comments.csv', header=None)[0]

# # Combine all comments into a single string
# all_comments_text = ' '.join(cleaned_comments)

# # Generate a word cloud
# wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_comments_text)

# # Display the word cloud using matplotlib
# plt.figure(figsize=(10, 6))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.savefig("wordCloud.png")


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Ensure you have downloaded the VADER lexicon
# nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Load the cleaned CSV file
input_file_path = 'combined_top_comments.csv'
df = pd.read_csv(input_file_path, header=None, names=['comment'])

# Perform sentiment analysis on each comment using VADER
def analyze_sentiment(comment):
    sentiment_scores = sid.polarity_scores(str(comment))
    return sentiment_scores['compound']

df['Sentiment'] = df['comment'].apply(analyze_sentiment)

# Plot the distribution of sentiment scores
plt.figure(figsize=(10, 6))
sns.histplot(df['Sentiment'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Sentiment Scores')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
# plt.savefig("Distribution.png")

# Plot a pie chart to show the percentage of positive, negative, and neutral comments
positive_comments = df[df['Sentiment'] > 0].shape[0]
negative_comments = df[df['Sentiment'] < 0].shape[0]
neutral_comments = df[df['Sentiment'] == 0].shape[0]
labels = ['Positive', 'Negative', 'Neutral']
sizes = [positive_comments, negative_comments, neutral_comments]
colors = ['lightgreen', 'lightcoral', 'lightskyblue']

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Sentiment Analysis: Piechart')
plt.axis('equal')
plt.savefig("pieChart.png")

# Load the cleaned comments from the CSV file
cleaned_comments = pd.read_csv('combined_top_comments.csv', header=None)[0]

# Combine all comments into a single string
all_comments_text = ' '.join(cleaned_comments)

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_comments_text)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig("wordCloud.png")
