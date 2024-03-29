from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'data_criacao')

    list_display_links = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'data_criacao')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
