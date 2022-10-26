from django.urls import reverse
import datetime

from time import timezone
from urllib import response
from django.test import TestCase
from django.utils import timezone

from . models import Question
# Create your tests here.
# Models and views
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="Quies es el mejor Course Director de Platzi?", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """If no question exists, a message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls available.")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])