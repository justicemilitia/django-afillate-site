from django.views.generic.list import ListView
from .models import Product

class home_view(ListView):
    model = Product
    paginate_by = 8
    context_object_name = 'articles'
    queryset = Product.objects.filter(sort='new')
    template_name = 'home.html'



