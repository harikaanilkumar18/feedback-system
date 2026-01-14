from django.db import models

class FeedbackForm(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    form = models.ForeignKey(FeedbackForm, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    question_type = models.CharField(
        max_length=20,
        choices=[('text', 'Text'), ('rating', 'Rating')]
    )

    def __str__(self):
        return self.text

class Response(models.Model):
    form = models.ForeignKey(FeedbackForm, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to {self.form.title}"

class Answer(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()

    def __str__(self):
        return f"Answer to {self.question.text}"
