# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from upastesite.models import Paste, Group
from django.shortcuts import render, get_object_or_404

def index(request):
    latest_paste_list = Paste.objects.order_by('-added')[:5]
    context = {'latest_paste_list': latest_paste_list}
    return render(request, 'upastesite/index.html', context)

def new_paste(request):
    if len(request.POST) > 0:
        paste = Paste()
        paste.email = request.POST['email']
        paste.code = request.POST['code']
        paste.group = Group.objects.get(pk=1)
        paste.save()
        return HttpResponseRedirect(reverse('paste', args=(paste.id,)))
    else:
        return render(request, 'upastesite/new_paste.html')

def paste(request, paste_id):
    paste = get_object_or_404(Paste, pk=paste_id)
    return render(request, 'upastesite/paste.html', {'paste':paste})

def group(request, group_id):
    return HttpResponse("You're looking for group #%s" % group_id)
