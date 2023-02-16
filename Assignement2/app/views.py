from django.shortcuts import HttpResponse,render,redirect

from app import models

def class_main(request):
    classes = models.classes.objects.all()
    return render(request,"course_main.html",{'classes':classes})

def add_class(request,id):
    res = models.classes.objects.filter(id=id).first()
    if res.classe_openseats != 0:
        models.classes.objects.filter(id=id).update(classe_openseats=(res.classe_openseats-1))
    return redirect("/course/list/")

def drop_class(request,id):
    res = models.classes.objects.filter(id=id).first()
    if res.classe_openseats < res.classe_capacity:
        models.classes.objects.filter(id=id).update(classe_openseats=(res.classe_openseats+1))
    return redirect("/course/list/")

def delete_class(request,id):
    models.classes.objects.filter(id=id).delete()
    return redirect("/course/list/")

def add_classForm(request):
    if request.method == "GET":
        return render(request, 'course_add.html')
    classe_id = request.POST.get("classe_ID")
    classe_title = request.POST.get("classe_Title")
    classe_instructor = request.POST.get("classe_Instructor")
    classe_capacity = request.POST.get("classe_capacity") 
    classe_openseats = request.POST.get("classe_openSeats")
    models.classes.objects.create(classe_id=classe_id,classe_title=classe_title,classe_instructor=classe_instructor,classe_capacity=classe_capacity,classe_openseats=classe_openseats)
    return redirect("/course/list/")