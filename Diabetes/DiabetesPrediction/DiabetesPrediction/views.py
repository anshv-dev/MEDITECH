from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from django.http import JsonResponse
def home(request):
    return render(request, 'home.html')
def predict(request):
    return render(request, 'predict.html')
def result(request):
    try:
        # Get the query parameters
        n1 = request.GET.get('n1', '')
        n2 = request.GET.get('n2', '')
        n3 = request.GET.get('n3', '')
        n4 = request.GET.get('n4', '')
        n5 = request.GET.get('n5', '')
        n6 = request.GET.get('n6', '')
        n7 = request.GET.get('n7', '')
        n8 = request.GET.get('n8', '')

        # Check if any parameter is an empty string
        if '' in [n1, n2, n3, n4, n5, n6, n7, n8]:
            error_message = 'Empty parameters are not allowed.'
            return render(request, 'predict.html', {'error_message': error_message})

        # Convert parameters to float
        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)
        n4 = float(n4)
        n5 = float(n5)
        n6 = float(n6)
        n7 = float(n7)
        n8 = float(n8)

        # Further processing with the numerical values
        
        # Return the result
        

    except ValueError as e:
        # Handle the ValueError (could not convert string to float)
        error_message = 'Invalid input. Please provide valid numerical values.'
        return render(request, 'predict.html', {'error_message': error_message})
    data =pd.read_csv(r'A:\INNOTECH_2k24\Diabetes\DiabetesPrediction\DiabetesPrediction\diabetes.csv')
    
    # splitting into input and target features
    X=data.drop('Outcome',axis=1)
    Y=data['Outcome']

    # splitting into train and test data
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)

    # training the model
    model=LogisticRegression()
    model.fit(X_train,Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    pred = model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])
    result1 = ""
    if pred == [1]:
        result1="Positive"
    else:
        result1="Negative"   
          

    return render(request, 'predict.html', {"result2":result1})
