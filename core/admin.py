from django.contrib import admin

from .models import Pessoa,Atividade

admin.site.register(Pessoa)
admin.site.register(Atividade)