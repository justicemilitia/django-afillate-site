from django.views.generic.list import ListView
from django.shortcuts import render, HttpResponse, get_object_or_404

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

def product_detail(request, id):

    product = get_object_or_404(Product, id=id)
    context = {
        'product': product,
    }

    return render(request, 'detail.html', context)

# Create your views here.

