import streamlit as st
import pandas as pd
import duckdb
import plotly.express as px

st.image("ph_banner.png", use_column_width=True)
st.title("Product Hunt Analysis (January - April 2024)")

@st.cache_data
def load_data(path: str):
    data = pd.read_csv(path)
    data.rename(columns={"Product Rating Float": "Rating", "Topic 1": "T1", "Topic 2": "T2", "Topic 3": "T3", "Day Rank": "DRank", "Week Rank": "WRank", "Num Topics": "TopicsCount"}, inplace=True)
    return data

df = load_data("./data/ph_jan_april_2024_processed.csv")

columns_required = ['Name', 'Upvotes', 'Reviews', 'Pricing', 'Comments', 'DRank', 'WRank', 'Rating', 'Day', 'TopicsCount', 'T1', 'T2', 'T3']

df = duckdb.sql(f"""SELECT {', '.join(columns_required)} FROM df""").df()

with st.expander("Data Preview"):
    st.dataframe(df)

st.markdown(f"Total Number of Products Launched: {df.shape[0]}")
st.table(df.describe())

#### Upvotes distribution

st.subheader("Upvotes Distribution")

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
    st.subheader("Pricing Models Used")
    pricing_counts = duckdb.sql("SELECT Pricing, COUNT(*) as Count FROM df GROUP BY Pricing").df()
    pricing_pie = px.pie(pricing_counts, values='Count', names='Pricing', width=360, height=400)
    st.plotly_chart(pricing_pie)

##### Launch Days

with launch_days:
    st.subheader("Launch Days Traffic")
    days_counts = duckdb.sql("SELECT Day, COUNT(*) as Count FROM df GROUP BY Day ORDER BY DAY").df()
    days_bar = px.bar(days_counts, x='Day', y='Count', width=400, height=400)
    st.plotly_chart(days_bar)

##### Topics of Products

st.subheader("Most Used Product Topic / Tag")
topic_1_bar, topic_1_pie = st.columns(2)


with topic_1_bar:
    topic_1 = duckdb.sql("SELECT T1 as Topic, COUNT(*) as Count FROM df GROUP BY Topic HAVING Count > 20 ORDER BY Count DESC").df()
    topic_1_bar = px.bar(topic_1, x='Topic', y='Count')
    st.plotly_chart(topic_1_bar, use_container_width=True)

with topic_1_pie:
    topic_1_pie = px.pie(topic_1, values='Count', names='Topic')
    st.plotly_chart(topic_1_pie, use_container_width=True)

st.header("Analysis on Top Products (Under Day Rank #10)")

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
    top_10_drank_bar = px.bar(top_10_list, x='Day', y='Count')
    st.plotly_chart(top_10_drank_bar, use_container_width=True)

with top_10_pie:
    top_5_drank_pie = px.pie(top_10_list, values='Count', names='Day')
    st.plotly_chart(top_5_drank_pie, use_container_width=True)


st.subheader("Reviews received by Top Products")

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


st.subheader("Average Upvotes required to get under #10 Product of the Day")

top_10_upvotes_query = """
SELECT Upvotes, Day
FROM df
WHERE DRank < 11
"""
top_10_upvotes = duckdb.sql(top_10_upvotes_query).df()
average_upvotes = top_10_upvotes.groupby('Day')['Upvotes'].mean().reset_index()
top_10_upvotes_bar = px.bar(average_upvotes, x='Day', y='Upvotes')
st.plotly_chart(top_10_upvotes_bar, use_container_width=True)

best_day = average_upvotes[average_upvotes['Upvotes'] == average_upvotes['Upvotes'].min()]['Day'].values[0]

st.markdown(f'''
Best Day to launch on Product Hunt with higher chances of getting rank under #10 and less competition is **:red[{best_day}]** :calendar:
''')

top_10_topic_1_bar, top_10_topic_1_pie = st.columns(2)

with top_10_topic_1_bar:
    top_10_topic_1 = duckdb.sql("SELECT T1 as Topic, COUNT(*) as Count FROM df WHERE DRank < 4 AND TOPIC IS NOT NULL GROUP BY Topic HAVING Count > 10 ORDER BY Count DESC").df()
    top_10_topic_1_bar = px.bar(top_10_topic_1, x='Topic', y='Count')
    st.plotly_chart(top_10_topic_1_bar, use_container_width=True)

with top_10_topic_1_pie:
    top_10_topic_1_pie = px.pie(top_10_topic_1, values='Count', names='Topic')
    st.plotly_chart(top_10_topic_1_pie, use_container_width=True)