from django.shortcuts import render

def post_list(request):
    return render(request, 'defensora/post_list.html', {})
