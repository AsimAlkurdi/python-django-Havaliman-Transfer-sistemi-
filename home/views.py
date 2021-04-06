from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    latest_question_list = "asim alkurdi"
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)
