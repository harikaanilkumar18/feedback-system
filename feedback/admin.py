from django.contrib import admin
from .models import FeedbackForm, Question, Response, Answer

admin.site.register(FeedbackForm)
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(Answer)

