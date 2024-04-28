import streamlit as st
import pandas as pd
import duckdb
import plotly.figure_factory as ff
import plotly.express as px


st.title("Product Hunt Analysis (January 2024)")

@st.cache_data
def load_data(path: str):
    data = pd.read_csv(path)
    data.rename(columns={"Product Rating Float": "Rating", "Topic 1": "T1", "Topic 2": "T2", "Topic 3": "T3", "Day Rank": "DRank", "Week Rank": "WRank", "Num Topics": "TopicsCount"}, inplace=True)
    return data

df = load_data("./data/ph_jan_24.csv")

columns_required = ['Name', 'Upvotes', 'Reviews', 'Pricing', 'Comments', 'DRank', 'WRank', 'Rating', 'Day', 'TopicsCount', 'T1', 'T2', 'T3']

df = duckdb.sql(f"""SELECT {', '.join(columns_required)} FROM df""").df()

with st.expander("Data Preview"):
    st.dataframe(df)

st.text("Total Number of Products Launched: 504")

#### Upvotes distribution

st.header("Upvotes Distribution")

upvotes = duckdb.sql("SELECT Upvotes FROM df WHERE Upvotes > 0").df()

fig2 = px.histogram(
    upvotes,
    x='Upvotes',
    marginal="box",
)
st.plotly_chart(fig2, use_container_width=True)


pricing_models, launch_days = st.columns(2)


##### Pricing Models


with pricing_models:
    st.header("Pricing Models")
    pricing_counts = duckdb.sql("SELECT Pricing, COUNT(*) as Count FROM df GROUP BY Pricing").df()
    pricing_pie = px.pie(pricing_counts, values='Count', names='Pricing', width=360, height=400)
    st.plotly_chart(pricing_pie)

##### Launch Days

with launch_days:
    st.header("Launch Days")
    days_counts = duckdb.sql("SELECT Day, COUNT(*) as Count FROM df GROUP BY Day ORDER BY DAY").df()
    days_bar = px.bar(days_counts, x=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], y='Count', width=400, height=400)
    st.plotly_chart(days_bar)

##### Topics of Products

st.header("Most Used Product Topic / Tag")
topic_1 = duckdb.sql("SELECT T1 as Topic, COUNT(*) as Count FROM df GROUP BY Topic HAVING Count > 5 ORDER BY Count DESC").df()
topic_1_bar = px.bar(topic_1, x='Topic', y='Count')
st.plotly_chart(topic_1_bar, use_container_width=True)

st.header("Top Products Launch Day (Under Day Rank #10)")
top_10_bar, top_10_pie = st.columns(2)

top_10_query = """
SELECT Day, COUNT(*) as Count
FROM df
WHERE DRank < 11
GROUP BY Day
ORDER BY Day
"""
top_10_list = duckdb.sql(top_10_query).df()


with top_10_bar:
    top_10_drank_bar = px.bar(top_10_list, x=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], y='Count')
    st.plotly_chart(top_10_drank_bar, use_container_width=True)

with top_10_pie:
    top_5_drank_pie = px.pie(top_10_list, values='Count', names=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
    st.plotly_chart(top_5_drank_pie, use_container_width=True)


st.header("Reviews received by Top Products")

top_10_review_query = """
SELECT ANY_VALUE(DRank) as Day_Rank, Reviews
FROM df
WHERE DRank < 11
GROUP BY Reviews
ORDER BY Reviews
"""
top_10_review = duckdb.sql(top_10_review_query).df()
top_10_review_scatter = px.scatter(top_10_review, x='Day_Rank', y='Reviews', size='Reviews', color='Day_Rank', size_max=80)

st.plotly_chart(top_10_review_scatter, use_container_width=True)


st.header("Average Upvotes required to get under #10 Product of the Day")

top_10_upvotes_query = """
SELECT Upvotes, Day
FROM df
WHERE DRank < 11
"""
top_10_upvotes = duckdb.sql(top_10_upvotes_query).df()
average_upvotes = top_10_upvotes.groupby('Day')['Upvotes'].mean().reset_index()
top_10_upvotes_bar = px.bar(average_upvotes, x=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], y='Upvotes')
st.plotly_chart(top_10_upvotes_bar, use_container_width=True)

st.header("More data and Analysis Coming Soon!")