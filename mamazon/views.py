from django.views.generic import TemplateView,LiistView
from .models import Product


class Home(TemplateView):
    template_name = 'mamazon/home.html'

class ProductListView(ListView):
    model = Product
    template_name='mamazon/list.html'
