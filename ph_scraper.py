from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import date
import pandas as pd
import numpy as np

ph_data = pd.DataFrame()

driver = webdriver.Edge()

sub_folder = 'april'
start_date = 26
end_date = 30
month = 4

for k in range(start_date, (end_date+1)):
  driver.get(f"https://www.producthunt.com/leaderboard/daily/2024/{month}/{k}/all")
  time.sleep(4)

  page_df = pd.DataFrame()

  i = 1
  product_el = driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/div/div[2]/div[{i}]')

  while product_el:

    ad_slot = product_el.get_attribute('data-test')

    if "ad" in ad_slot:
      print(ad_slot)
      i = i + 1
      product_el = driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/div/div[2]/div[{i}]')
      continue

    # product_el.click()
    driver.execute_script("arguments[0].click();", product_el)

    time.sleep(8)

    '''
      Scraping Tags
    '''
    topic_1 = np.nan
    try:
      topic_1_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/div[3]/div/a[1]/div/div/span')
      topic_1 = topic_1_el.text
    except:
      try:
        topic_1_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/a[1]/div/div/span')
        topic_1 = topic_1_el.text
      except:
        pass

    topic_2 = np.nan
    try:
      topic_2_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/div[3]/div/a[2]/div/div/span')
      topic_2 = topic_2_el.text
    except:
      try:
        topic_2_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/a[2]/div/div/span')
        topic_2 = topic_2_el.text
      except:
        pass

    topic_3 = np.nan
    try:
      topic_3_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/div[3]/div/a[3]/div/div/span')
      topic_3 = topic_3_el.text
    except:
      try:
        topic_3_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/a[3]/div/div/span')
        topic_3 = topic_3_el.text
      except:
        pass

    '''
      Scraping Name
    '''
    name = np.nan
    try:
      name_el = driver.find_element(By.CLASS_NAME, 'styles_title__x5KUY')
      name = name_el.text
    except:
      pass
    
    '''
      Scraping Description
    '''
    desc = np.nan
    try:
      desc_el = driver.find_element(By.CLASS_NAME, 'styles_tagline__svEiR')
      desc = desc_el.text
    except:
      pass
    
    '''
      Scraping Pricing Option
    '''
    pricing = np.nan
    try:
      pricing_el = driver.find_element(By.CSS_SELECTOR, '[data-test="pricing-type"]')
      pricing = pricing_el.text
    except:
      pass

    '''
      Scraping Link of the product
    '''
    link = np.nan
    try:
      link_el = driver.find_element(By.CSS_SELECTOR, '[data-test="embed-btn"]')
      link = link_el.get_attribute('href')
    except:
      try:
        link_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[4]/div')
        link = link_el.text
      except:
        pass

    '''
      Scraping upvotes
    '''
    upvotes = 0
    try:
      # 1st element
      upvotes_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[4]/div[3]/div[4]/div[1]/div[2]')
      upvotes = int(upvotes_el.text)
    except:
      try:
        # rest
        upvotes_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[4]/div[2]/div[4]/div[1]/div[2]')
        upvotes = int(upvotes_el.text)
      except:
        try:
          # on Edge
          upvotes_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[4]/div[2]/div[4]/div[1]/div[2]')
          upvotes = int(upvotes_el.text)
        except:
          pass


    '''
      Scraping Number of Reviews
    '''

    reviews = 0

    try:
      # For 1st element
      reviews_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[4]/div[3]/div[2]/div/div[1]/div/div[1]/a[1]')
      reviews = int(reviews_el.text)
    except:
      try:
        # rest of the elements
        reviews_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[4]/div[2]/div[2]/div/div[1]/div/div[1]/a[1]')
        reviews = int(reviews_el.text)
      except:
        # on Edge
        try:
          reviews_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[4]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]')
          reviews = int(reviews_el.text)
        except:
          pass
    
    
    '''
      Scraping Product Ratings
    '''
    rating = np.nan

    if reviews > 0:
      try:
        rating_el = driver.find_element(By.PARTIAL_LINK_TEXT, '/5 ★')
        rating = rating_el.text
      except:
        try:
          rating_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[4]/div[2]/div[3]/a[4]')
          rating = rating_el.text
        except:
          pass


    
    '''
      Scraping Number of comments
    '''
    comments = 0
    try:
      comments_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[4]/div[3]/div[4]/div[3]/div[2]')
      comments = int(comments_el.text)
    except:
      try:
        comments_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[4]/div[2]/div[4]/div[3]/div[2]')
        comments = int(comments_el.text)
      except:
        try:
          comments_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[4]/div[2]/div[4]/div[3]/div[2]')
          comments = int(comments_el.text)
        except:
          pass
    
    '''
      Scraping Day Rank
    '''
    day_rank = np.nan
    try:
      # 1st element
      day_rank_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[4]/div[3]/div[4]/div[5]/div[2]')
      day_rank = day_rank_el.text
    except:
      try:
        # rest
        day_rank_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[4]/div[2]/div[4]/div[5]/div[2]')
        day_rank = day_rank_el.text
      except:
        try:
          day_rank_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[4]/div[2]/div[4]/div[5]/div[2]')
          day_rank = day_rank_el.text
        except:
          pass
    
    '''
      Scraping Week Rank
    '''
    week_rank = np.nan
    try:
      # 1st element
      week_rank_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[4]/div[3]/div[4]/div[7]/div[2]')
      week_rank = week_rank_el.text
    except:
      try:
        # rest
        week_rank_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div[2]/div[4]/div[2]/div[4]/div[7]/div[2]')
        week_rank = week_rank_el.text
      except:
        try:
          week_rank_el = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[4]/div[2]/div[4]/div[7]/div[2]')
          week_rank = week_rank_el.text
        except:
          pass

    try:
      close_btn = driver.find_element(By.CLASS_NAME, 'styles_close__gzHdp')
      close_btn.click()
    except:
      try:
        close_btn = driver.find_element(By.CSS_SELECTOR, '[data-test="modal"]')
        close_btn.click()
      except:
        driver.refresh()
    

    launch_date = date(2024, month, k)
    new_row = pd.DataFrame([{
      'Date': launch_date,
      'Name': name,
      'Description': desc,
      'Topic 1': topic_1,
      'Topic 2': topic_2,
      'Topic 3': topic_3,
      'URL': link,
      'Upvotes': upvotes,
      'Pricing': pricing,
      'Reviews': reviews,
      'Product Rating': rating,
      'Comments': comments,
      'Day Rank': day_rank,
      'Week Rank': week_rank
    }])
    page_df = pd.concat([page_df, new_row])
    print(new_row)
    
    i = i + 1
    try:
      product_el = driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/div/div[2]/div[{i}]')
    except:
      break
    time.sleep(4)
  
  ph_data = pd.concat([ph_data, page_df])

ph_data.to_csv(f"./raw_data/{sub_folder}/{start_date}_to_{end_date}_{sub_folder}_2024.csv")
driver.close()