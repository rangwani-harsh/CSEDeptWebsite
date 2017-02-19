# Create your views here.
from django.shortcuts import render

from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from django.conf import settings
from .models import Faculty, ProDetails, EduDetails, NewsItem, EventItem, Student,Course
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from cses.forms import ContactForm,ChatForm
from chatmaster.p2p_chat import *
import os
import sys


def faculty(request, id):
    person = Faculty.objects.filter(idx=id)[0]
    areas = person.areas.split(';')
    projects = person.projects.split(';')
    publications = person.publications.split(';')
    eduDetails = EduDetails.objects.filter(idx=id)
    proDetails = ProDetails.objects.filter(idx=id)
    context = {
        'person': person,
        'projects': projects,
        'areas': areas,
        'edu': eduDetails,
        'pro': proDetails,
        'pub': publications
    }

    return render(request, 'eachfaculty.html', context)


def mainfaculty(request):
    person = Faculty.objects.order_by('id')
    faculty_list = []
    for x in person:
        d = {}
        d['name'] = x.name
        d['desig'] = x.desig
        d['address'] = x.address
        d['email'] = x.email
        d['phone'] = x.phone
        d['image'] = x.image.url
        d['link'] = '/eachfaculty/' + str(x.id) + '/'
        faculty_list.append(d)

    context = {

        'list': faculty_list
    }

    return render(request, 'faculty.html', context)

def sendmail(request):
    return render(request, 'sendmail.html')


def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')

    if subject and message and from_email:
        try:
            message = message + str('\n') + str(from_email)
            send_mail(subject, message, from_email, ['harsh.rangwani.cse15@itbhu.ac.in'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['harsh.rangwani.cse15@itbhu.ac.in'],
            )
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm()
    return render(request, 'Contact.html', {'form':
                                                form})


def index(request):
    news = NewsItem.objects.order_by('date')[0:2]
    context = {
        'news': news
    }
    return render(request, 'index.html', context)


def research(request):
    return render(request, 'Research-Test.html')


def event(request):
    event_list = EventItem.objects.order_by('idx')
    final = []
    for x in event_list:
        d = {}
        d['title'] = x.title
        d['desc'] = x.desc
        d['image'] = x.image.url

        d['sub'] = [p.strip('\r\n') for p in x.subevents.split(';')]
        sys.stderr.write(str(d['sub']))
        final.append(d)
    context = {
        'list': final
    }
    return render(request, 'event.html', context)


def aboutus(request):
    return render(request, 'aboutus.html')



def lab(request):
    return render(request, 'lab.html')


def acad(request):
    return render(request, 'Academic.html')


def student(request):
    if request.method=="POST":
        person = []
        q = request.POST.get("query","")
        t = request.POST.get("type","")

        if q and t:
            if t=="name":
                person = Student.objects.filter(name__icontains=q)
            elif t=="roll":
                person = Student.objects.filter(roll = int(q))
        else:
            person = Student.objects.order_by('id')
        sys.stderr.write(str(person))
    else:
        person = []
        person = Student.objects.order_by('id')
    student_btech = []
    student_idd = []
    student_phd = []
    for people in person:
        d = {}
        d['roll'] = people.roll
        d['name'] = people.name
        d['email'] = people.email_id
        d['part'] = people.part
        if people.class_type == 'idd':
            student_idd.append(d)
        elif people.class_type == 'phd':
            student_phd.append(d)
        else:
            student_btech.append(d)

    context = {
        'btech': student_btech,
        'idd': student_idd,
        'phd': student_phd
    }

    return render(request, 'student.html', context)

def chat(request):
    root=tk.Tk()
    p2p_chat=P2pChat(master=root)
    p2p_chat.mainloop()
    
    return render(request,'Thanks.html')


def chatroot(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            return HttpResponseRedirect('/chat/')
    else:
        form = ChatForm()
        import socket
        ip = str(socket.gethostbyname(socket.gethostname()))
    return render(request, 'Chat.html', {'form':
                                                form,'ip':ip})


def thanks(request):
    return render(request,'Thanks.html')
def course(request):
    tr = Course.objects.order_by('id')
    cour = []
    for it in tr:
        k = {}
        k['cscoursecode'] = it.cscoursecode
        k['coursecode'] = it.coursecode
        k['subject'] = it.subject
        k['contacthours'] = it.contacthours
        k['credits'] = it.credits
        k['sem'] = it.sem
        cour.append(k)
    context = {
        'subject': cour
    }
    return render(request, 'Course.html',context)
