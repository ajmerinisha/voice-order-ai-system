import json
import os

DATABASE_FILE = "database/orders.json"


# CREATE DATABASE FILE
def initialize_database():

    if not os.path.exists(DATABASE_FILE):

        with open(DATABASE_FILE, "w") as f:

            json.dump([], f)


# READ ALL ORDERS
def get_all_orders():

    initialize_database()

    with open(DATABASE_FILE, "r") as f:

        orders = json.load(f)

    return orders


# SAVE NEW ORDER
def save_order(order_data):

    orders = get_all_orders()

    orders.append(order_data)

    with open(DATABASE_FILE, "w") as f:

        json.dump(orders, f, indent=4)

    return True


# GET LAST ORDER
def get_last_order():

    orders = get_all_orders()

    if len(orders) == 0:

        return None

    return orders[-1]


# CLEAR ALL ORDERS
def clear_orders():

    with open(DATABASE_FILE, "w") as f:

        json.dump([], f)

    return True