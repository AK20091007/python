from django.shortcuts import render,redirect

from app import models

def course_list(request):
    course = models.course.objects.all()
    return render(request,"courseHome.html",{'courses':course})

def getValue(value):
    if value == "":
        return 30
    else:
        return value

def add_courseForm(request):
    if request.method == "GET":
        return render(request, 'courseAdd.html')
    course_id = request.POST.get("courseID")
    course_title = request.POST.get("courseTitle")
    course_instructor = request.POST.get("courseInstructor")
    course_capacity = request.POST.get("coursecapacity") 
    course_openseats = request.POST.get("courseopenSeats")
    course_openseats = getValue(course_openseats)
    course_capacity = getValue(course_capacity)
    models.course.objects.create(course_id=course_id,course_title=course_title,course_instructor=course_instructor,course_capacity=course_capacity,course_openseats=course_openseats)
    return redirect("/course/list/")

def add_Course(request,formid):
    res = models.course.objects.filter(id=formid).first()
    if res.course_openseats != 0:
        models.course.objects.filter(id=formid).update(course_openseats=(res.course_openseats-1))
    return redirect("/course/list/")

def drop_Course(request,formid):
    res = models.course.objects.filter(id=formid).first()
    if res.course_openseats < res.course_capacity:
        models.course.objects.filter(id=formid).update(course_openseats=(res.course_openseats+1))
    return redirect("/course/list/")

def delete_Course(request,formid):
    models.course.objects.filter(id=formid).delete()
    return redirect("/course/list/")