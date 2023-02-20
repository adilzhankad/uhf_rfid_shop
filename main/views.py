from django.shortcuts import render
import requests
from .models import uid
from .forms import uidform
from .auth import sendemail
import sqlite3


def authkod(request):
    if request.method == 'POST':
        kodemail = request.POST.get('kodemail')

    return render(request,'main/auth.html')
def home(request):
        
    return render(request,'main/home.html')



def about(request):
        
    return render(request,'main/about.html')





def future(request):
        
    return render(request,'main/future.html')


kod=0
data =[]
def registery(request):
    if request.method == 'POST':
        no = None
        global data
        global kod
        test = request.POST.get('name')
        print(str(test))



        if str(test) != "None":
            name=request.POST.get('name')
            email=request.POST.get('email')
            ps1=request.POST.get('ps1')
            ps1=request.POST.get('ps2')
            print("test",name)
            data.append(name)
            data.append(email)
            data.append(ps1)



        kodemail = request.POST.get('kodemail')


        if(len(request.POST) >= 4):
            print(email)
            kod = sendemail(email)
            print(kod)
            flag = True
            return render(request,'main/auth.html')
        if type(kodemail) != no  and type(kod) != no:
            print('ke',kodemail,kod)
            if str(kod) == str(kodemail):
                print("yehooo")

                name=data[0]
                email=data[1]
                ps1=data[2]

                print(name,email,ps1)


                db = sqlite3.connect("db.sqlite3")
                sql = db.cursor()

                sql.execute("""CREATE TABLE IF NOT EXISTS users (
                    Name TEXT,
                    Email TEXT,
                    Password TEXT
                ) """)

                db.commit()

                for value in sql.execute("SELECT * FROM users"):
                    print(value)
                    name_arr=[]

                sql.execute(f"INSERT INTO users VALUES (?, ?, ?)",(name, email, ps1))
                db.commit()

                for value in sql.execute("SELECT * FROM users"):
                    print(value)
                data = [] 
            else:
                print("NOOOOOOOOOO:(")
                        

    return render(request,'main/registery.html')




 
def index(request):
    with open('/home/adminu/django_uhf_rfid_shop/uhf_rfid_shop/main/base.txt') as f:
    
        lines = f.readlines()


    basetxt2=[]
    datanow=[]
    suma=[]
    namet=[]
    sumat=[]
    namet2=[]
    sumat2=[]

    p=0

    lines = str(lines)
    basetxt = lines[3:-4]
    
    basetxt = basetxt.replace("'", '')
    basetxt = basetxt.replace(" ", '')
    basetxt = basetxt.split("*")

    len_arr=[]

    tovar=[]

    tovar_arr=[]

    tovar_arr3=[]

    for i in range(len(basetxt)):
        basetxt2.append(basetxt[i][1:-1].split(","))
        print(basetxt)
        datanow.append(basetxt2[i][-1].replace("#"," "))
        sumatxt = "Total: " + basetxt2[i][-2] + "tg"
        suma.append(sumatxt)
        basetxt2[i] = basetxt2[i][0:-2]
    
    v = '\n'
    
    for i in range(len(basetxt2)):
        namet.append(v)
        sumat.append(v)
        tovar_arr.append(datanow[i])
        tovar_arr.append(suma[i])
        for k in range(len(basetxt2[i])):
            if p == 0:
                namet.append(basetxt2[i][k])
                tovar.append(basetxt2[i][k])
                p = 1
            else:
                sumat.append(basetxt2[i][k])
                tovar.append(basetxt2[i][k] + "tg")
                p = 0
                tovar_arr.append(tovar)
                tovar=[]
        
        tovar_arr3.append(tovar_arr)
        tovar_arr=[]
        namet.append(v)
        sumat.append(v)
        namet2.append(namet)
        sumat2.append(sumat)
        len_arr.append(len(namet))

        namet=[]
        sumat=[]
    leng=len(len_arr)

    print(basetxt2) 

    len_arr_test=[]
    len_arr_ran=[]

    for i in range(len(len_arr)):
        for k in range(len_arr[i]):
            len_arr_test.append(k)

        len_arr_ran.append(len_arr_test)

        len_arr_test = []


    return render(request,'main/index.html',{ "datanow" : datanow, 'basetxt2':basetxt2, 
    'suma':suma, 'sumat2': sumat2, 'namet2': namet2, 'len_arr':len_arr, 'leng':leng,
     'len_arr_ran':len_arr_ran, 'leng_ran': range(0,leng), 'tovar_arr3':tovar_arr3})

    return(request)






def insert_num(line,text):
    text.insert(line - 1,text)
