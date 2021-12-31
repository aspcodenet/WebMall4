from flask import Flask, render_template
from models import db, Category, Product
 
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
    products = Product.query.filter_by(CategoryId = id)
    category = Category.query.filter_by(CategoryID = id).first()
    return render_template('category.html', products=products, categoryName = category.CategoryName)



if __name__  == "__main__":
    app.run(debug=True)
