from flask import Flask, render_template, request
from models import db, Category, Product
from sqlalchemy import desc
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:hejsan123@localhost/northwind'
db.app = app
db.init_app(app)

@app.route("/")
def index() -> str:
    categories = Category.query.all()
    return render_template('index.html', allCategories=categories)



@app.route("/category/<id>")
def category(id) -> str:
    sortColumn = request.args.get('sortColumn')
    sortOrder = request.args.get('sortOrder')

    if sortColumn == "" or sortColumn == None:
        sortColumn = "ProductName"

    if sortOrder == "" or sortOrder == None:
        sortOrder = "asc"


    products = Product.query.filter_by(CategoryId = id)
    if sortColumn == "ProductName":
        if sortOrder == "desc":
            products = products.order_by(Product.ProductName.desc())
        else:
            products = products.order_by(Product.ProductName)

    if sortColumn == "UnitPrice":
        if sortOrder == "desc":
            products = products.order_by(Product.UnitPrice.desc())
        else:
            products = products.order_by(Product.UnitPrice)


    if sortColumn == "UnitsInStock":
        if sortOrder == "desc":
            products = products.order_by(Product.UnitsInStock.desc())
        else:
            products = products.order_by(Product.UnitsInStock)



    category = Category.query.filter_by(CategoryID = id).first()
    sortDict = {'ProductName': 'asc', 'UnitPrice': 'asc', 'UnitsInStock': 'asc'}
    if sortOrder == "asc":
        sortDict[sortColumn] = 'desc'
    return render_template('category.html', sortColumn=sortColumn, sortDict=sortDict,  products=products, categoryID = id, categoryName = category.CategoryName)

@app.route("/product/<id>")
def product(id) -> str:
    product = Product.query.filter_by(ProductID = id).first()
    return render_template('product.html', product=product)



if __name__  == "__main__":
    app.run(debug=True)
