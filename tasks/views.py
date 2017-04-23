import json
from django.views import View
from django.http import JsonResponse, HttpResponse
from tasks.models import Task
from tasks.tasks import some_task


class TasksView(View):

    def get(self, request, *args, **kwargs):
        data = list()
        for task in Task.objects.all().order_by('create_time'):
            data.append(task.serialize)
        return HttpResponse(json.dumps(data))

    def post(self, request, *args, **kwargs):
        task = Task()
        task.save()
        some_task.delay(task.id)
        return HttpResponse(json.dumps(task.serialize))