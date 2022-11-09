from django.contrib import admin
from .models import Employees, Jobs, Services, Questions, Answers, Quizzes, Sessions, Resultats

# Register your models here.
admin.site.register(Employees)
admin.site.register(Jobs)
admin.site.register(Services)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Quizzes)
admin.site.register(Sessions)
admin.site.register(Resultats)
