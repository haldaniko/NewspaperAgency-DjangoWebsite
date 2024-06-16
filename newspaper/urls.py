from django.urls import path, include
from newspaper.views import (index,
                             TopicListView, TopicCreateView, TopicUpdateView, TopicDeleteView)

app_name = "newspaper"

urlpatterns = [
    path("", index, name="index"),

    # region ---------- Topic Views  ----------
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topics/<int:pk>/update/", TopicUpdateView.as_view(), name="topic-update"),
    path("topics/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic-delete"),
    # endregion ---------- Topic Views  ----------

]
