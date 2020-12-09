from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from vaccineapp.models import Vaccine, Person, Collection, PersonVaccine, Disease
from vaccineapp.forms import SearchForm, PersonForm
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# def login(request):
#     template = "login.html"
#     params = dict()
#     if request.method == "POST":
#         email = request.POST.get("email", "").lower()
#         password = request.POST.get("password", "")
#         print(request.user.is_authenticated)
#         user = authenticate(username=email, password=password)
#         print(user)
#         if user:
#             print(request.user.is_authenticated)
#             template = "index.html"
#             return render(request, template, params)
#     return render(request, template, params)


def promo(request):
    return render(request, 'promo.html')

@login_required(login_url='/promo')
def index(request):
    # # if not request.user:
    # #     HttpResponseRedirect(reverse('promo'))
    context = {}
    print(request.user.username)

     # создаю нового пользователя
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            userObj = User.objects.get(email=request.user.email)
            person = Person(
                name = form.cleaned_data['name'],
                dateofbirth = form.cleaned_data['dateofbirth'],
                sex = form.cleaned_data['sex'],
                user = userObj
            )
            person.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            context['errors'] = form.errors 


    person_list = Person.objects.filter(user__email__icontains=request.user.email)
    for item in person_list:
        item.vaccine_data = PersonVaccine.objects.filter(person=item)
    context['person_list'] = person_list

    person = PersonForm(initial={'name': 'Artem', 'dateofbirth': '1970-01-01', 'sex': 'M'})
    context['personForm'] = person
    return render(request, 'index.html', context) 

class CollectionList(LoginRequiredMixin, ListView):
    model = Collection

class CollectionDetail(LoginRequiredMixin, DetailView):
    model = Collection

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["persons"] = Person.objects.filter(user__email__icontains=request.user.email)
        return context
    





def collection_json(request):  
    if request.GET:
        form = SearchForm(request.GET)
    else:
        form = SearchForm()
    # если форма не валидная, то автоматически создаётся в форме 
    # ошибки по каждому полю form.errors
    # и можно этим воспользоваться
    search = ''
    if form.is_valid():
        search = form.cleaned_data['search']
        queryset = Collection.objects.filter(name__icontains=search)
    else:
        queryset = Collection.objects.all()

    collection_list = list(queryset.values('id', 'name'))
    return JsonResponse(collection_list, safe=False) 

def disease_json(request, *args, **kwargs): 
    disease_pk = kwargs.get('pk') 
    queryset = Disease.objects.filter(pk=disease_pk)

    disease_list = list(queryset.values('id', 'name', 'vaccines', 'vaccines__name'))
    return JsonResponse(disease_list, safe=False) 

def person_vaccine_item(request, *args, **kwargs): 
    person_vaccine_pk = kwargs.get('pk')
    if request.method == 'POST':
        vaccination_date = request.POST.get('vaccination_date')
        vaccine_id = request.POST.get('vaccine_id')

        obj = PersonVaccine.objects.filter(pk=person_vaccine_pk).first()
        obj.vaccine = Vaccine.objects.filter(pk=vaccine_id).first()
        obj.vaccination_date = vaccination_date
        obj.save()
        vac_list = [obj.vaccine.name, obj.vaccination_date]
        print(vac_list)
        return JsonResponse(vac_list, safe=False) 
    elif request.method == 'DELETE':
        obj = PersonVaccine.objects.filter(pk=person_vaccine_pk).first()
        obj.delete()
        return JsonResponse({'result': True }, safe=False) 

import json

def post_person_vaccine(request, *args, **kwargs):
    # persons = request.POST.get('persons')
    # data = request.POST.get('data')
    # print(request.POST)
    print(request.body)
    reqJson = json.loads(request.body)
    persons = reqJson['persons']
    data = reqJson['data']
    result_list = []
    for person_id in persons:
        for item in data:
            disease_id = item["disease_id"]
            vaccine_id = item["vaccine_id"]
            vaccine = Vaccine.objects.filter(pk=vaccine_id).first()
            obj_list = PersonVaccine.objects.filter(person__pk=person_id,disease__pk=disease_id)
            if not obj_list.exists():
                disease = Disease.objects.filter(pk=disease_id).first()
                person = Person.objects.filter(pk=person_id).first()
                obj = PersonVaccine(vaccine=vaccine, disease=disease, person=person)
                obj.save()
                result_list.append(obj)
    print(result_list)
    return JsonResponse(str(result_list), safe=False)