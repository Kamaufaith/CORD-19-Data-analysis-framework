import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("~/Downloads/cord19_cleaned.csv", low_memory=False)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['publish_year'] = df['publish_time'].dt.year
    df['journal'] = df['journal'].fillna("Unknown")
    return df

df = load_data()

# --- Page Layout ---
st.title("COVID-19 Research Analysis Dashboard 🧬")
st.markdown("""
This Streamlit app provides an interactive analysis of COVID-19 research papers from the **CORD-19 dataset**.
Use the controls on the sidebar to explore publication trends, journals, and frequent terms.
""")

# --- Sidebar Controls ---
st.sidebar.header("Filters & Settings")

year_range = st.sidebar.slider(
    "Select Publication Year Range:",
    int(df['publish_year'].min()),
    int(df['publish_year'].max()),
    (int(df['publish_year'].min()), int(df['publish_year'].max()))
)

# Filter dataset by year
filtered_df = df[(df['publish_year'] >= year_range[0]) & (df['publish_year'] <= year_range[1])]

# --- Show Data Sample ---
st.subheader("📊 Sample of the Data")
st.dataframe(filtered_df.head(10))

# --- Publications Over Time ---
st.subheader("📈 Publications Over Time")
papers_by_year = filtered_df['publish_year'].value_counts().sort_index()

fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.lineplot(x=papers_by_year.index, y=papers_by_year.values, ax=ax1, marker='o')
ax1.set_title("Number of Publications Over Time")
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Papers")
st.pyplot(fig1)

# --- Top Journals ---
st.subheader("🏛️ Top Journals Publishing COVID-19 Research")
top_n = st.sidebar.slider("Select number of top journals:", 5, 20, 10)
top_journals = filtered_df['journal'].value_counts().head(top_n)

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_journals.values, y=top_journals.index, palette="coolwarm", ax=ax2)
ax2.set_title(f"Top {top_n} Journals")
ax2.set_xlabel("Number of Papers")
ax2.set_ylabel("Journal")
st.pyplot(fig2)

# --- Word Cloud of Titles ---
st.subheader("☁️ Most Frequent Words in Paper Titles")
text = " ".join(filtered_df['title'].astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis("off")
st.pyplot(fig3)

# --- Source Distribution ---
st.subheader("📚 Distribution of Paper Counts by Source")
if 'source_x' in filtered_df.columns:
    top_sources = filtered_df['source_x'].value_counts().head(10)
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_sources.values, y=top_sources.index, palette='viridis', ax=ax4)
    ax4.set_title("Top 10 Sources by Paper Count")
    ax4.set_xlabel("Number of Papers")
    ax4.set_ylabel("Source")
    st.pyplot(fig4)
else:
    st.warning("No 'source_x' column found in dataset.")