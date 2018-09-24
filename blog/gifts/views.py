from django.views.generic.list import ListView

from home.models import Product

class gifts_formen_view(ListView):
    model = Product
    paginate_by = 8
    context_object_name = 'articles'
    queryset = Product.objects.filter(sort='gfm')
    template_name = 'gifts/home.html'

class gifts_forwomen_view(ListView):
    model = Product
    paginate_by = 8
    context_object_name = 'articles'
    queryset = Product.objects.filter(sort='gfwm')
    template_name = 'gifts/home.html'

# Create your views here.

