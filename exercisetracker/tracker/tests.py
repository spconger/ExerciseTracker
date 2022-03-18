from django.test import TestCase
from .models import Goal, Exercise, DailyExercise, CaloryCount, Weight
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
        self.ex=Exercise(exercisename='pushups',measure='reps',dateentered=entry)

    def test_String(self):
        self.assertEqual(str(self.ex), 'pushups')

    def test_measure(self):
        self.assertEqual(self.ex.measure, 'reps')

    def test_exerciseDate(self):
        self.assertEqual(str(self.ex.dateentered), '2022-02-22')

class TestDailyExercise(TestCase):
    def setUp(self):
        d=datetime.date(2022,3,10)
        self.goal=Goal(goalname="test goal")
        self.exercise=Exercise(exercisename="walking", measure='steps')
        self.daily=DailyExercise(exercisedate=d, exercise=self.exercise, score=1000, goal=self.goal )


    def test_exerciseString(self):
        self.assertEqual(str(self.daily), '2022-03-10')

    def test_exercise(self):
        self.assertEqual(str(self.daily.exercise), 'walking')

    def test_score(self):
        self.assertEqual(self.daily.score, 1000)

    def test_goal(self):
        self.assertEqual(str(self.daily.goal), 'test goal')

class TestCaloryCOunt(TestCase):
    def setUp(self):
        self.goal=Goal(goalname='test')
        date=datetime.date(2022,3,10)
        self.cal=CaloryCount(entrydate=date, calories=1500, goal=self.goal)

    def test_string(self):
        self.assertEqual(str(self.cal), '2022-03-10')

    def test_date(self):
        self.assertEqual(self.cal.entrydate, datetime.date(2022,3,10))

    def test_goal(self):
        self.assertEqual(str(self.cal.goal), 'test')

#tests for non model classes in model
class TestWeight(TestCase):
    def setUp(self):
        date=datetime.date(2022, 3,12)
        self.goal=Goal(goalname="loose weight")
        self.weight=Weight(weightdate=date, weightamt=190, goal=self.goal)
    

    def test_difference(self):
        self.assertEqual(self.weight.distanceFromGoal(190), 20)