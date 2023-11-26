import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from selenium.common.exceptions import NoSuchElementException


# Create a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open the website you want to scrape
driver.get("https://sallysbakingaddiction.com/my-favorite-cornbread/")

time.sleep(5)

# Find the element that contains the comments
comments_element = driver.find_element(By.CLASS_NAME, "comment-list")

# Extract the text of the comments and ratings
comments_and_ratings = []
for comment_element in comments_element.find_elements(By.CLASS_NAME, "comment-content"):
    comment = comment_element.find_element(By.TAG_NAME, 'p').text
    
    # Check if the comment has a rating
    try:
        rating_element = comment_element.find_element(By.CLASS_NAME, "tasty-recipes-ratings")
        rating = len(rating_element.find_elements(By.CSS_SELECTOR, '.tasty-recipes-rating-solid'))
    except NoSuchElementException:
        rating = None  # No rating element found

    comments_and_ratings.append({'Comment': comment, 'Rating': rating})
    print("Comment:", comment)
    print("Rating:", rating)
    print("=====")

# Close the browser window
driver.quit()

time.sleep(5)

# Save comments and ratings to a CSV file
csv_file_path = 'comments_and_ratings.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['Comment', 'Rating']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Write the header
    csv_writer.writeheader()
    
    # Write the comments and ratings
    for entry in comments_and_ratings:
        print("entry")
        print(entry)
        csv_writer.writerow(entry)

time.sleep(5)

