# CS 410 Fall 2023 Final Project

Author: Pratyusha Pogaru

Project: Chrome extension for sentiment analysis of recipe reviews

# Overview

  This project is a Chrome extension for sentiment analysis on recipe blog comments. Sometimes, not all the comments on recipe blogs have a star rating, or the ability to rank comments from most to least liked (or vice versa). This makes it difficult to tell from a quick glance, if the recipe has (overall) more positive or negative reviews. Additionally, users must often scroll all the way to the bottom of the blog to find the comments, and then read through them to determine the sentiment. This takes time. This project aims to provide a summary of the reviews’ sentiment for a particular recipe. The idea is to give the user a quick glance, to be able to tell if a recipe is overall more liked or disliked. 

# Usage

This software can be used by downloading the folder titled “project_code” from GitHub. The reviews.csv from this Kaggle link <https://www.kaggle.com/code/gemmin/sentiment-analysis/input?select=reviews.csv> must also be downloaded and added to the same folder. 

Open your machine's terminal and navigate into the project directory (into “project_code”). Run the following scripts:

1) python scrape_me.py <URL of a Sally’s Baking Addiction recipe, eg  https://sallysbakingaddiction.com/strawberry-cake/ >

2) python naive_bayes.py

3) Open Chrome and go to chrome://extensions/. Click on the “Load unpacked” button on the top left, and upload the whole folder “project_code”. Ensure a new Extension card is created (titled Sentiment Analysis Extension), reload it if needed. Once it is active, click the extensions icon (puzzle piece) at the top of the browser to view the new extension. Pin it using the pin icon. A green icon should now be visible at the top of the browser. Navigate to the same recipe link (reload it if the webpage is already open), and click the green extension icon. A popup dialog box of the average predicted sentiments of the comments of the current recipe should now be visible.