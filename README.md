<<<<<<< HEAD
# Reddit Sentiment Analysis

This project analyzes Reddit data to classify posts into Positive, Neutral, or Negative sentiments. It also explores engagement trends to identify which types of posts perform better in terms of upvotes and comments.

## Features
- Fetches Reddit posts using the PRAW library.
- Performs sentiment analysis with TextBlob to classify posts.
- Visualizes:
  - Sentiment distribution (Positive, Neutral, Negative).
  - Engagement (post scores) by sentiment.
- Cleans and preprocesses data for meaningful insights.

## File Structure
- Reddit-Sentiment-Analysis 
- data reddit_top_posts.csv
- Raw Reddit data cleaned_reddit_data.csv
- Cleaned data sentiment_analysis.csv
- Sentiment analysis results final_reddit_analysis.csv 
- Fully processed dataset /visualizations sentiment_distribution.png 
- Sentiment distribution plot engagement_by_sentiment.png 
- Engagement trends by sentiment reddit_analysis.py 
- Main Python script README.md 
- Project documentation


## Tools and Libraries
- **Programming Language**: Python
- **Libraries**:
  - `pandas`: For data manipulation.
  - `matplotlib` and `seaborn`: For visualizations.
  - `textblob`: For sentiment analysis.
  - `praw`: For accessing Reddit API.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/your-Thiru0407/Reddit-Sentiment-Analysis.git

2.  Navigate to the project directory:
bash
Copy code
cd Reddit-Sentiment-Analysis

3. pip install praw pandas matplotlib seaborn textblob

4. Run the main script:
bash
Copy code
python reddit_analysis.py

## Results
Sentiment Distribution:
A plot showing the proportion of Positive, Neutral, and Negative posts.
Engagement Trends:
A boxplot showing how engagement (upvotes and comments) varies by sentiment.

## Insights
Sentiment Analysis: The subreddit contains a balanced distribution of Positive, Neutral, and Negative posts.
Engagement Trends: Negative posts tend to attract higher engagement, indicating that controversial or critical content gets more attention.

## Acknowledgments
Data was fetched using Reddit's API via the PRAW library.
Sentiment analysis powered by TextBlob.

## Future Work
Add word clouds for frequently used terms in Positive, Neutral, and Negative posts.
Explore temporal trends in sentiment and engagement.
Implement advanced machine learning techniques for sentiment analysis.



=======
# Reddit-Sentiment-Analysis
A Python project that analyzes Reddit data for sentiment analysis (Positive, Neutral, Negative) and engagement insights. It includes data cleaning, sentiment classification, and visualizations to explore subreddit activity.
>>>>>>> 2d04687b9abd19c45c4bbabb2643d9c2c567efcd
