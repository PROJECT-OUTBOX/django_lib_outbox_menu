# from django.shortcuts import render

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "menu/index.html"

class TestMenuView(TemplateView):
    template_name = 'menu/test-menu.html'