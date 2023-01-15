"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""



# Task 11: Import required modules and create an empty list named 'reviews_data'.
# This will be used to store the data read from the source data file.

from tui import * 
#imports all from the Tui module

import process
import visual


reviews_data =[]



def run():
    # Task 12: Call the function welcome of the module 'tui'.

    # This will display our welcome message when the program is executed.

    welcome()

    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    # - Load the data. Each line in the file should represent a review in the list 'reviews_data'.
    # You should appropriately handle the case where the file cannot be found or loaded.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many reviews have
    # been loaded and that the data loading operation has completed.
    

    
    progress ()


import numpy as np
import tui

try:
    
    df = np.read_csv('reviews.csv')

    reviews_data = []

    for index, row in df.iterrows():
        reviews_data.append(row['hotel_reviews'])

    tui.display_message(f'{len(reviews_data)} reviews have been loaded.')

except FileNotFoundError:
    
    tui.display_error('File not found. Please check the file path and try again.')
except:
    tui.display_error('An error occurred while loading the file. Please check the file format and try again.')



    
    while True:
        # Task 14: Using the appropriate function in the module 'tui', display the main menu
        # Assign the value returned from calling the function to a suitable local variable
    
        main_menu()
      


        # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, do the following:
        # - Use the appropriate function in the module 'tui' to display a sub-menu of options for processing the data
        # (menu variant 1).
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve reviews by hotel name then
        #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process
        #       has started.
        #       - Use the appropriate function in the module 'process' to retrieve the review and then appropriately
        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve reviews by review dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the reviews retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve the reviews
        #       - Use the appropriate function in the module 'tui' to display the retrieved reviews.
        #       - Use the appropriate function in the module 'tui' to indicate that the reviews retrieval
        #       process has completed.
        #
        #   - If the user selected the option to group reviews by nationality then
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has started.
        #       - Use the appropriate function in the module 'process' to group the reviews
        #       - Use the appropriate function in the module 'tui' to display the groupings.
        #       - If required, you may add a suitable function to the module 'tui' to display the groupings
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has completed.
        #
        #   - If the user selected the option to summarise the reviews then
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has started.
        #       - Use the appropriate function in the module 'process' to summarise the reviews.
        #       - Add a suitable function to the module 'tui' to display the summary
        #       - Use your function in the module 'tui' to display the summary
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has completed.
       
    def process_data(data, tui):
    # Use the appropriate function in the module tui to display a message to indicate that the data processing
    # operation has started.
        tui.progress("Data processing has started.")

    # Use the appropriate function in the module 'tui' to display a sub-menu of options for processing the data
    # (menu variant 1).
        option = tui.sub_menu(1)

        if option == 1:
        # Use the appropriate function in the module 'tui' to indicate that the review retrieval process has started.
            tui.progress("Retrieving reviews by hotel name...")
            # Use the appropriate function in the module 'process' to retrieve the review and then appropriately
            # display it.
            hotel_name = tui.get_hotel_name()
            reviews = process.get_reviews_by_hotel(data, hotel_name)
            tui.display_reviews(reviews)
            # Use the appropriate function in the module 'tui' to indicate that the review retrieval process has completed.
            tui.progress("Retrieval of reviews by hotel name completed.")
        
        elif option == 2:
            # Use the appropriate function in the module 'tui' to indicate that the reviews retrieval process has started.
            tui.progress("Retrieving reviews by review dates...")
            # Use the appropriate function in the module 'process' to retrieve the reviews
            review_dates = tui.get_review_dates()
            reviews = process.get_reviews_by_dates(data, review_dates)
            # Use the appropriate function in the module 'tui' to display the retrieved reviews.
            tui.display_reviews(reviews)
            # Use the appropriate






        # Task 21: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual' to display the visual
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.
        if tui.selected_option == 2:
            visual.visualise_hotel_reviews()
            tui.progress()
        
        # Task 25: Check if the user selected the option for exporting reviews.  If so, then do the following:
        # - Use the appropriate function in the module 'tui' to retrieve what reviews are to be exported.
        # - Check what option has been selected
        #
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has started.
        # - Export the reviews (see below)
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has completed.
        #
        # To export the reviews, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create suitable classes with appropriate methods.
        # You should use these to write the reviews (either all or only those for a specific country/region) to a JSON file.
        if tui.selected_option == 3:
                visual.visualise_hotel_reviews()
                visual.progress()

        # Task 26: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        while tui.selected_option == 4:
            break

        # Task 27: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        if tui.selected_option not in valid_options:
            tui.display_error("Invalid option selected")

    


        if __name__ == "__main__":
            run()
