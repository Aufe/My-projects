from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from carservice.forms import FeedBack
from .models import Employee, Service
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def team(request):

    
    employees = Employee.objects.all()
    
    return render(request, 'team.html', {'empl': employees})

def services(request):

    services = Service.objects.all()

    return render(request, 'services.html', {'services': services})

def feedback(request):

    if request.method == 'POST':
        form = FeedBack(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            car = form.cleaned_data['car']
            message = form.cleaned_data['message']

            service_email = 'ServGadgHack@gmail.com'
            name_mess = {'serv': 'New client', 'client': 'Service Gadget Hackwrench'}
            mess_to_serv = f"Client: {name}.\nPhone: {phone}.\nEmail: {email}.\nCar: {car}.\nMessage: {message}"
            mess_to_client = f"Thank you for choosing our service. We will contact you shortly."


            try:
                send_mail(name_mess['serv'], mess_to_serv, settings.EMAIL_HOST_USER, [service_email]) # to service
                send_mail(name_mess['client'], mess_to_client, settings.EMAIL_HOST_USER, [email]) # to client
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            
            return HttpResponseRedirect('/thanks/')
    else:
        form = FeedBack()
    
    return render(request, 'feedback.html', {'form': form})

    

def thanks(request):
    thanks = 'thanks'
    return render(request, 'thanks.html', {'thanks': thanks})
