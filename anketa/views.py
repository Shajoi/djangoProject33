from django.shortcuts import render
from django.http import  HttpResponse

def index(req):
    return render(req, 'index.html')
from anketa.forms import Nashaforma,Forma2,Uploadforma,Socialform

def forma1(req):
    pass
    # if req.method == 'POST':
    #     if anketa1.is_valid():
    #         name = req.POST.get("name")
    #         num = req.POST.get("num")
    #         output = '''<h1>Спасибо</h1>
    #         <h2>Ваше имя -- {0}</h2>
    #         <h2>Ваше число -- {1}</h2>
    #         '''.format(name,num)
    #         return HttpResponse(output)
    # else:
    #     anketa1 = Nashaforma
    #     data = {'form':anketa1}
    #     return render(req,'form.html',context=data)

def forma3(req):
    if req.method == 'POST':
        k1 = req.POST.get('k1')
        k2 = req.POST.get('k1')
        k4 = req.POST.get('k4')
        k10 = req.POST.get('k10')
        print(k1,k2)
        output =  '''<h1>Спасибо</h1>
            <h2>Ваше имя -- {0}</h2>
            <h2>Ваше число -- {1}</h2>
            <h2>Ваше число -- {2}</h2>
            <h2>Язык -- {3}</h2>
            '''.format(k1,k2,k4,k10)
        return HttpResponse(output)
    else:
        anketa = forma3()
        data = {'form':anketa}
        return render(req,'form.html',context=data)

def upload(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        img = req.FILES.get('img').read
        file = open('anketa/static/upload/123.jpg'.format(name),'wb')
        file.write(img)
        fpath = 'upload/{0}.jpg'.format(name)
        data = {'k1':name,'k2':fpath}
        return render(req,'final.html',context=data)
    else:
        anketa = Uploadforma()
        data = {'form': anketa}
        return render(req, 'form.html', context=data)

def social(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        surname = req.POST.get('surname')
        otchestvo = req.POST.get('otchestvo')
        age = req.POST.get('age')
        language = req.POST.get('language')
        email = req.POST.get('email')
        can_cook = req.POST.get('can_cook')
        with_cat = req.POST.get('with_cat')
        img = req.FILES.get('img')
        data = {'name':name,'surname':surname,'otchestvo':otchestvo,'age':age,'language':language,'email':email,'can_cook':can_cook,'with_cat':with_cat,'img':img}
        return render(req,'social.html',context=data)
    else:
        anketa = Socialform()
        data = {'form': anketa}
        return render(req, 'form.html', context=data)