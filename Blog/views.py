from django.shortcuts import render

def post_list1(request):
    return render(request, 'blog/post_list1.html', {})
# Create your views here.
