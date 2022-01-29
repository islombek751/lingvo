from django.shortcuts import redirect, render
from .models import *
# Create your views here.
from django.utils.translation import gettext_lazy as _

import telebot
def home(request):
    advantages = Advantages.objects.all()
    services = Category.objects.all()
    banner = Banner.objects.all()
    questions = Questions.objects.all()
    team = Team.objects.first()
    about = About.objects.first()
    contact = About.objects.first()
    members = team.team.all()    
    clients = about.about.all()    
    context = {"advantages":advantages,'services':services,'team':team,'members':members,
                "banner":banner,'about':about,'clients':clients,'questions':questions,'contact':contact}
    bot = telebot.TeleBot(about.bot_token)
    if request.method == "POST":
        service = request.POST['service']
        name = request.POST['name']
        source = request.POST['source']
        target = request.POST['target']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(service=service,name= name,source=source,target=target,phone=phone,email=email,message=message)
        text = _(f"""New message from Lingvo.uz\n\nFrom: {name}\nEmail: {email}\nPhone: {phone},\n\nService: {service}\nFrom: {source}\nTo: {target}\n\nSubject:\n\n{message}""")
        bot.send_message(about.admin_id,f"{text}")
        print(text)
        return redirect('home')
    return render(request,'index.html',context)