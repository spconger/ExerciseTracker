from django.shortcuts import render
from django.db.models import Sum, Count
from .models import Goal, Exercise, Weight, DailyExercise, Miles, WeightDifference, DailyGoal, CaloryCount, CaloryGoal
from .forms import ExerciseForm, WeightForm, NewExerciseForm, NewGoalForm, AddCalories

# Create your views here.
def index(request):
    #count returns the number of obects in a table
    goals=Goal.objects.all().count()
    exercises=Exercise.objects.all().count()
    weights=Weight.objects.all().count()
    calory=CaloryCount.objects.all().count()
    daily=DailyExercise.objects.all().count()


    #you can collect all the different elements into a context
    #and send the context
    context= {
        'goals' : goals,
        'exercises' : exercises,
        'weights' : weights,
        'calory' : calory,
        'daily' : daily,
    }
    return render(request, 'tracker/index.html', context=context)

def about(request):
    return render(request, 'tracker/about.html')

def getGoals(request):
    goals=Goal.objects.all()
    return render (request, 'tracker/goals.html', {'goals' : goals})

def getWeights(request):
    #the [:12] limits the display to 12 items. 
    #It is ordered by the date in descending order
    # the - before weightdate is what signals
    # descending sort
    weights=Weight.objects.all().order_by('-weightdate')[:12]
  
    list_weights=[] #declare a list
    #use the class WeightDifference to calculate the difference
    #of the weight from the goal and then
    #append them to the list
    for w in weights:
        wdif=WeightDifference(w.weightdate, w.weightamt)
        list_weights.append(wdif)

   
    return render (request, 'tracker/getweights.html', {'list_weights' : list_weights})

def exerciseTotals(request):
   #This is more complex statment. The values groups by, the annotate does an aggregate 
   #function--in this case sum, We are summing the score. The records will be sorted
   #by exercisedate in a descending order and limited to 12
    sumTotals=DailyExercise.objects.values('exercisedate').annotate(sum=Sum('score')).order_by("-exercisedate")[:12]
 
   
    return render(request, 'tracker/exercisetotals.html', {'sumTotals': sumTotals})

"""
to convert steps to miles first retrieve all exercieses fileted by exercise_id
for walk. Then create a second list and loop through all the records
and divide steps by 2250 to get miles
add it to the new list and pass this list to the template.
filter is like adding a WHERE clause in SQL
"""
def stepsToMiles(request):
    steps = DailyExercise.objects.filter(exercise_id='7').order_by('-exercisedate')[:15]
  
    miles_list=[]
    #miles is another class I wrote and added to models
    #but it is not a model class. It does not inherit Model.
    for s in steps:
        m=Miles(s.exercisedate, s.score)
        miles_list.append(m)
       
       
    return render(request, 'tracker/stepstomiles.html', {'miles_list' : miles_list})

#similar process
def getCaloryCounts(request):
    cals=CaloryCount.objects.all().order_by('-entrydate')[:15]
    cal_list=[]
    for c in cals:
        c=CaloryGoal(c.entrydate, c.calories)
        cal_list.append(c)
    return render (request, 'tracker/calories.html', {'cal_list' : cal_list})

def getExercises(request):
    exer = Exercise.objects.all()
    return render(request, 'tracker/getexercises.html', {'exer': exer})

 
#Forms
def addExercise(request):
    form=ExerciseForm

    if request.method=='POST':
        form=ExerciseForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=ExerciseForm()
    else:
        form=ExerciseForm()
    return render(request, 'tracker/addexercise.html', {'form': form})

def addWeight(request):
    form=WeightForm

    if request.method=='POST':
        form=WeightForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=WeightForm()
    else:
        form=WeightForm()
    return render(request, 'tracker/addweight.html', {'form': form})

def newExercise(request):
    form=NewExerciseForm

    if request.method=='POST':
        form=NewExerciseForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=NewExerciseForm()
    else:
        form=NewExerciseForm()
    return render(request, 'tracker/newexercise.html', {'form': form})

def newGoal(request):
    form=NewGoalForm

    if request.method=='POST':
        form=NewGoalForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=NewGoalForm()
    else:
        form=NewGoalForm()
    return render(request, 'tracker/newgoal.html', {'form': form})

def addCalories(request):
    form=AddCalories

    if request.method=='POST':
        form=AddCalories(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=AddCalories()
    else:
        form=AddCalories()
    return render(request, 'tracker/addcalories.html', {'form': form})

   
    