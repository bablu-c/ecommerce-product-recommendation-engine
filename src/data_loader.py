import csv

def load_products(file_path):

    products = {}

    with open(file_path, newline='', encoding='utf-8') as file:

        reader = csv.DictReader(file)

        for row in reader:

            products[row["product_id"]] = row

    return products


def load_users(file_path):

    users = {}

    with open(file_path, newline='', encoding='utf-8') as file:

        reader = csv.DictReader(file)

        for row in reader:

            users[row["user_id"]] = row

    return users