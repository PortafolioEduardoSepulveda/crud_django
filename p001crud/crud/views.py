from django.shortcuts import render,redirect,get_object_or_404
from .models import task
from .forms import TaskForm

# Create your views here.

def task_list_and_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:crud_list')
    else:
        form = TaskForm()
    # tasks = task.objects.all()
    complete_tasks = task.objects.filter(is_created=True)
    incomplete_tasks = task.objects.filter(is_created=False)

    return render(request,'task_list.html',{
        'form': form,
        'complete_tasks': complete_tasks,
        'incomplete_tasks':incomplete_tasks
     #    'tasks': tasks
    })

def update_task(request,task_id):
    if request.method == 'POST':
        task_db = task.objects.get(id=task_id)
        task_db.is_created = not task_db.is_created
        task_db.save()
        return redirect('crud:crud_list')

def edit_task(request,task_id):
    task_db = get_object_or_404(task,id=task_id)
    initial_data = {
        'title': task_db.title,
        'description':task_db.description
    }
    if request.method == 'POST':
       form = TaskForm(request.POST, instance = task_db)
       if form.is_valid():
            form.save()
            return redirect('crud:crud_list')
    else:
        form = TaskForm(initial_data, instance=task_db)

    return render(request,'edit_task.html',{ 'form': form }) 

def delete_task(request, task_id):
    if request.method == 'POST':
        task_db = task.objects.get(id=task_id)
        task_db.delete()
        return redirect('crud:crud_list')   



                      

