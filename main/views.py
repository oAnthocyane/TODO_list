from django.shortcuts import render, redirect
from .models import Homework


def index(request):
    homework = Homework.objects.all()


    return render(request, 'main/index.html', {'homework':homework})


def timetable(request):
    user_agent = request.META['HTTP_USER_AGENT']
    keywords = ['Mobile', 'Opera Mini', 'Android', 'iPhone']
    if any(word in user_agent for word in keywords):

        return render(request, 'main/timetable_mobile.html')
    else:
        return render(request, 'main/timetable.html')


def delete(request, pk):
    homework = Homework.objects.get(pk=pk)
    homework.delete()
    return redirect('main')


def add_hw(request):
    if request.method == 'POST':
        homework = Homework()
        homework.lesson = request.POST.get("id_lesson")
        homework.content = request.POST.get("id_content")
        homework.deadline = request.POST.get("id_deadline")
        homework.save()
        return redirect('main')
    return render(request, 'main/add_hw.html')
