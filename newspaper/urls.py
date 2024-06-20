from django.urls import path, include
from newspaper.views import (index,
                             TopicListView, TopicCreateView, TopicUpdateView, TopicDeleteView,
                             RedactorListView, RedactorCreateView, RedactorUpdateView, RedactorDeleteView,
                             RedactorDetailView,
                             NewspaperListView, NewspaperCreateView, NewspaperUpdateView, NewspaperDeleteView,
                             TopicDetailView, NewspaperDetailView, )

app_name = "newspaper"

urlpatterns = [
    path('index/', index, name='index'),
    path('', index, name='index'),

    # region ---------- Topic Views  ----------
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topics/<int:pk>/update/", TopicUpdateView.as_view(), name="topic-update"),
    path("topics/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic-delete"),
    # endregion ---------- Topic Views  ----------

    # region ---------- Redactor Views  ----------
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/create/", RedactorCreateView.as_view(), name="redactor-create"),
    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path("redactors/<int:pk>/update/", RedactorUpdateView.as_view(), name="redactor-update"),
    path("redactors/<int:pk>/delete/", RedactorDeleteView.as_view(), name="redactor-delete"),
    # endregion ---------- Redactor Views  ----------

    # region ---------- Newspaper Views  ----------
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("newspapers/create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("newspapers/<int:pk>/update/", NewspaperUpdateView.as_view(), name="newspaper-update"),
    path("newspapers/<int:pk>/delete/", NewspaperDeleteView.as_view(), name="newspaper-delete"),
    # endregion ---------- Newspaper Views  ----------
]
