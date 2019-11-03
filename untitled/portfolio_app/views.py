from django.shortcuts import render

from blog.models import Post
from portfolio_app.models import Project


def project_index(request):
    projects = Project.objects.all()

    context = {

        'projects': projects

    }

    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)

    context = {

        'project': project

    }

    return render(request, 'project_detail.html', context)


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')

    context = {

        "posts": posts,

    }

    return render(request, "blog_index.html", context)
