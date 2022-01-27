from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    advantages = Advantages.objects.all()
    services = Category.objects.all()
    banner = Banner.objects.all()
    questions = Questions.objects.all()
    team = Team.objects.first()
    about = About.objects.first()
    members = team.team.all()    
    clients = about.about.all()    
    context = {"advantages":advantages,'services':services,'team':team,'members':members,
                "banner":banner,'about':about,'clients':clients,'questions':questions}
    return render(request,'index.html',context)