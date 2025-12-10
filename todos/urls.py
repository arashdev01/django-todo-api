# todos/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# 1. تعریف روتر (Router)
# روتر یک ابزار خودکار DRF است که آدرس‌های CRUD را برای ViewSet شما می‌سازد.
router = DefaultRouter()

# 2. ثبت ViewSet
# با این کار، آدرس‌های tasks/ و tasks/<id>/ به TaskViewSet متصل می‌شوند.
router.register('tasks', TaskViewSet, basename='task')

# 3. تعریف الگوهای آدرس
urlpatterns = [
    # تمام آدرس‌هایی که روتر ساخته را اضافه می‌کند.
    path('', include(router.urls)), 
]