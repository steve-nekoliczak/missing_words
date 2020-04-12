from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from common import views as common_views
from nlp_json.views import process_sentence


router = routers.DefaultRouter()
router.register(r'documents', common_views.DocumentViewSet)
router.register(r'exercises', common_views.ExerciseViewSet)
router.register(r'users', common_views.UserViewSet)
router.register(r'exercise_attempts', common_views.ExerciseAttemptViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'process_sentence/<str:sentence>/', process_sentence),
    path('admin/', admin.site.urls),
]
