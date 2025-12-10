# todos/serializers.py

from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    # 1. تعریف صریح owner برای نمایش نام کاربری (username)
    # 2. تنظیم ReadOnlyField برای جلوگیری از ارسال آن توسط کاربر
    owner = serializers.ReadOnlyField(source='owner.username') 

    class Meta:
        model = Task
        # فیلد owner را در لیست fields قرار می‌دهیم تا نمایش داده شود
        fields = ('id', 'owner', 'title', 'description', 'completed')