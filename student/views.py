from django.shortcuts import redirect, render
from.models import Student
from django.http import HttpResponse
# from .forms import Student_form

# Create your views here.

def register(request):
    if request.method=='POST':
        sid=request.POST['s1']
        name=request.POST['n1']
        age=request.POST['a1']
        address=request.POST['ad1']
        mark=request.POST['m1']
        data=Student.objects.create(s_id=sid,name=name,age=age,address=address,mark=mark)
        data.save()
        return HttpResponse("................ successfully created............")
    return render(request,'register.html')


def display(request):
    data=Student.objects.all()
    return render(request,'display.html',{'x':data})




def delete(request,pk):
    data=Student.objects.get(pk=pk)
    data.delete()
    return display(request)


def update_new(request,pk):
    obj=Student.objects.get(id=pk)
    context={
        'x':obj
    }
    if request.method=='POST':
        obj=Student.objects.get(id=pk)
        obj.s_id=request.POST.get('s1')
        obj.name=request.POST.get('n2')
        obj.age=request.POST.get('a2')
        obj.address=request.POST.get('ad2')
        obj.mark=request.POST.get('m2')
        obj.save()
        return redirect('/student/display/')
    return render(request,'update.html',context)

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import android_serializers


class student_view(APIView):
    def get(self,request):
        ob=Student.objects.all()
        ser=android_serializers(ob, many=True)
        return Response(ser.data)
    def post(self,request):
        ser=android_serializers(data=request.data)
        if ser.is_valid():
            ser.save()
        return  Response("ok")


