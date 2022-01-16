from flask import Flask, render_template, request
from models import db, Category, Product
from sqlalchemy import desc
import datetime
import random
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:hejsan123@localhost/northwind'
db.app = app
db.init_app(app)

class NewsListItem:
    header = ""
    description = ""

@app.route("/articles")
def articles()->str:
    art1 = NewsListItem()
    art1.header = "Artikel 1"
    art1.description = "Bla bla bla"
    art2 = NewsListItem()
    art2.header = "Artikel 2"
    art2.description = "Bla bla bla"
    art3 = NewsListItem()
    art3.header = "Artikel 3"
    art3.description = "Bla bla bla"
    
    lista = [ art1,art2,art3 ]
    return render_template('articles.html', allArticles = lista)



@app.route("/")
def index() -> str:
    categories = Category.query.all()
    return render_template('index.html', allCategories=categories)

@app.route("/mypage")
def mypagefunction() -> str:
    return render_template('mypage.html', name = "Kalle", age=27)


@app.route("/RandomNumber")
def randomnumber():
    tal = random.randint(0,300000)
    tid = datetime.datetime.now().strftime("%H:%M")
    return render_template('randomNumber.html', randomNumber=tal, tid=tid)


@app.route("/players")
def players():
    playerList = ["Kalle Persson", "Lisa Larsson", "Mats Matssson"]
    return render_template('players.html', playerList = playerList)

@app.route("/currentday")
def currentDay() -> str:
    weekDays = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]
    weekday = datetime.datetime.now().weekday()
    weekDayInSwedish = weekDays[weekday]
    return render_template('currentday.html', weekDayInSwedish = weekDayInSwedish)


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
