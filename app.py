from flask import Flask, render_template

app = Flask(__name__)

products = [

{
"id":1,
"name":"SmartPhone",
"price":20000,
"old_price":24000,
"image":"smartphone.jpg",
"category":"Electronics",
"badge":"Best Seller",
"description":"High performance smartphone with powerful processor, excellent camera, and long lasting battery."
},

{
"id":2,
"name":"Laptop",
"price":55000,
"old_price":62000,
"image":"laptop.jpg",
"category":"Computers",
"badge":"",
"description":"Lightweight laptop with fast processor, SSD storage and long battery life."
},

{
"id":3,
"name":"AirPods",
"price":12000,
"old_price":15000,
"image":"airpods.jpg",
"category":"Accessories",
"badge":"Hot Deal",
"description":"Wireless earbuds with crystal clear sound quality and noise cancellation."
},

{
"id":4,
"name":"Tablet",
"price":25000,
"old_price":29000,
"image":"tablet.jpg",
"category":"Electronics",
"badge":"",
"description":"Portable tablet with large display, smooth performance and long battery life."
}

]

@app.route("/")
def home():
    return render_template("index.html", products=products)


@app.route("/product/<int:id>")
def product(id):

    selected_product = None

    for p in products:
        if p["id"] == id:
            selected_product = p
            break

    return render_template("product.html", product=selected_product)


if __name__ == "__main__":
    app.run()
