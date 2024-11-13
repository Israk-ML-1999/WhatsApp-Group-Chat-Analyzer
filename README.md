# WhatsApp-Group-Chat-Analyzer
This app is a Streamlit-based tool for analyzing WhatsApp chat data. It processes uploaded chats to generate statistics, visualizations, and insights into user activity, word frequency, and emoji usage. This interactive tool aids in understanding  and data preprocessing and analysis, making chat insights accessible and visually engaging. 

# Installation
Follow step:

 1. git clone https://github.com/Israk-ML-1999/WhatsApp-Group-Chat-Analyzer.git
 2. pip install -r requirements.txt
 3. streamlit run app.py

# Usage
1. Upload the WhatsApp Chat File: Export the chat from WhatsApp in .txt format and upload it to the analyzer.
2. Choose a User or 'Overall': Select a specific user to analyze their activity, or choose "Overall" for group-level insights.
3. Explore the Results: Use the sidebar to select the analyses you want to view.


# Project Structure
  app.py: Main Streamlit application file.
  preprocess.py: Contains functions for preprocessing the WhatsApp chat data.
  helper.py: Provides helper functions for generating statistics and visualizations.
  requirements.txt: Lists dependencies needed to run the application.   

# Example Analyses
1. Most Active Days and Hours
Displays the days and hours with peak activity in the conversation.

2. Word Cloud
Visual representation of the most frequently used words, helping to capture the common topics discussed.

3. Emoji Analysis
Breakdown of the emojis used, showcasing popular emojis and their counts

# Future Enhancements
    1. Sentiment Analysis: Incorporate sentiment analysis to show positive, negative, and neutral message trends.
    2. Advanced Filtering: Allow users to filter by date ranges or specific keywords.
    3. Additional Visualizations: Include advanced visualizations for deeper insights.
