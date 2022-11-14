from django.shortcuts import render, HttpResponseRedirect
from .models import Sessions, Quizzes, Questions, Services
from .forms import QuestionsForm, SessionForm, UploadFileForm

# Create your views here.
def home(request):
    return render(request, "dashboard/home.html", {})

def all_sessions(request):
    session_list = Sessions.objects.all()
    nb_session = Sessions.objects.all().count
    nb_quizz = Quizzes.objects.all().count
    nb_question = Questions.objects.all().count
    return render(request, "dashboard/session_list.html",
        {"session_list": session_list,
         "nb_session": nb_session,
         "nb_quizz": nb_quizz,
         "nb_question": nb_question,
       })

def add_session(request):
    submitted = False

    if request.method == "POST":
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_session?submitted=True")
    else:
        form = SessionForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "dashboard/add_session.html",{"form" : form, "submitted" : submitted})


def add_question(request):
    submitted = False

    if request.method == "POST":
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_question?submitted=True")
    else:
        form = QuestionsForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "dashboard/add_question.html",{"form" : form, "submitted" : submitted})


def add_quiz(request):
    return render(request, "dashboard/add_quiz.html", {})

def upload_quiz(request):
    return render(request, "dashboard/upload_quiz.html", {})

def quizz(request):
    return render(request, "dashboard/quizz.html", {})

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})