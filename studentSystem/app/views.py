from django.shortcuts import render,redirect

from app import models

# Create your views here.
def course_list(request):
    course = models.course.objects.all()
    return render(request,"main.html",{'course':course})

def add_course(request):
    if request.method == "GET":
        return render(request, 'add.html')

    courseid = request.POST.get("course_ID")
    coursetitle = request.POST.get("course_Title")
    courseinstructor = request.POST.get("course_Instructor")
    coursecapacity = request.POST.get("course_capacity")
    courseopenSeats = request.POST.get("course_openSeats")

    models.course.objects.create(courseid=courseid,coursetitle=coursetitle,courseinstructor=courseinstructor,coursecapacity=coursecapacity,courseopenSeats=courseopenSeats)

    return redirect("/course/list/")

def add(request,number):
    res = models.course.objects.filter(id=number).first()
    if res.courseopenSeats != 0:
        models.course.objects.filter(id=number).update(courseopenSeats=(res.courseopenSeats-1))
    return redirect("/course/list/")

def drop(request,number):
    res = models.course.objects.filter(id=number).first()
    if res.courseopenSeats < res.coursecapacity:
        models.course.objects.filter(id=number).update(courseopenSeats=(res.courseopenSeats+1))
    return redirect("/course/list/")

def delete(request,number):
    models.course.objects.filter(id=number).delete()
    return redirect("/course/list/")