# Create your views here.
from django.http import HttpResponse
from upastesite.models import Paste, Group
from django.shortcuts import render

def index(request):
    latest_paste_list = Paste.objects.order_by('-added')[:5]
    context = {'latest_paste_list': latest_paste_list}
    return render(request, 'upastesite/index.html', context)

def paste(request, paste_id):
    return HttpResponse("You're looking for paste #%s" % paste_id)

def group(request, group_id):
    return HttpResponse("You're looking for group #%s" % group_id)
