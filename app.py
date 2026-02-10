import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

@st.cache_data(show_spinner=False)
def load_data(path: str):
    usecols = ["publish_time", "journal", "title", "source_x"]
    dtype = {"journal": "string", "title": "string", "source_x": "string"}
    df = pd.read_csv(path, usecols=lambda c: c in usecols, dtype=dtype)

    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["publish_year"] = df["publish_time"].dt.year.astype("Int16")
    df["journal"] = df["journal"].fillna("Unknown")
    df["title"] = df["title"].fillna("")
    return df

path = os.path.expanduser("~/Downloads/cord19_cleaned.csv")
df = load_data(path)

st.title("COVID-19 Research Analysis Dashboard 🧬")

st.sidebar.header("Filters & Settings")

year_min = int(df["publish_year"].dropna().min())
year_max = int(df["publish_year"].dropna().max())
year_range = st.sidebar.slider("Select Publication Year Range:", year_min, year_max, (year_min, year_max))

top_n = st.sidebar.slider("Select number of top journals:", 5, 20, 10)

make_wc = st.sidebar.checkbox("Generate wordcloud (can be heavy)", value=False)
max_wc_rows = st.sidebar.slider("Wordcloud: max rows", 5_000, 50_000, 10_000, step=5_000)

run = st.sidebar.button("Run analysis")
if not run:
    st.stop()

filtered_df = df[(df["publish_year"] >= year_range[0]) & (df["publish_year"] <= year_range[1])]

st.subheader("📊 Sample of the Data")
st.caption(f"Filtered rows: {len(filtered_df):,}")
st.dataframe(filtered_df.head(200))

st.subheader("📈 Publications Over Time")
papers_by_year = filtered_df["publish_year"].value_counts().sort_index()

fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.lineplot(x=papers_by_year.index, y=papers_by_year.values, ax=ax1, marker="o")
st.pyplot(fig1)

st.subheader("🏛️ Top Journals Publishing COVID-19 Research")
top_journals = filtered_df["journal"].value_counts().head(top_n)

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax2)
st.pyplot(fig2)

st.subheader("☁️ Most Frequent Words in Paper Titles")
if make_wc:
    wc_df = filtered_df.head(max_wc_rows)
    titles = wc_df["title"].astype(str).str.slice(0, 200)
    text = " ".join(titles.tolist())
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    ax3.imshow(wordcloud, interpolation="bilinear")
    ax3.axis("off")
    st.pyplot(fig3)
else:
    st.info("Enable the checkbox in the sidebar to generate the wordcloud.")

st.subheader("📚 Distribution of Paper Counts by Source")
if "source_x" in filtered_df.columns:
    top_sources = filtered_df["source_x"].value_counts().head(10)
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_sources.values, y=top_sources.index, ax=ax4)
    st.pyplot(fig4)
