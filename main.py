from bs4 import BeautifulSoup
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request

from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from functools import wraps
import requests

from src.database import MySqlDb
from src import helpers
from src import scraping


scraperApp = Flask(__name__)
db = MySqlDb(scraperApp, "localhost", "root",
             "775477birhan", "coolscraperapp",)


@scraperApp.route('/', methods=["GET", "POST"])
def index():
    form = producInputForm(request.form)
    if request.method == "POST":
        productLink = form.productLink.data
        if helpers.validateLink(productLink):
            productObject = addingProduct(productLink)
            flash("Adding product is successful", "success")
            return redirect(url_for("index"))
        else:
            flash("Please enter a correct URL from etsy.com", "danger")
            return redirect(url_for("index"))
    else:
        return render_template("index.html", form=form, products=listingProducts())


@scraperApp.route('/product/<string:id>')
def productDetail(id):
    product = db.getProduct(id)
    return render_template("product.html", product=product)


def addingProduct(productLink):
    product = scraping.getProductInfo(productLink)
    db.addProduct(product['name'], product['img'], product['price'],
                  product['price_symbol'], product['description'])


def listingProducts():
    products = db.getProducts()
    return products


class producInputForm(Form):
    productLink = StringField("Product Link from Etsy", validators=[
                              validators.DataRequired()])


if __name__ == "__main__":
    scraperApp.run(debug=True)
