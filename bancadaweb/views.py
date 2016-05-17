from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')

# def get_form_data(request):
    # if request.method == 'POST':
    #     form = Person(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         password = form.cleaned_data['password']
    #         email = form.cleaned_data['email']
    #         Supercalifragilistic = form.cleaned_data['Supercalifragilistic']
    #
    #         return HttpResponseRedirect('/thanks/')
    #
    # return render(request, 'success.html', {'form': form})
