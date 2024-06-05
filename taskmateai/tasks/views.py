import openai
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.conf import settings
from .models import Tasks, AIResponse
from .serializers import TasksSerializer

openai.api_key = settings.OPENAI_API_KEY

class TaskAPI(viewsets.ModelViewSet):
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()

        # Extra words to include in the AI request to make response more clear
        extra_words = "According to the work description below, give me 5 summarized bullet points to help complete this work."

        # Concatenate
        content = f"{extra_words}\n\n{task.description}"

        # Generate AI response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": content}
            ]
        )

        ai_response_text = response['choices'][0]['message']['content']

        # Create AIResponse and associate it with the task
        ai_response = AIResponse.objects.create(ai_text=ai_response_text)
        task.ai_response = ai_response
        task.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
