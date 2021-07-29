from flask import Blueprint, render_template, request
# defining this file as a blueprint simply means
# it has a bunch of routes inside of it
# by using blueprint we can have 
# routes defined in multiple files

views = Blueprint('views', __name__)

# @views.route('/')
# def index():
  # return render_template('bmi.html')

# @views.route('/', methods=['GET', 'POST'])
# @views.route('/')
# def index():

  # if request.method == 'POST' and ('height-feet' in request.form) and ('height-inches' in request.form) and ('weight' in request.form):
  #   heightFeet = int(request.form.get('height-feet'))
  #   heightInches = int(request.form.get('height-inches'))

  #   height = (round(heightInches / 12, 2)) + heightFeet

  #   weight = int(request.form.get('weight'))

  #   return render_template('bmi.html', height=height, weight=weight)
  # return render_template('bmi.html')

@views.route('/', methods=['GET', 'POST'])
# def bmi_calc():
def index():
  if request.method == 'POST' and ('height-feet' in request.form) and ('height-inches' in request.form) and ('weight' in request.form):
    heightFeet = int(request.form.get('height-feet'))
    heightInches = int(request.form.get('height-inches'))

    # height = (round(heightInches / 12, 2)) + heightFeet
    height = round(heightInches + (heightFeet * 12), 2)

    weight = int(request.form.get('weight'))

    bmi = round((weight / (height ** 2)) * 703, 2)

    return render_template('bmi.html', height=height, weight=weight, bmi=bmi)  
  return render_template('bmi.html')
