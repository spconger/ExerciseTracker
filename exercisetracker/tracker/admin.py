from django.contrib import admin
from .models import Goal, Exercise, DailyExercise, Weight

# Register your models here.
admin.site.register(Goal)
admin.site.register(Exercise)
admin.site.register(DailyExercise)
admin.site. register(Weight)
