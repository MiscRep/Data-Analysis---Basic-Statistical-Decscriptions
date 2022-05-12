# Data Analysis - Basic Statistical Decscriptions

import pandas
import numpy
import statistics

ages = [13, 15, 16, 16, 19, 20, 20 ,21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]

# Main Menu
def main_menu():
    global player_choice
    print("+==================================================================+")
    print("+                                                                  +")
    print("+                           Ebony Boykin                           +")
    print("+                             presents                             +")
    print("+                           Data Analysis                          +")
    print("+                   Basic Statistical Descriptions                 +")
    print("+                                                                  +")
    print("+    Choose an option from the menu                                +")
    print("+    1. Mean of Data                                               +")
    print("+    2. Median of Data                                             +")
    print("+    3. Mode of the Data                                           +")
    print("+    4. Midrange of the Data                                       +")
    print("+    5. Variance and Standard Deviation                            +")
    print("+    6. First and Third Quartile of Data                           +")
    print("+                                                                  +")
    print("+==================================================================+")
    
    player_choice = int(input("Please type a number and press [ENTER]\n"))

    if player_choice == 1:
        print("Ah, brave adventurer! Here is the Mean of the Data.\n")
        # Finding the mean of the ages
        mean_age = 1
        print(f"The mean is: {mean_age}")
    elif player_choice == 2:
        print("Wise choice. Here is the median of the data.\n")
        # Finding the Median of the ages
        median_age = statistics.median(ages)
        print(f"The median is :{median_age}")
    elif player_choice == 3:
        # Mode of Data
        print("The data is bimodal\n") ################# Not Complete #################
    elif player_choice == 4:
        print("Weird choice, but okay. The Midrange of the Data is.\n")
        # Finding Midrange of data
        mid_range = (13 + 30)/2
        print(f"The Midrange is: {mid_range}")
    elif player_choice == 5:

        print("You must really like numbers or something. The Variance and Standard Deviation.")
        # Finding Deviation and Variance
        deviation = (13 - 29.9)**2 + (15 - 29.9)**2 + (16 - 29.9)**2 + (16 - 29.9)**2 + (19 - 29.9)**2 + (20 - 29.9)**2 + (20 - 29.9)**2 + (21 - 29.9)**2 + (22 - 29.9)**2 + (22 - 29.9)**2 + (25 - 29.9)**2 + (25 - 29.9)**2 + (25 - 29.9)**2 + (25 - 29.9)**2 + (30 - 29.9)**2 + (33 - 29.9)**2 + (33 - 29.9)**2 + (35 - 29.9)**2 + (35 - 29.9)**2 + (35 - 29.0)**2 + (35 - 29.9)**2 + (36 - 29.9)**2 + (40 - 29.9)**2 + (45 - 29.9)**2 + (46 - 29.9)**2 + (52 - 29.9)**2 + (70 - 29.9)**2
        variance = deviation/27
        print(f"The Variance and Standard Diviation: {variance}")
    else:
        print("Come back anytime for more math stuff. Farewell!\n")
        exit()
    return player_choice

main_menu()

