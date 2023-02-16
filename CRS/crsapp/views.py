from django.shortcuts import render,redirect

from crsapp import models

# Create your views here.
def courseMenu(request):
    Stream = models.Stream.objects.all()
    return render(request,"StreamList.html",{'Stream':Stream})

def addForm(request):
    if request.method == "GET":
        return render(request, 'StreamAdd.html')

    Streamid = request.POST.get("StreamID")
    Streamtitle = request.POST.get("StreamTitle")
    Streaminstructor = request.POST.get("StreamInstructor")
    Streamcapacity = request.POST.get("Streamcapacity")
    StreamopenSeats = request.POST.get("StreamopenSeats")

    models.Stream.objects.create(Streamid=Streamid,Streamtitle=Streamtitle,Streaminstructor=Streaminstructor,Streamcapacity=Streamcapacity,StreamopenSeats=StreamopenSeats)

    return redirect("/course/list/")

def addID(request,course_number):
    res = models.Stream.objects.filter(id=course_number).first()
    if res.StreamopenSeats != 0:
        models.Stream.objects.filter(id=course_number).update(StreamopenSeats=(res.StreamopenSeats-1))
    return redirect("/course/list/")

def dropID(request,course_number):
    res = models.Stream.objects.filter(id=course_number).first()
    if res.StreamopenSeats < res.Streamcapacity:
        models.Stream.objects.filter(id=course_number).update(StreamopenSeats=(res.StreamopenSeats+1))
    return redirect("/course/list/")

def deleteCRS(request,course_number):
    models.Stream.objects.filter(id=course_number).delete()
    return redirect("/course/list/")