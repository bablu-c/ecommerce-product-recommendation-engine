from fastapi import FastAPI
from src.data_loader import load_products
from src.personalized import personalized_recommendation
from src.top_products import get_top_products
from src.category_recommendation import category_recommendation

app = FastAPI(
    title="E-Commerce Product Recommendation Engine",
    description="DSA-based Recommendation API",
    version="1.0"
)

products = load_products("data/products.csv")


@app.get("/")
def home():
    return {
        "message": "E-Commerce Recommendation Engine Running"
    }


@app.get("/products")
def products_list():
    return list(products.values())


@app.get("/top-products")
def top_products():
    return get_top_products(products)


@app.get("/category/{category}")
def category_products(category: str):
    return category_recommendation(
        products,
        category
    )


@app.get("/recommend")
def recommend():

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

    result = []

    for pid, score in recommendations:

        result.append({
            "product_id": pid,
            "product_name": products[pid]["name"],
            "score": score
        })

    return result