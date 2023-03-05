from django.shortcuts import render
from .models import contactModel,AllUsers
# Create your views here.
from django.shortcuts import render,redirect
import mysql.connector as sql

# Create your views here.
def signupaction(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password=request.POST["password"]
        AllUsers(first_name=first_name,last_name=last_name,email=email,password=password).save()
        return redirect('/homepage')

    return render(request,'signup_page.html')

def loginaction(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        if AllUsers.objects.filter(email=email).exists():
           if(AllUsers.objects.get(email=email).password==password):
                return redirect('/homepage')
           else:
                return render(request,'error.html')
        else:
                return render(request,'error.html')



            



   
            

    return render(request,'login_page.html')


# Create your views here.

def create_new_contact(request):

    if request.method=='POST':
        new_contact=contactModel(
            full_name=request.POST['fullname'],
            relationship=request.POST['relationship'],
            email=request.POST['email'],
            phone_number=request.POST['phone-number'],
            address=request.POST['address']

        )
        new_contact.save()
        return redirect('http://localhost:8000/homepage/')



    return render (request,'new_contact.html')

def homepage(request):
    if request.method=='POST':
        value=request.POST['search-area']
        print(value)
        allmodel=[]
        usermodel=contactModel.objects.all()
        fullnames=[person.full_name for person in usermodel]
        fullnames=[i for i in fullnames if value in i ]
        for i in fullnames:
            objects=contactModel.objects.filter(full_name=i)
            for j in objects:
                allmodel.append(j)
        
        
        
  
        return render(request,'homepage.html',{'contact':allmodel})

    contact_details=contactModel.objects.all()
    return render(request,'homepage.html',{'contact':contact_details})

def detailpage(request,value):
    myobject=contactModel.objects.get(id=value)
    print(type(myobject))
    return render(request,'profile_details.html',{'object':myobject})
