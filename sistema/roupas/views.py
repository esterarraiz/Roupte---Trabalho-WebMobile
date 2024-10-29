from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from roupas.models import Roupa
from roupas.forms import FormularioRoupa
from django.urls import reverse_lazy

class Home(LoginRequiredMixin, ListView):
    model = Roupa
    context_object_name = 'roupas'
    template_name = 'roupas/home.html'
    def get_queryset(self):
        return Roupa.objects.all()

class CriarAnuncio(LoginRequiredMixin, CreateView):
    model = Roupa
    form_class = FormularioRoupa
    template_name = 'roupas/criar.html'
    success_url = reverse_lazy('principal')

class FotoRoupa(View):
    def get(self, request, arquivo):
        try:
            roupa = Roupa.objects.get(foto='roupas/foto/{}'.format(arquivo))
            return FileResponse(open(roupa.foto.path, 'rb'), content_type='image/jpeg')
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada ou acesso não autorizado!")


class DeletarAnuncio(LoginRequiredMixin, DeleteView):
    model = Roupa
    template_name = 'roupas/deletar.html'
    success_url = reverse_lazy('principal')

class EditarAnuncio(LoginRequiredMixin, UpdateView):
    model = Roupa
    form_class = FormularioRoupa
    template_name = 'roupas/editar.html'
    success_url = reverse_lazy('principal')

    def get_queryset(self):
        return Roupa.objects.all()