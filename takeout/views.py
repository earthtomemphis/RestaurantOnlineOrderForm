from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django import forms
from django.http import HttpResponse
from django.urls import reverse_lazy
from . models import Menu, Order
from . forms import OrderForm

# Create your views here.
class HomeView(ListView):
    model = Menu
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        menu = Menu.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["menu"] = menu
        return context

class OrderView(CreateView):
    model = Order
    form_class = OrderForm
    
    def order_valid(self, form):
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
    template_name = 'order.html'