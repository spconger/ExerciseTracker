from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('addExercise/', views.addExercise, name='addexercise'),
    path('getWeights/',views.getWeights, name='getweights'),
    path('addWeight/', views.addWeight, name='addweight'),
    path("newExercise/", views.newExercise, name='newexercise'),
    path('exerciseTotals/', views.exerciseTotals, name='etotals'),
    path('stepsToMiles/', views.stepsToMiles, name='stepstomiles'),
    path('newGoal/', views.newGoal, name='newgoal'),
    path('addCalories/', views.addCalories, name='addcalories'),
    path('getCaloryCounts', views.getCaloryCounts, name='calories'),
    path('about/', views.about, name='about'),
    path('getGoals/', views.getGoals, name='goals'),
    path('getExercises/', views.getExercises, name='exercises'),
]