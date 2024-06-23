from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from newspaper.models import Redactor, Newspaper, Topic
from datetime import datetime

INDEX_URL = reverse("newspaper:index")
REDACTOR_URL = reverse("newspaper:redactor-list")
NEWSPAPER_URL = reverse("newspaper:newspaper-list")
TOPIC_URL = reverse("newspaper:topic-list")


class TopicModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Topic.objects.create(name="test_topic")

    def test_topic_str(self):
        topic = Topic.objects.get(id=1)
        self.assertEqual(str(topic), topic.name)


class NewspaperModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        topic = Topic.objects.create(
            name="test_name",
        )
        redactor = get_user_model().objects.create_user(
            username="test_username",
            password="test_password",
            years_of_experience=5
        )
        newspaper = Newspaper.objects.create(
            title="test_title",
            content="test_content",
            published_date=timezone.now(),
            topic=topic,
        )
        newspaper.publishers.add(redactor)

    def test_newspaper_str(self):
        newspaper = Newspaper.objects.get(id=1)
        self.assertEqual(str(newspaper), newspaper.title)


class PublicTest(TestCase):
    def test_index_accessible(self):
        res = self.client.get(INDEX_URL)
        self.assertEqual(res.status_code, 200)

    def test_newspaper_login_required(self):
        res = self.client.get(NEWSPAPER_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_redactor_login_required(self):
        res = self.client.get(REDACTOR_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_topic_login_required(self):
        res = self.client.get(TOPIC_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_name",
            password="test_password",
        )
        self.client.force_login(self.user)

    def test_retrieve_topics(self):
        Topic.objects.create(name="test_topic")
        Topic.objects.create(name="test_topic_2")
        topics = Topic.objects.all()
        response = self.client.get(TOPIC_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["topic_list"]), list(topics))
        self.assertTemplateUsed(response, "newspaper/topic/topic_list.html")

    def test_retrieve_newspapers(self):
        Newspaper.objects.create(
            title="test_title",
            content="test_content",
            published_date=timezone.now(),
            topic=Topic.objects.create(name="test_topic")
        )
        Newspaper.objects.create(
            title="test_title_2",
            content="test_content_2",
            published_date=timezone.now(),
            topic=Topic.objects.create(name="test_topic_2")
        )
        newspapers = Newspaper.objects.all()
        response = self.client.get(NEWSPAPER_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["newspaper_list"]), list(newspapers))
        self.assertTemplateUsed(response, "newspaper/newspaper/newspaper_list.html")

    def test_retrieve_redactors(self):
        get_user_model().objects.create_user(
            username="test_username",
            password="test_password",
            years_of_experience=5
        )
        get_user_model().objects.create_user(
            username="test_username_2",
            password="test_password_2",
            years_of_experience=3
        )
        redactors = get_user_model().objects.all()
        response = self.client.get(REDACTOR_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["redactor_list"]), list(redactors))
        self.assertTemplateUsed(response, "newspaper/redactor/redactor_list.html")


class AdminPanelTest(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin_user",
            password="admin_password"
        )
        self.client.force_login(self.admin_user)

    def test_redactor_str(self):
        redactor = get_user_model().objects.create(
            username="redactor",
            password="password",
            first_name="First",
            last_name="Last",
            years_of_experience=5
        )
        self.assertEqual(str(redactor), f"{redactor.username} ({redactor.first_name} {redactor.last_name})")

    def test_get_absolute_url(self):
        redactor = get_user_model().objects.create(
            username="redactor",
            password="password"
        )
        self.assertEqual(redactor.get_absolute_url(), reverse("newspaper:redactor-detail", kwargs={"pk": redactor.pk}))
