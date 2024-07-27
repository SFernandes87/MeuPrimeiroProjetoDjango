from django.shortcuts import render
from django.http import HttpResponse
from .models import saf
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

# Create your views here.


def home(request):
    # return HttpResponse('<h1>view Home</h1>')
    return render(request, "saf\home.html")


# def safListar(request):
#     # tarefas = [{
#     #     'id':'1',
#     #     'Tarefa':'comprar fraldas'
#     # }]


#     tarefas = saf.objects.all()  # busca todos os dados do banco


#     return render(request, "saf/saflistar.html",{'tarefas':tarefas})

class safListarView(ListView):
    model = saf #classe deve usar o modelo saf (.\saf\models.py)
class safCriarView(CreateView):
    model = saf
    fields = ["titulo","dtFinalizado"]  # Uma lista de campos que o usuario pode alterar
    success_url = reverse_lazy('saf_listar')
