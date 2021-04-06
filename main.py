from bs4 import BeautifulSoup
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request

from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from functools import wraps
import requests


scraperApp = Flask(__name__)

if __name__ == "__main__":
    scraperApp.run(debug=True)
