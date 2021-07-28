from flask import Blueprint, render_template
# defining this file as a blueprint simply means
# it has a bunch of routes inside of it
# by using blueprint we can have 
# routes defined in multiple files

views = Blueprint('views', __name__)

@views.route('/')
def index():
  return render_template('bmi.html')