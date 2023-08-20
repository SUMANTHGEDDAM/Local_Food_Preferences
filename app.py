from flask import Flask, render_template, request
import numpy as np
import pandas as pd


app = Flask(__name__)

@app.route('/')
def view():
    return render_template('view.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    recipe=pd.read_csv('.venv//prac_1.csv')
    df=pd.DataFrame(recipe)
    Plac=request.form['Cuisine']
    # Item_id=[]
    Name=[]
    #Place=[]
    Item_type=[]
    Carbohydrates=[]
    Fats=[]
    Proteins=[]
    Calories=[]
    #Images=[]
    for i in df.index:
        if(df['Place'][i]==Plac):
            # Item_id.append(df['Item_id'][i])
            Name.append(df['Name'][i])
            #Place.append(df['Place'][i])
            Item_type.append(df['Item_type'][i])
            Carbohydrates.append(df['Carbohydrates'][i])
            Fats.append(df['Fats'][i])
            Proteins.append(df['Proteins'][i])
            Calories.append(df['Calories'][i])
            #Images.append(df['Images'][i])

    list_of_tuples = list(zip(Name,Item_type,Carbohydrates,Fats,Proteins,Calories))
    df3 = pd.DataFrame(list_of_tuples, columns = ['Name','Item_type','Carbohydrates','Fats','Proteins','Calories']) 
    return render_template('output.html', tables=[df3.to_html(classes='table table-striped table-dark',index=False)] , titles=df3.columns.values,text=Plac)
    