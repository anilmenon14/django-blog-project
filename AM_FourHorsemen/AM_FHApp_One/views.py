from django.shortcuts import render

# Create your views here.


def index(request):
    context_dict = { 'text':'how you doing yo?','number':100}
    return render(request,'AM_FHApp_One/index.html',context_dict)


def other(request):
    return render(request,'AM_FHApp_One/other.html')


def relative(request):
    return render(request,'AM_FHApp_One/relative_url_templates.html')
