from flask import Blueprint, render_template, request, url_for
# defining this file as a blueprint simply means
# it has a bunch of routes inside of it
# by using blueprint we can have 
# routes defined in multiple files

views = Blueprint('views', __name__)

@views.route('/')
def index():
  return render_template('welcome.html')

@views.route('/bmi_imperial', methods=['GET', 'POST'])
def bmiImperialCalc():
  if request.method == 'POST' and ('height-feet' in request.form) and ('height-inches' in request.form) and ('weight' in request.form):
    heightFeet = int(request.form.get('height-feet'))
    heightInches = int(request.form.get('height-inches'))

    height = round(heightInches + (heightFeet * 12), 2)

    weight = int(request.form.get('weight'))

    bmi = round((weight / (height ** 2)) * 703, 2)

    return render_template('bmi_imperial.html', height=height, weight=weight, bmi=bmi)  
  return render_template('bmi_imperial.html')


@views.route('/bmi_metric', methods=['GET', 'POST'])
def bmiMetricCalc():
  if request.method == 'POST' and ('height-cm' in request.form) and ('weight-kgs' in request.form):
    heightCm = int(request.form.get('height-cm'))
    weightKgs = int(request.form.get('weight-kgs'))

    bmiMetric = round(weightKgs / (heightCm ** 2) * 10_000, 2)

    return render_template('bmi_metric.html', heightCm=heightCm, weightKgs=weightKgs, bmiMetric=bmiMetric )
  return render_template('bmi_metric.html')