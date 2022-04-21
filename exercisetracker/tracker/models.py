from datetime import date, datetime
from xmlrpc.client import DateTime
from django.db import models
import datetime
from django.db.models import Sum, Count

'''These are the model classes. They are fairly basic
I didn't make them too complex.'''
class Goal (models.Model):
    goalname=models.CharField(max_length=255)
    startdate=models.DateField()
    achievedate= models.DateField(null=True, blank=True)
    evidence=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.goalname

    class Meta:
        db_table='goal'

class Exercise(models.Model):
    exercisename=models.CharField(max_length=255)
    measure=models.CharField(max_length=255)
    dateentered = models.DateField()

    def __str__(self):
        return self.exercisename

    class Meta:
        db_table='exercise'

class DailyExercise(models.Model):
    exercisedate=models.DateField()
    exercise = models.ForeignKey(Exercise, on_delete=models.DO_NOTHING)
    goal = models.ForeignKey(Goal, on_delete=models.DO_NOTHING)
    score = models.IntegerField()

    def __str__ (self):
        return str(self.exercisedate)

    class Meta:
        db_table='dailyexercise'

class CaloryCount(models.Model):
    entrydate = models.DateField()
    calories=models.IntegerField()
    goal=models.ForeignKey(Goal, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.entrydate)

    class Meta: 
        db_table='calorycount'

class Journal(models.Model):
    entrytitle = models.CharField(max_length=255)
    entrydate=models.DateField()
    goal = models.ManyToManyField(Goal)
    entrytext=models.TextField()

    def __str__(self):
        return self.entrytitle

    class Meta:
        db_table='journal'



'''These are non-model classes. They are classes I use to do 
and store calculations and data for various views'''

class Weight(models.Model):
    weightdate=models.DateField()
    goal = models.ForeignKey(Goal, on_delete=models.DO_NOTHING)
    weightamt=models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.weightdate)

    class Meta:
        db_table='weight'

    def distanceFromGoal(self, amt):
        goal=170.0
        return amt - goal
        
class Miles():
    def __init__(self, walkdate, steps):
        self.walkdate=walkdate
        self.steps=steps
        self.miles=self.stepsToMiles(self.steps)
            
    def stepsToMiles(self, steps):
        m = steps / 2250
        m=round(m, 2)
        return m
        
    def getWalkdate(self):
        return self.walkdate
        
    def getSteps(self):
        return self.steps

    def getMiles(self):
        return self.miles

class WeightDifference():
    def __init__(self, weightdate, weight):
        self.goalweight=170
        self.weightdate=weightdate
        self.weight=weight
        self.dif=self.calculateDifference(self.weight)

    def calculateDifference(self, weight):
        return weight-self.goalweight

    def getGoalweight(self):
        return self.goalweight

    def getWeightDate(self):
        return self.weightdate

    def getWeight(self):
        return self.weight
    
    def getDif(self):
        return self.dif

class CaloryGoal():
    def __init__(self, entrydate, calories):
        self.entrydate=entrydate
        self.calories=calories
        self.goal=2000
        self.difference=self.calcDifference(self.calories)

    def calcDifference(self,calories):
        return calories-self.goal

    def getEntryDate(self):
        return self.entrydate

    def getCalories(self):
        return self.calories

    def getGoal(self):
        return self.goal

    def getDifference(self):
        return self.difference

class DailyGoal():
    def __init__(self, exercisedate, totalscore):
        self.exercisedate=exercisedate
        self.totalscore=totalscore
        self.rating=self.ratingCalc(self.totalscore)

    def ratingCalc(self, totalscore):
        rate = 0
        if totalscore > 5000:
            rate=5
        elif totalscore > 4000:
            rate=4
        elif totalscore > 3000:
            rate=3
        elif totalscore > 2000:
            rate=2
        else:
            rate=1
        return rate

    def getExerciseDate(self) :
        return self.exercisedate

    def getTotalScore(self):
        return self.totalscore

    def getRating(self):
        return self.rating
