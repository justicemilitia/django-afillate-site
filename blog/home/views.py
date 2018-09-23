from django.views.generic.list import ListView
from .models import Product

class home_view(ListView):
    model = Product
    paginate_by = 5
    context_object_name = 'articles'
    template_name = 'home.html'


# def home_view(request):
#     numbers_list = range(1, 1000)
#     page = request.GET.get('page', 1)
#     paginator = Paginator(numbers_list, 20)
#     try:
#         numbers = paginator.page(page)
#     except PageNotAnInteger:
#         numbers = paginator.page(1)
#     except EmptyPage:
#         numbers = paginator.page(paginator.num_pages)
#     return render(request, 'home.html', {'numbers': numbers})


# class home_view(ListView):
#     model = Product
#     paginate_by = 5
#     context_object_name = 'articles'
#     template_name = 'sdsdsl'

