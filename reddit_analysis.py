import praw
import pandas as pd
import re
from datetime import datetime
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Fetch Reddit Data
# Reddit API credentials
reddit = praw.Reddit(
    client_id="Hq90X0v1cdGyy0R4OxCDsA",
    client_secret="2s5AlUsQ0hIg4pmaNwsrQkPiYEm-OA",
    user_agent="SocialMediaAnalyticsBot/1.0"
)

# Fetch top 100 posts from a subreddit
subreddit = reddit.subreddit("learnpython")
posts = []
for post in subreddit.top(limit=100):
    posts.append({
        "Title": post.title,
        "Score": post.score,
        "Comments": post.num_comments,
        "Created": post.created_utc,
        "URL": post.url
    })

# Save raw data to CSV
df = pd.DataFrame(posts)
df.to_csv("reddit_top_posts.csv", index=False)
print("Raw data saved to 'reddit_top_posts.csv'")

# Step 2: Load and Clean Data
# Load data
df = pd.read_csv("reddit_top_posts.csv")

# Clean post titles
def clean_text(text):
    return re.sub(r"[^a-zA-Z0-9\s]", "", text)

df["Cleaned_Title"] = df["Title"].apply(clean_text)

# Convert timestamps to readable dates
df["Created_Date"] = pd.to_datetime(df["Created"], unit="s")
df = df.drop(columns=["Created"])  # Drop raw timestamp column

# Save cleaned data to CSV
df.to_csv("cleaned_reddit_data.csv", index=False)
print("Cleaned data saved to 'cleaned_reddit_data.csv'")

# Step 3: Perform Sentiment Analysis
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

df["Sentiment"] = df["Cleaned_Title"].apply(get_sentiment)

# Save sentiment analysis results to CSV
df.to_csv("sentiment_analysis.csv", index=False)
print("Sentiment analysis results saved to 'sentiment_analysis.csv'")

# Step 4: Visualize Data
# Sentiment Distribution
sns.countplot(x="Sentiment", data=df)
plt.title("Sentiment Distribution")
plt.savefig("sentiment_distribution.png")
plt.show()

# Engagement by Sentiment
sns.boxplot(x="Sentiment", y="Score", data=df)
plt.title("Engagement by Sentiment")
plt.savefig("engagement_by_sentiment.png")
plt.show()

# Step 5: Save Final Processed Data
df.to_csv("final_reddit_analysis.csv", index=False)
print("Final processed data saved to 'final_reddit_analysis.csv'")
