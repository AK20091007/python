from django.shortcuts import render,redirect

from app1 import models

def mysite4List(request):
    course = models.course.objects.all()
    return render(request,"Home.html",{'courses':course})

def add_studentForm(request):
    if request.method == "GET":
        return render(request, 'Add.html')
    course_id = request.POST.get("course_ID")
    course_title = request.POST.get("course_Title")
    course_instructor = request.POST.get("course_Instructor")
    models.course.objects.create(course_id=course_id,course_title=course_title,course_instructor=course_instructor,course_capacity=30,course_openseats=30)
    return redirect("/course/list/")

def add_student(request,course_id):
    res = models.course.objects.filter(id=course_id).first()
    if res.course_openseats != 0:
        models.course.objects.filter(id=course_id).update(course_openseats=(res.course_openseats-1))
    return redirect("/course/list/")

def drop_student(request,course_id):
    res = models.course.objects.filter(id=course_id).first()
    if res.course_openseats < res.course_capacity:
        models.course.objects.filter(id=course_id).update(course_openseats=(res.course_openseats+1))
    return redirect("/course/list/")

def delete_student(request,course_id):
    models.course.objects.filter(id=course_id).delete()
    return redirect("/course/list/")