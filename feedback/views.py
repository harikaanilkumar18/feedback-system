from django.shortcuts import render, get_object_or_404, redirect
from .models import FeedbackForm, Question, Response, Answer

def form_list(request):
    forms = FeedbackForm.objects.all()
    return render(request, 'feedback/form_list.html', {'forms': forms})

def fill_form(request, form_id):
    form = get_object_or_404(FeedbackForm, id=form_id)
    questions = Question.objects.filter(form=form)
    return render(request, 'feedback/fill_form.html', {'form': form, 'questions': questions})

def submit_form(request, form_id):
    form = get_object_or_404(FeedbackForm, id=form_id)
    if request.method == 'POST':
        response = Response.objects.create(form=form)
        for q in Question.objects.filter(form=form):
            answer = request.POST.get(str(q.id))
            Answer.objects.create(
                response=response,
                question=q,
                answer_text=answer
            )
        return render(request, 'feedback/thank_you.html')
