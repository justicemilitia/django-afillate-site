from django.shortcuts import render, HttpResponse, get_object_or_404

from post.models import Post


def post_index(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'post/index.html', {'posts': posts})


def post_detail(request, id):
    # post = Post.objects.get(id=1)

    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }

    return render(request, 'post/detail.html', context)


def post_create(request):
    return HttpResponse('Post create sayfas')


def post_update(request):
    return HttpResponse('Post Update sayfası')


def post_delete(request):
    return HttpResponse('Post delete sayfası')


# Create your views here.
