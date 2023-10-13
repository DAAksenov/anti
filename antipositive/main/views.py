from django.shortcuts import render

posts = [
    {
        'title': 'Beautiful is better than ugly',
        'author': 'John Doe',
        'content': 'Beautiful is better than ugly',
        'published_at': 'October 1, 2022'
    },
    {
        'title': 'Explicit is better than implicit',
        'author': 'Jane Doe',
        'content': 'Explicit is better than implicit',
        'published_at': 'October 1, 2022'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Zen of Python'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
