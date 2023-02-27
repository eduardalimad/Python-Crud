from django.shortcuts import render,redirect
from .models import Pessoa,Atividade

# Create your views here.

def home(request):
    pessoas = Pessoa.objects.all()
    notas = Atividade.objects.all()
    return render(request, "index.html",{"pessoas":pessoas, "notas":notas})

def salvar(request):
    vtitle = request.POST.get("title")
    vinfo = request.POST.get("info")
    Atividade.objects.create(title=vtitle,info=vinfo)
    notas=Atividade.objects.all()

    return render(request, "index.html",{ "notas":notas})


def editar(request,id):
    notas=Atividade.objects.get(id=id)
    return render(request, "update.html",{ "notas":notas})
    
def update(request,id):
    vtitle = request.POST.get("title")
    notas=Atividade.objects.get(id=id)
    notas.title= vtitle
    notas.save()
    
    return redirect(home)

def delete(request,id):
    notas=Atividade.objects.get(id=id)
    notas.delete()
    return redirect(home)