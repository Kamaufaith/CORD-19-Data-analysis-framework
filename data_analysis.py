import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud
import streamlit as st

df_clean = pd.read_csv("~/Downloads/cord19_cleaned.csv")
print("Cleaned dataset loaded successfully!")
print(df_clean.shape)
print(df_clean.head())
# Count the number of papers per year
papers_by_year = df_clean['publish_year'].value_counts().sort_index()
print(papers_by_year)
#Identify top journals publishing COVID-19 research
top_journals = df_clean['journal'].value_counts().head(10)
print("Top 10 Journals:\n", top_journals)
# Find most frequent words in titles
from collections import Counter
import re
# Combine all titles into one string
all_titles = ' '.join(df_clean['title'].dropna().astype(str))
#Split and clean words
words = re.findall(r'\b[a-zA-Z]{3,}\b', all_titles.lower())
#Count most common words
common_words = Counter(words).most_common(20)
print("Most frequent words in titles:")
for word, count in common_words:
    print(f"{word}: {count}")

# Plot a number of publications over time
plt.figure(figsize=(10, 5))
papers_by_year.plot(kind='bar')
plt.title("Number of Publications Over Time")
plt.xlabel("Publication Year")
plt.ylabel("Number of Papers")
plt.tight_layout()
save_path = os.path.expanduser("~/Downloads/publications_over_time.png")
plt.savefig(save_path)
print("Plot saved to Downloads as 'publications_over_time.png'")
#Bar chart of top publishing journals
plt.figure(figsize=(10,6))
sns.barplot(x=top_journals.values, y=top_journals.index, palette='viridis')
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.tight_layout()
save_path = os.path.expanduser("~/Downloads/top_journals_bar_chart.png")
plt.savefig(save_path)
print("Bar saved to Downloads as 'top_journals_bar_chart.png'")
#Generate a word cloud of paper titles
wordcloud = WordCloud(width=1000, height=600, background_color='white').generate(all_titles)
plt.figure(figsize=(10,6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Paper Titles")
save_path = os.path.expanduser("~/Downloads/wordcloud_of_paper_titles.png")
plt.savefig(save_path)
print("Word Cloud saved to Downloads as 'wordcloud_of_paper_titles.png'")
#Distribution of paper counts by source
if 'source_x' in df_clean.columns:
    top_sources = df_clean['source_x'].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_sources.values, y=top_sources.index, palette='coolwarm')
    plt.title("Top 10 Sources by Paper Count")
    plt.xlabel("Number of Papers")
    plt.ylabel("Source")

    save_path_3 = os.path.expanduser("~/Downloads/top_sources_distribution.png")
    plt.savefig(save_path)
    print("Bar chart saved to Downloads as 'top_sources_distribution.png'")

    plt.close()
else:
    print("Column 'source_x' not found in dataset, skipping source distribution plot.")