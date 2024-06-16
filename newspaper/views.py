from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
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


# region ---------- Topic Views  ----------
class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "newspaper/topic/topic_list.html"
    paginate_by = 5


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topic-list")

# endregion ---------- Topic Views  ----------
