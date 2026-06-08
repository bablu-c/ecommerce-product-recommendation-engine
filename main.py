from src.data_loader import load_products
from src.personalized import personalized_recommendation
from src.report_generator import generate_report
from src.top_products import get_top_products
from src.category_recommendation import category_recommendation

products = load_products("data/products.csv")


def show_all_products():
    print("\n===== ALL PRODUCTS =====\n")

    for pid, product in products.items():
        print(
            pid,
            product["name"],
            "|",
            product["category"],
            "| Rating:",
            product["rating"]
        )


def show_top_products():
    print("\n===== TOP PRODUCTS =====\n")

    top_products = get_top_products(products)

    for product in top_products:
        print(
            product["name"],
            "| Rating:",
            product["rating"]
        )


def show_category_products():

    category = input(
        "\nEnter Category: "
    )

    recommendations = category_recommendation(
        products,
        category
    )

    print("\nCategory Recommendations\n")

    for product in recommendations:
        print(
            product["name"],
            "| Rating:",
            product["rating"]
        )


def show_personalized_recommendations():

    search_history = [
        "Mobile",
        "Electronics"
    ]

    cart_items = [
        "P107"
    ]

    purchase_items = [
        "P103"
    ]

    recommendations = personalized_recommendation(
        products,
        search_history,
        cart_items,
        purchase_items
    )

    print("\nTop Recommendations\n")

    for pid, score in recommendations:

        print(
            products[pid]["name"],
            "Score:",
            score
        )

    generate_report(
        recommendations,
        products
    )


while True:

    print("\n")
    print("=" * 50)
    print("E-Commerce Product Recommendation Engine")
    print("=" * 50)

    print("1. View All Products")
    print("2. Show Top Products")
    print("3. Category Recommendations")
    print("4. Personalized Recommendations")
    print("5. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        show_all_products()

    elif choice == "2":
        show_top_products()

    elif choice == "3":
        show_category_products()

    elif choice == "4":
        show_personalized_recommendations()

    elif choice == "5":
        print("\nThank You!\n")
        break

    else:
        print("\nInvalid Choice")