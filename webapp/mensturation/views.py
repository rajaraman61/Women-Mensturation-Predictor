import os
import pickle
import pandas as pd
from django.shortcuts import render
from mensturation.models import Period
from mensturation.apps import MensturationConfig

# Create your views here.
def periods(request):
    current_user = request.user
    periods = Period.objects.filter(user_id=current_user.id)
    return render(request,"../templates/pages/periods.html",{'periods':periods})

def predict(request, id):
    periods = Period.objects.filter(id=id)
    data = []
    for period in periods:
        data.append(period.age)
        data.append(period.height)
        data.append(period.weight)
        data.append(period.heart_rate)
        data.append(period.average_heart_rate_per_day)
        data.append(period.average_body_temp_per_day)
        data.append(period.average_calories_burnt_per_day)
    print(data)
    activitiy_model = MensturationConfig.ACTIVITY_MODEL
    gaussian = pickle.load(open(os.path.dirname(os.path.realpath(__file__)) + '\gNB.sav','rb'))
    df = pd.DataFrame([data])
    df.columns = ['Age','Height','Weight','Duration','Heart_Rate','Body_Temp','Calories']
    result =  gaussian.predict(df.head(1))
    result_text = "No result"
    result_num = int(result[0])
    if(result_num == 0):
        result_text = "You are maintaining good lifestyle, so you will get your mensturation at right date"
    elif(result_num == 1):
        result_text = "You mensturation date might delay 1 or 2 days, because of your poor activity"
    elif(result_num == 2):
        result_text = "You will get your mensturation at right date"
    else:
        result_text = "You need little more activity to get regular periods"
        
    return render(request,"../templates/pages/predict.html", {'result': result_text})