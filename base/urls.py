from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from common.views.document_view import DocumentViewSet
from common.views.exercise_sentence_view import ExerciseSentenceViewSet
from common.views.user_view import UserViewSet
from common.views.exercise_attempt_view import ExerciseAttemptViewSet
from nlp_json.views import process_sentence


router = routers.DefaultRouter()
router.register(r'documents', DocumentViewSet)
router.register(r'exercise_sentences', ExerciseSentenceViewSet)
router.register(r'users', UserViewSet)
router.register(r'exercise_attempts', ExerciseAttemptViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'process_sentence/<str:sentence>/', process_sentence),
    path('admin/', admin.site.urls),
]
