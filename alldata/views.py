from django.shortcuts import render
from .models import contactModel,AllUsers
from django.db import  connection
# Create your views here.
from django.shortcuts import render,redirect
from .helpers import  dictfetchall
# Create your views here.
def signupaction(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password=request.POST["password"]
        if  AllUsers.objects.filter(email=email).exists():
                            return render(request,'error.html')


        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO alldata_allusers(first_name,last_name,email,password) values(%s,%s,%s,%s)",(first_name,last_name,email,password))
            
        return redirect('/homepage')

    return render(request,'signup_page.html')

def loginaction(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM alldata_allusers WHERE email=%s AND password=%s",(email,password))
            result=cursor.fetchall()
            if result:
                return redirect('/homepage')
            else:
                return render(request,'error.html')
        



            



   
            

    return render(request,'login_page.html')


# Create your views here.

def create_new_contact(request):

    if request.method=='POST':
        full_name=request.POST['fullname']
        relationship=request.POST['relationship']
        email=request.POST['email']
        phone_number=request.POST['phone-number']
        address=request.POST['address']
        with connection.cursor() as cursor:
            connection.cursor().execute("INSERT INTO contactmodel(full_name,relationship,email,phone_number,address) VALUES(%s,%s,%s,%s)",(full_name,relationship,email,phone_number,address))
        # new_contact=contactModel(
        #     full_name=request.POST['fullname'],
        #     relationship=request.POST['relationship'],
        #     email=request.POST['email'],
        #     phone_number=request.POST['phone-number'],
        #     address=request.POST['address']

        # )
        # new_contact.save()
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
        # with connection.cursor() as cursor:
        #     cursor.execute(f"SELECT * FROM contactmodel WHERE full_name LIKE %{value}%")
        #     allmodel=dictfetchall(cursor)
        #     if allmodel:
        #          return render(request,'homepage.html',{'contact':allmodel})
        #     else:
        #         return render(request,'homepage.html',{'contact':allmodel})
        
        
  
       

    # contact_details=contactModel.objects.all()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM contactmodel")
        response=dictfetchall(cursor)
    return render(request,'homepage.html',{'contact':response})

def detailpage(request,value):
    # myobject=contactModel.objects.get(id=value)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM contactmodel WHERE id=%s",[value])
        response=dictfetchall(cursor)
        print(response)
    return render(request,'profile_details.html',{'object':response[0]})


def editprofile(request,pk):
    # myobject=contactModel.objects.get(id=value)
        if request.method == 'POST':
            full_name=request.POST['fullname']
            relationship=request.POST['relationship']
            email=request.POST['email']
            phone_number=request.POST['phone-number']
            address=request.POST['address']
            with connection.cursor() as cursor:
                connection.cursor().execute("UPDATE contactmodel SET full_name=%s,relationship=%s,email=%s,phone_number=%s,address=%s WHERE id=%s",(full_name,relationship,email,phone_number,address,pk))
                cursor.execute("SELECT * FROM contactmodel WHERE id=%s",[pk])
                response=dictfetchall(cursor)
                return redirect('http://localhost:8000/profile_details/'+str(pk))
           
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM contactmodel WHERE id=%s",[pk])
            response=dictfetchall(cursor)
            print(response)
        return render(request,'edit_contact.html',{'object':response[0]})


def deleteprofile(request,pk):
    with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM contactmodel WHERE id=%s",[pk])
            response=dictfetchall(cursor)
    return render(request,'delete.html',{'object':response[0]})

def deleteprofilebyid(request,pk):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM contactmodel WHERE id=%s",[pk])
            cursor.execute("SELECT * FROM contactmodel")
            response=dictfetchall(cursor)
        return redirect('http://localhost:8000/homepage/')
