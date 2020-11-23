from django.shortcuts import render
from django.views.generic import ListView, CreateView
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
    template_name = 'order.html'