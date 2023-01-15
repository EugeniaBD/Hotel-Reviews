"""
This module is responsible for processing the data.  Each function in this module will take a list of reviews,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of reviews (where each review is a list of data values) as a parameter.
- Process the list of reviews appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of reviews that have been loaded.
- Retrieve the reviews for a hotel where the hotel name is specified by the user.
- Retrieve the reviews for the dates specified by the user.
- Retrieve all the reviews grouped by the reviewer’s nationality.
- Retrieve a summary of all the reviews. This should include the following information for each date in ascending order:
    - the total number of negative reviews on that date
    - the total number of positive reviews on that date
    - the average rating on that date
"""

import tui

def get_total_reviews(reviews):
    return len(reviews)

def get_hotel_reviews(reviews):
    hotel_name = tui.get_input("Enter the hotel name: ")
    return [review for review in reviews if review[1] == hotel_name]

def get_date_reviews(reviews):
    start_date = tui.get_input("Enter the start date (YYYY-MM-DD): ")
    end_date = tui.get_input("Enter the end date (YYYY-MM-DD): ")
    return [review for review in reviews if start_date <= review[3] <= end_date]

def get_reviews_by_nationality(reviews):
    nationality_reviews = {}
    for review in reviews:
        nationality = review[4]
        if nationality not in nationality_reviews:
            nationality_reviews[nationality] = []
        nationality_reviews[nationality].append(review)
    return nationality_reviews

def get_review_summary(reviews):
    review_summary = {}
    for review in reviews:
        date = review[3]
        if date not in review_summary:
            review_summary[date] = {'Negative_Review': 0, 'Positive_Review': 0, 'avg_rating': 0, 'Total_Reviews_By_Reviewer': 0}
        if review[2] != 'No Negative':
            review_summary[date]['neg_reviews'] += 1
        elif review[2] != 'No Positive':
            review_summary[date]['pos_reviews'] += 1
        review_summary[date]['avg_rating'] += review[5]
        review_summary[date]['total_reviews'] += 1
    for date in review_summary:
        review_summary[date]['avg_rating'] = review_summary[date]['avg_rating']/review_summary[date]['total_reviews']
    return review_summary