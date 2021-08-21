from django.shortcuts import render,HttpResponse

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        context={
            'isim':'Berkay',
        }
    else:
        context = {
            'isim':'misafir',
        }

    return render(request,'home.html',context)

