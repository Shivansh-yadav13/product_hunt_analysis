# Product Hunt Launch Analysis

## Dataset
The dataset is of the products launched on Product Hunt from January - April 2024. This data was scrapped using a python script using selenium. This dataset will help us to analyze the factors that leads to a successful Product Hunt launch.

## Objective

**To analyze what factors or features, listed on Product Hunt, can lead the product to have higher chances of ranking in top 10 products of the day on Product Hunt.**

## Observations

Total Number of Products Launched: **2130**

Average upvotes received: **205**

Maximum upvotes received: **981**

Average reviews received by the Products: **12**

Maximum No. of reviews went upto: **997** 

Average ratings received by the Products: **2.5**

---

### Let's find out the Upvotes required to get Top Day Rank

Here is the distribution of upvotes received by all the products:

![Upvotes Distribution](/images/upvotes_hist.png)

Here are the **Average Upvotes** required to get under **#10, #5, #1 Day Rank**:

![Top Products Average Upvotes](/images/avg_upvotes_top_dayrank.png)

### Let's Figure out the Best Day to Launch

The most crowded days of Product Launches were:

![Traffic on Week Days](/images/launches_days.png)

Most crowded days of the week are usually `Monday` & `Tuesday`.

Let's say we want to get under `#10 Product Of the Day` Day Rank, we need to find out how many upvotes do we need on average for the week days.

![Top 10 Avg Upvotes Each Day](/images/avg_upvotes_each_day_top_10.png)

We can observe that on `Sunday` and `Saturday` we need relatively less number of upvotes to get under `#10 Day Rank`. Therefore, we can conclude that `Sunday` and `Saturday` might be the best days for eaisly ranking top on Product Hunt.

### Let's figure out what Pricing model is good during the launch

Most of the products launched on Product Hunt contain **Free** plan in their pricing.

![Pricing](/images/pricing.png)

Free Plan isn't the best way to grow MRR and many Free users will never convert to paid users. But we can see **Free** Plan is what used by most of the Products on Product Hunt.

### What category of Products are mostly launched

![Topics Used](/images/topics_used.png)

Most of the products launched, are launched under the Topic of `Productivity` as their first topic.

Except `Productivity`, let's see what other categories of products are launched which get under `#10 Day Rank`.

![Topics Used by Top #10](/images/topic_top_10.png)

We can observer the top 5 categories of top products except `Productivity` are:
- Design Tools
- Marketing
- Android
- Artificial Intelligence
- SaaS
