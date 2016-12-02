from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

def home(request):
    params={
        'sentence': 'Главная страница'
    }
    return render(request, 'home.html', context=params)

companies=[
    {'title':'Apple','id':1},
    {'title':'JBL','id':2},
    {'title':'JVC','id':3}
]
companies_dict = {val.get('id'):val for val in companies }

class CompaniesView(View):
    def get(self,request):
        return render (request, 'companies.html', {'companies':companies})

class CompanyView(View):
    def get(self,request,id):
        company = companies_dict.get(int(id))
        return render(request,'company.html',{'company':company})
