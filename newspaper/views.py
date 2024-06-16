from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from newspaper.models import Topic, Redactor, Newspaper


def index(request):
    num_topics = Topic.objects.count()
    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()

    context = {
        "num_topics": num_topics,
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
    }

    return render(request, "newspaper/index.html", context=context)