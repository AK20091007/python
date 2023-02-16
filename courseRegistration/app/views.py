from django.shortcuts import HttpResponse,render,redirect

from app import models

# Create your views here.
def courseList(request):
    courses = models.Courses.objects.all()
    return render(request,"courseList.html",{'courses':courses})

def addStudent(request,course_id):
    res = models.Courses.objects.filter(id=course_id).first()
    if res.openSeats != 0:
        models.Courses.objects.filter(id=course_id).update(openSeats=(res.openSeats-1))
    return redirect("/course/list/")

def dropStudent(request,course_id):
    res = models.Courses.objects.filter(id=course_id).first()
    if res.openSeats < res.capacity:
        models.Courses.objects.filter(id=course_id).update(openSeats=(res.openSeats+1))
    return redirect("/course/list/")

def deleteCourse(request,course_id):
    models.Courses.objects.filter(id=course_id).delete()
    return redirect("/course/list/")

def addCourse(request):
    if request.method == "GET":
        return render(request, 'courseAdd.html')

    courseid = request.POST.get("ID")
    title = request.POST.get("Title")
    instructor = request.POST.get("Instructor")
    capacity = request.POST.get("capacity")
    openSeats = request.POST.get("openSeats")

    # update database
    models.Courses.objects.create(courseid=courseid,title=title,instructor=instructor,capacity=capacity,openSeats=openSeats)

    return redirect("/course/list/")