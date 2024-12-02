from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):

    # post = Post.objects.all()
    # print(post[0].categories.all())
    posts = Post.objects.all()

    return render(request,"blog/blog.html", {"posts": posts})

def category(request, category_id):
    categorys = get_object_or_404( Category ,id=category_id)
    # posts = Post.objects.filter(categories=category_id)

    return render(request, 'blog/category.html', {"category": categorys})