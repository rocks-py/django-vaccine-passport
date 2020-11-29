from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from vaccineapp.models import Vaccine, Person, User, Collection
from vaccineapp.forms import SearchForm, PersonForm
from django.urls import reverse
from django.views.generic import ListView
# Create your views here.

def index(request):
    context = {}
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            userObj = User.objects.get(email='temaez@ya.ru')
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

    # search = request.GET.get('search', '')
    form = SearchForm(request.GET)
    # если форма не валидная, то автоматически создаётся в форме 
    # ошибки по каждому полю form.errors
    # и можно этим воспользоваться
    if form.is_valid():
        search = form.cleaned_data['search']
        context['vaccine_list'] = Vaccine.objects.all().filter(name__icontains=search)
        context['searchForm'] = form
    else:
        context['errors'] = form.errors

    person_list = Person.objects.filter(user__email__icontains='temaez')
    context['person_list'] = person_list
    person = PersonForm(initial={'name': 'Artem', 'dateofbirth': '1970-01-01', 'sex': 'M'})
    context['personForm'] = person
    # return HttpResponse("Hello, world. !!! Artemka")
    return render(request, 'index.html', context) 


def collection_list(request):
    context = {}
    # form = SearchForm(request.GET)
    # if form.is_valid():
    #     search = form.cleaned_data['search']
    #     context['collection_list'] = Vaccine.objects.all().filter(name__icontains=search)
    #     context['searchForm'] = form
    # else:
    #     context['errors'] = form.errors

    collection_list = Collection.objects.all()
    context['collection_list'] = collection_list
    return render(request, 'collection_list.html', context) 

class CollectionList(ListView):
    model = Collection