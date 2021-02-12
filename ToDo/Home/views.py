from django.shortcuts import render,HttpResponse,get_object_or_404, redirect
from .models import Task

# Create your views here.
def index(request):

    if request.method == 'POST':
        title = request.POST['NewTask']
        print(title)
        ins = Task(task_title=title)
        ins.save()
    all_tasks = Task.objects.all()
    context = {'tasks':all_tasks}
    return render(request, 'index.html', context)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task_pk = task.pk
    task.delete()
    all_tasks = Task.objects.all()
    context = {'tasks':all_tasks}
    return redirect('/')


def delete_all(request):
    all_tasks = Task.objects.all().delete()
    return redirect('/')


# def cat_delete(request, pk):
#     task = get_object_or_404(Task, pk=pk)  # Get your current cat
#
#     if request.method == 'POST':         # If method is POST,
#         task.delete()                     # delete the cat.
#         return redirect('/')             # Finally, redirect to the homepage.
#
#     return render(request, 'index.html', {'tasks': task})
