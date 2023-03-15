from django.shortcuts import render
from entrega.models import Post
from entrega.forms import PostForm

def index(request):
    return render(request, "entrega/index.html")


def mostrar_posts(request):
    context = {
         "posts": Post.objects.all(),
         "form": PostForm(),
         }

    
    return render(request, "entrega/admin_post.html", context)


def agregar_post(request):
    post_form = PostForm(request.POST)
    post_form.save()
    context = {
         "posts": Post.objects.all(),
         "form": PostForm(),
         }

    return render(request, "entrega/admin_post.html", context)


def buscar_post(request):
    criterio = request.GET.get("criterio")
    context = { "posts": Post.objects.filter(carousel_caption_title__icontains=criterio).all()}
    return render(request, "entrega/admin_post.html", context)