"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display a pie chart showing the total number of positive and negative reviews for a specified hotel.
- Display the number of reviews per the nationality of a reviewer. This should by ordered by the number of reviews, highest first, and should show the top 15 + “Other” nationalities.
- Display a suitable animated visualisation to show how the number of positive reviews, negative reviews and the average rating change over time.

Each function should visualise the data using Matplotlib.
"""
import tui
import matplotlib.pyplot as plt

def visualise_hotel_reviews(reviews):
    hotel_name = tui.get_input("Enter the hotel name: ")
    pos_reviews = [review for review in reviews if review[1] == hotel_name and review[2] == 'positive']
    neg_reviews = [review for review in reviews if review[1] == hotel_name and review[2] == 'negative']

    review_counts = [len(pos_reviews), len(neg_reviews)]
    labels = ['Positive', 'Negative']

    plt.pie(review_counts, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

def visualise_reviews_by_nationality(reviews):
    nationality_reviews = {}
    for review in reviews:
        nationality = review[4]
        if nationality not in nationality_reviews:
            nationality_reviews[nationality] = 0
        nationality_reviews[nationality] += 1

    nationality_reviews = {k: v for k, v in sorted(nationality_reviews.items(), key=lambda item: item[1], reverse=True)}
    top_nationalities = list(nationality_reviews.keys())[:15]
    other_reviews = sum([v for k, v in nationality_reviews.items() if k not in top_nationalities])

    top_nationalities.append('Other')
    review_counts = [v for k, v in nationality_reviews.items() if k in top_nationalities[:-1]]
    review_counts.append(other_reviews)

    plt.barh(top_nationalities, review_counts)
    plt.xlabel('Number of reviews')
    plt.ylabel('Nationality')
    plt.show()

def visualise_review_summary(review_summary):
    dates = list(review_summary.keys())
    neg_reviews = [review_summary[date]['neg_reviews'] for date in dates]
    pos_reviews = [review_summary[date]['pos_reviews'] for date in dates]
    avg_rating = [review_summary[date]['avg_rating'] for date in dates]

    fig, ax = plt.subplots()
    ax.plot(dates, neg_reviews, label='Negative Reviews')
    ax.plot(dates, pos_reviews, label='Positive Reviews')
    ax.plot(dates, avg_rating, label='Average Rating')
    ax.legend()
    plt.xlabel('Dates')
    plt.ylabel('Reviews')
    plt.show()
