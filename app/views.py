from django.shortcuts import render,get_object_or_404
from .models import technology , topics , subtopics
# Create your views here.
def home(request):
    technologys = technology.objects.all()
    topic = topics.objects.all()
    context={"technology":technologys,
             "topics":topic}
    return render(request,'home.html',context)

def topic(request,id):
    
    topic = topics.objects.filter(technology=get_object_or_404(technology, id=id))
    context = {"topics":topic}
    return render(request,"topic.html",context)

def subtopic(request,id):
    #subtopic = subtopics.objects.filter(topics_name = get_object_or_404(topics,id=id))
    subtopic = subtopics.objects.filter(topics_name = get_object_or_404(topics,id=id))
    return render(request,"subtopics.html",context={"subtopics":subtopic})