from django.shortcuts import render
# from django.http import HttpResponse # useless if HttpResponse is off

# def home(request):
#     return HttpResponse('<h1>Blog Home</h1>')

# def about(request):
#     return HttpResponse('<h1>Blog About</h1>')

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 29, 2018'
    },
]
def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')