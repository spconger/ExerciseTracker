from socket import fromshare
from django import forms
from .models import DailyExercise, Weight, Exercise, Goal, CaloryCount

class ExerciseForm(forms.ModelForm):
    class Meta:
        model=DailyExercise
        fields='__all__'

class WeightForm(forms.ModelForm):
    class Meta:
        model=Weight
        fields='__all__'

class NewExerciseForm(forms.ModelForm):
    class Meta:
        model=Exercise
        fields='__all__'

class NewGoalForm(forms.ModelForm):
    class Meta:
        model=Goal
        fields={'goalname', 'startdate', 'evidence'}

class AddCalories(forms.ModelForm):
    class Meta:
        model=CaloryCount
        fields='__all__'