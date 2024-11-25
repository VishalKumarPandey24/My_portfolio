from django.shortcuts import render

# Create your views here.
def contact(request):
    context={'contact':'active'}
    return render(request,'cnt/cnt.html',context)