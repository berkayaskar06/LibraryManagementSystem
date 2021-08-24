from django.shortcuts import render,HttpResponse
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.conf import settings

CACHE_TTL = getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)

# Create your views here.
@cache_page(CACHE_TTL)
def home_view(request):
    if request.user.is_authenticated:
        context={
            'isim':'Berkay',
        }
    else:
        context = {
            'isim':'Guest',
        }

    return render(request,'home.html',context)

