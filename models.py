from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model):
    __tablename__= "Categories"
    CategoryID = db.Column(db.Integer, primary_key=True)
    CategoryName = db.Column(db.String(15), unique=False, nullable=False)
    Description = db.Column(db.String(255), unique=False, nullable=False)
    Products = db.relationship('Product', backref='Category', lazy=True)

class Product(db.Model):
    __tablename__= "Products"
    ProductID = db.Column(db.Integer, primary_key=True)
    ProductName = db.Column(db.String(40), unique=False, nullable=False)
    SupplierID = db.Column(db.Integer, unique=False, nullable=False)
    CategoryId = db.Column(db.Integer, db.ForeignKey('Categories.CategoryID'), nullable=False)
    QuantityPerUnit = db.Column(db.String(20), unique=False, nullable=False)
    UnitPrice = db.Column(db.Float, unique=False, nullable=False)
    UnitsInStock = db.Column(db.Integer, unique=False, nullable=False)
    UnitsOnOrder = db.Column(db.Integer, unique=False, nullable=False)
    ReorderLevel = db.Column(db.Integer, unique=False, nullable=False)
    Discontinued = db.Column(db.Boolean, unique=False, nullable=False)

