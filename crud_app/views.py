from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .db_conn import conn

db = conn['employee']
collection = db['employee_details']
from .models import employee

def add_data(request):
    if request.method == 'POST':
        data = request.POST
        emp_id = data.get('emp_id')  
        emp_name = data.get('emp_name')
        emp_age = data.get('emp_age')
        emp_email = data.get('emp_email')
        emp_gender = data.get('emp_gender')
        emp_salary = data.get('emp_salary')
        
        emp_data =  {
                      "emp_id" : emp_id,
                       "emp_name" : emp_name,
                       "emp_age" : emp_age,
                       "emp_email" : emp_email,
                       "emp_gender" : emp_gender,
                       "emp_salary" : emp_salary  
            }
                      
        collection.insert_one(emp_data)

    return render(request , 'insert_data.html')


def view_data(request):
    data = collection.find()
    context = {"employee_info" : data}

    return render(request , 'view_data.html' , context)


def update_data(request , id):
    data1 = collection.find_one({"emp_id" : id})
    if request.method == "POST":
        data = request.POST
        emp_id = data.get('emp_id')  
        emp_name = data.get('emp_name')
        emp_age = data.get('emp_age')
        emp_email = data.get('emp_email')
        emp_gender = data.get('emp_gender')
        emp_salary = data.get('emp_salary')
     
        new_data = {
            '$set' :
           { "emp_id" : emp_id,
            "emp_name" : emp_name,
            "emp_age" : emp_age,
            "emp_email" : emp_email,
            "emp_gender" :emp_gender,
            "emp_salary" : emp_salary }        
        } 

        collection.update_(data1 , new_data)
        return redirect('/show')
    context = {"employee_info" : data1}
    return render(request , 'update_data.html' ,context)

def delete_data(request , id):
    data = collection.find_one({"emp_id" : id})
    collection.delete_one(data)

    return redirect('/show')