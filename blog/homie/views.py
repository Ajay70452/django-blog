from django.shortcuts import render

def post_list(request):
    return render(request, 'homie/post_list.html', {})
