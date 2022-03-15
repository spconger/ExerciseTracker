from django.test import TestCase
from .models import Goal, Exercise
import datetime

# Tests for models
class TestGoal(TestCase):
    def setUp(self):
        start=datetime.date(2022,2,22)
        self.goal=Goal(goalname='test goal', startdate=start, evidence="the test is done")
        
    def test_String(self):
        self.assertEqual(str(self.goal),'test goal')

    def test_StartDate(self):
        self.assertEqual(str(self.goal.startdate), '2022-02-22')

    def test_Evidence(self):
        self.assertEqual(self.goal.evidence, 'the test is done')

    def test_AchieveDate(self):
        self.assertIsNone(self.goal.achievedate)

    def test_AchieveDateAdded(self):
        end=datetime.date(2022,4,1)
        self.goal.achievedate=end
        self.assertEqual(str(self.goal.achievedate), '2022-04-01')

class TestExercise(TestCase):
    def setUp(self):
        entry=datetime.date(2022,2,22)
        self.ex=Exercise(excercisename='pushups',measure='reps',dateentered=entry)

    def test_String(self):
        self.assertEqual(str(self.ex, 'pushups'))


