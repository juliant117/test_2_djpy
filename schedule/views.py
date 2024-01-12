from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice
# Create your views here.

def home_1(request):
    return HttpResponse("i don't know what i'm doing with my life and my goals")

# --------------------------- old form -------------------------------------
"""
def index(request):
    latest_question_list=Question.objects.order_by("-pub_date")[:5]
    template= loader.get_template("schedule/index.html")

    #output=", ".join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

    context={"latest_question_list": latest_question_list,}
    return HttpResponse(request,template.render(context,request))

def detail(request, question_id):
    #try:
    #    question=Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    #return HttpResponse("You're looking at question %s." % question_id)
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"schedule/detail.html",{"question":question})
    

def results(request, question_id):
    #response = "You're looking at the results of question %s"
    #return HttpResponse(response % question_id)
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"schedule/results.html",{"question":question})

def vote(request, question_id):
    #return HttpResponse("You're voting on question %s" % question_id)
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except(KeyError,Choice.DoesNotExist):
        return render(request,
                      "schedule/detail.html",
                      {
                          "question":question,
                          "error_message":"You didn't select a choice.",
                      },
                      )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("schedule:results", args=(question.id,)))
"""
# --------------------------- new form -------------------------------------

class IndexView(generic.ListView):
    template_name="schedule/index.html"
    context_object_name="latest_question_list"

    def get_queryset(self):
        #"""Return the last five published questions."""
        #return Question.objects.order_by("-pub_date")[:5]
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]

class DetailView(generic.DetailView):
    model=Question
    template_name="schedule/detail.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultView(generic.DetailView):
    model=Question
    template_name ="schedule/results.html"

def vote(request, question_id):
    #return HttpResponse("You're voting on question %s" % question_id)
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except(KeyError,Choice.DoesNotExist):
        return render(request,
                      "schedule/detail.html",
                      {
                          "question":question,
                          "error_message":"You didn't select a choice.",
                      },
                      )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("schedule:results", args=(question.id,)))

