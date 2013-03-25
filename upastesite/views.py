# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from upastesite.models import Paste, Group
from django.shortcuts import render, get_object_or_404


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
