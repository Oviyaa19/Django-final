from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# <HINT> Register QuestionInline and ChoiceInline classes here

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# <HINT> Register Question and Choice models here
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Default number of empty choice rows shown

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2  # Default number of empty question rows shown
    inlines = [ChoiceInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'course', 'grade']
    search_fields = ['question_text']
    list_filter = ['course']

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['enrollment', 'score', 'submitted_at']
    list_filter = ['enrollment']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission, SubmissionAdmin)
