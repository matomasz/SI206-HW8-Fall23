# Your name:
# Your student id:
# Your email:
# List who you have worked with on this homework:

import matplotlib.pyplot as plt
import os
import sqlite3
import unittest


def load_restaurant_data(db):
    """
    This function accepts the filename of the database as a parameter, and returns a nested dictionary. Each outer 
    key of the dictionary is the name of each restaurant in the database, and each inner key is a dictionary, where the 
    key:value pairs should be the food_type, building_number, star_rating, and num_reviews for the restaurant.
    """
    pass


def plot_best_star_ratings_by_food_type(db):
    """
    This function accepts the filename of the database as a parameter and returns a dictionary. The keys should be 
    the restaurant food_types and the values should be the corresponding highest star_rating of the restaurants of 
    that food_type.
    """
    pass


def find_restaurants_in_building(building_number, db):
    '''
    This function accepts the building_number and the filename of the database as parameters and returns a list of 
    restaurant names. You need to find all the restaurant names which are in the specific building. The restaurants 
    should be sorted by their star_rating from highest to lowest
    '''
    pass

# EXTRA CREDIT


def get_highest_weighted_average_ratings(db):  # Do this through DB as well
    """
    This function returns a list of two tuples. The first tuple contains the highest-rated restaurant food_type 
    and its weighted average of restaurants, and the second tuple contains the highest rated 
    building_number and its weighted average of restaurants.

    This function should also plot two barcharts in one figure. 
    For the first bar chart, the y-axis will be different food_type of each restaurant. The x-axis will be the 
    weighted average star_rating for the restaurants of each food_type. The average values should be rounded to 
    two decimal places. Sort the y-axis in descending order from top-to-bottom by rating. 

    For the second bar chart, the y-axis will be different building_numbers. The x-axis will be the weighted 
    average star_rating for the restaurants in each building. The average values should also be rounded to two 
    decimal places, and the y-axis should be sorted in descending order by rating. 

    """
    pass


def main():  # Try calling your functions here
    pass


class TestHW8(unittest.TestCase):
    def setUp(self):
        self.rest_dict = {
            'food_type': 'Cafe',
            'building_number': 1101,
            'star_rating': 3.8,
            'num_ratings': 543
        }
        self.best_of_food_type = {
            'Bubble Tea Shop': 5.0,
            'Cafe': 4.8,
            'Korean Restaurant': 4.5,
            'Pizzeria': 4.4,
            'Japanese Restaurant': 4.4,
            'Mexican Restaurant': 4.3,
            'Asian Cuisine': 4.3,
            'Bar': 4.2,
            'Juice Shop': 4.2,
            'Thai Restaurant': 4.1,
            'Deli': 4.0,
            'Mediterranean Restaurant': 4.0,
            'Sandwich Shop': 3.9,
            'Cookie Shop': 3.8
        }
        self.w_avg_food_type = [
            ('Bubble Tea Shop', 4.82),
            ('Korean Restaurant', 4.5),
            ('Japanese Restaurant', 4.4),
            ('Mexican Restaurant', 4.22),
            ('Juice Shop', 4.2),
            ('Asian Cuisine', 4.15),
            ('Thai Restaurant', 4.1),
            ('Bar', 4.1),
            ('Mediterranean Restaurant', 4.0),
            ('Deli', 4.0),
            ('Cafe', 3.88),
            ('Sandwich Shop', 3.84),
            ('Cookie Shop', 3.8),
            ('Pizzeria', 3.67)
        ]
        self.w_avg_building_num = [
            (1220, 4.97),
            (1335, 4.8),
            (1327, 4.5),
            (1313, 4.5),
            (1205, 4.5),
            (1107, 4.4),
            (1321, 4.4),
            (1140, 4.16),
            (1300, 4.13),
            (1204, 4.1),
            (1208, 4.1),
            (1201, 4.0),
            (1235, 4.0),
            (1329, 4.0),
            (1207, 3.9),
            (1229, 3.8),
            (1101, 3.8),
            (1214, 3.66),
            (1315, 3.0)
        ]
        self.highest_weighted_ratings = [
            self.w_avg_food_type[0], self.w_avg_building_num[0]]

    def test_load_restaurant_data(self):
        rest_data = load_restaurant_data('South_U_Restaurants.db')
        self.assertIsInstance(rest_data, dict)
        self.assertEqual(
            rest_data['M-36 Coffee Roasters Cafe'], self.rest_dict)
        self.assertEqual(len(rest_data), 25)

    def test_plot_best_star_ratings_by_food_type(self):
        food_type_data = plot_best_star_ratings_by_food_type(
            'South_U_Restaurants.db')
        self.assertIsInstance(food_type_data, dict)
        for key in food_type_data:
            self.assertAlmostEqual(
                food_type_data[key], self.best_of_food_type[key], 1)
        self.assertEqual(len(food_type_data), 14)

    def test_find_restaurants_in_building(self):
        restaurant_list = find_restaurants_in_building(
            1140, 'South_U_Restaurants.db')
        self.assertIsInstance(restaurant_list, list)
        self.assertEqual(len(restaurant_list), 3)
        self.assertEqual(restaurant_list[0], 'BTB Burrito')

    def test_get_highest_weighted_average_ratings(self):
        food_type_ratings = get_highest_weighted_average_ratings(
            'South_U_Restaurants.db')
        self.assertEqual(food_type_ratings, self.highest_weighted_ratings)


if __name__ == '__main__':
    main()
    unittest.main(verbosity=2)
