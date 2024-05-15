# Product Hunt Launch Analysis

![Banner](/images/ph_banner.png)

## Dataset
The dataset is of the products launched on Product Hunt from January - April 2024. This data was scrapped using a python script using selenium. This dataset will help us to analyze the factors that leads to a successful Product Hunt launch.

## Top Features

1. **Upvotes**: Number of upvotes received by the product. These are the total number of upvotes recieved by the product till the date of when the data was scrapped (the data was scrapped in first week of may).

2. **Day Rank**: The day rank recieved by the product on the day it was launhced.

3. **Topic (T1)**: The topic/category under which the product was launched. There are a total of 3 topic options on product hunt. Topic 1 is the first, usually the primary topic of the product.

4. **Date**: The date on which the product was launched, this date helped us to find out the day of the week of the launch.

5. **Pricing**: This feature specifies the pricing option of the product. There are total 3 options that can be used, "Free", "Free Options" and "Payment Required".

    - **Free**: The product is either entirely free or the product has a Free plan.

    - **Free Options**: The product is not free but has x days of free trail or x amount of free usage.

    - **Payment Required**: The product only has paid plans.


## Objective

**To analyze what factors or features, listed on Product Hunt, can lead the product to have higher chances of ranking in top 10 products of the day on Product Hunt.**

## Observations

Total Number of Products Launched: **2130**

Average upvotes received: **205**

Maximum upvotes received: **981**

![Upvotes Distribution](/images/upvotes_hist.png)

Average reviews received by the Products: **12**

Maximum No. of reviews went upto: **997** 

**Maximum products did not received any reviews**
![Reviews Distribution](/images/reviews_dist.png)

**Distribution of reviews (astleast 1 review)**
![Reviews Distribution](/images/reviews_dist_10.png)


Average ratings received by the Products: **2.5**

![Reviews Distribution](/images/rating_dist.png)

---

### Let's find out the Upvotes required to get Top Day Rank

Here is the distribution of upvotes received by all the products:

![Upvotes Distribution](/images/upvotes_hist.png)

Here are the **Average Upvotes** required to get under **#10, #5, #1 Day Rank**:

![Top Products Average Upvotes](/images/avg_upvotes_top_dayrank.png)

### Let's Figure out the Best Day to Launch

The best day to launch will be a day where we usually have less traffic/competiotion, means not a lot of products are being launched and the average upvotes required to get under #10 Day rank is relatively less.

The most crowded days of Product Launches were:

![Traffic on Week Days](/images/launches_days.png)

Most crowded days of the week are usually `Monday` & `Tuesday`.

Let's say we want to get under `#10 Product Of the Day` Day Rank, we need to find out how many upvotes do we need on average for the week days.

![Top 10 Avg Upvotes Each Day](/images/avg_upvotes_each_day_top_10.png)

We can observe that on `Sunday` and `Saturday` we need relatively less number of upvotes to get under `#10 Day Rank`. Therefore, we can conclude that `Sunday` and `Saturday` might be the best days for eaisly ranking top on Product Hunt.

### Let's figure out what Pricing model is used the most

Most of the products launched on Product Hunt contain **Free** or **Free Options** plan in their pricing.

![Pricing](/images/pricing.png)

Free Plan isn't the best way to grow MRR and many Free users will never convert to paid users. But we can see **Free Options** Plan is what used by most of the Products on Product Hunt.

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

## Summary

- Launching on weekends, particularly Sunday and Saturday, appears to be advantageous due to lower competition and potentially fewer upvotes required to achieve a top day rank.
- The "Free Options" pricing model is prevalent among launched products, suggesting a strategy to attract users with limited financial commitment.
- The "Productivity" category dominates the launch topics, followed by other specialized areas like Design Tools, Marketing, Android, Artificial Intelligence, and SaaS. This suggests a strong interest in productivity-enhancing tools among Product Hunt users.

This analysis provides actionable insights for product creators looking to optimize their launch strategy on Product Hunt. By understanding the dynamics of upvotes, day ranks, launch days, and pricing models, creators can better position their products for success.

### [Checkout the Excel Report](https://1drv.ms/x/c/42733ca0d53e0690/EfvKx7cxeFdMuV30mbcxrpsB_yc0E7_JvPT6SqcdnHhSwA?e=FcTh1i&nav=MTVfe0RDRUM1Nzk1LTNCNTctNEQ0Qy05NEEyLTgwMjkxQzUwNkY2Mn0) 
