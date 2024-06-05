from django.db import models

class AIResponse(models.Model):
    id = models.AutoField(primary_key=True)
    ai_text = models.TextField()

    def __str__(self):
        return self.ai_text[:50]

class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, default='pending')
    importance = models.CharField(max_length=50, default="veryHighg")
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    ai_response = models.ForeignKey(AIResponse, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
