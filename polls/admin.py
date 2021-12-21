from django.contrib import admin
from django.db.models.fields import CharField

# Register your models here.
from .models import *


class QuestionAdmin(admin.ModelAdmin):
    # fields = ('pub_date', 'question_text')
    list_display = ['question_text', 'pub_date',]
#     list_filter = ['pub_date']
# # 
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]

    #  fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    @admin.display(
            boolean=False,
            ordering='pub_date',
            description='Published recently?',)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
admin.site.register(Questions, QuestionAdmin)




admin.site.register(Choice,)