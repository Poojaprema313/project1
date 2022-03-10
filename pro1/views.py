from django.http import HttpResponse

def home(request):
    return HttpResponse("welcome to programming world")
def html(request):
    f1=open(r'C:\Users\Admin\Desktop\Django_Venu\Project1\templates\1.htm','r')
    res=f1.read()
    return HttpResponse(res)