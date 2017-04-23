# -*- coding: utf-8 -*-
from django.urls import reverse
from django.db import models

# Create your models here.


class Task(models.Model):
    STATUS_CHOICES = (
        ('w', 'В ОЧЕРЕДИ'),
        ('r', 'ВЫПОЛНЯЕТСЯ'),
        ('f', 'ЗАВЕРШЕНА'),
    )

    id = models.AutoField(primary_key=True)  # pylint: disable=invalid-name
    create_time = models.DateTimeField(auto_now=True)
    finish_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default='w')

    def __str__(self):
        return "<Task: %s>" % self.pk

    @property
    def serialize(self):
        """Serialize runner object to string for JSON response"""
        if self.finish_time is not None:
            finish = self.finish_time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            finish = "" 
        return {"id": self.id,
                "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                "finish_time": finish,
                "status": self.get_status_display()}
