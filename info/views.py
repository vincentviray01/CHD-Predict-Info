from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
import os
from sklearn.externals import joblib
from enum import Enum
from .models import CHDPredictions

class Education(Enum):
	somehighschool = 1
	highschool = 2
	somecollege = 3
	college = 4

CURRENT_DIR = os.path.dirname(__file__)
model_file = os.path.join(CURRENT_DIR, 'model.joblib')
model = joblib.load(model_file)
def index(request):
	return render(request, 'info/index.html')

def predict(request):
	if request.method == "POST":
		data = request.POST.copy()
		print(data)
		prediction = [0 if data.get('gender') == 'Female' else 1, 0 if data.get('smoker') == 'No' else 1, 0 if data.get('BPMeds') == 'No' else 1, 0 if data.get('stroke') == 'No' else 1, 0 if data.get('hypertension') == 'No' else 1, 0 if data.get('diabetes') == 'No' else 1, getattr(Education, data.get('education')).value, float(data.get('age')), float(data.get('cigs')), float(data.get('cholesterol')), float(data.get('sysBP')), float(data.get('diaBP')), float(data.get('BMI')), float(data.get('heartRate')), float(data.get('glucose'))]
		# prediction = request.GET['prediction']
		obj = CHDPredictions.objects.create(gender = 0 if data.get('gender') == 'Female' else 1, isSmoker = 0 if data.get('smoker') == 'No' else 1, onBPM = 0 if data.get('BPMeds') == 'No' else 1, stroke = 0 if data.get('stroke') == 'No' else 1, hypertension = 0 if data.get('hypertension') == 'No' else 1, diabetes = 0 if data.get('diabetes') == 'No' else 1, education =  data.get('education'), age = float(data.get('age')), cigs = float(data.get('cigs')), cholesterol = float(data.get('cholesterol')), sysBP = float(data.get('sysBP')), diaBP = float(data.get('diaBP')), BMI = float(data.get('BMI')), heartRate = float(data.get('heartRate')), glucose = float(data.get('glucose')), hasCHD = bool(model.predict([prediction])))
		return render(request, 'info/predict.html', {'model_prediction': float("%.2f" % (model.predict_proba([prediction])[0][1] * 100 ))})
	
	return render(request, 'info/predict.html')

def references(request):
	return render(request, 'info/references.html')

def predictions(request):
	predictions = CHDPredictions.objects.all()
	return render(request, 'info/predictions.html', {'dbPredictions': predictions})


def vocabulary(request):
	return render(request, 'info/vocab.html')
# Create your views here.
