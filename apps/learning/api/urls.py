# =================================================================
# apps/learning/urls.py
# -----------------------------------------------------------------
# MIGRATION: Updated URL patterns to use `<int:pk>` or `<int:id>`
# for primary keys, which is standard for relational databases,
# instead of `<str:pk>` which was needed for MongoDB's ObjectId.
# =================================================================

from django.urls import path
from .views import (
    LessonDetailView,
    PathBuilderView,
    LearningPathCreateView,
    CourseManageView,
    LessonCreateView,
    QuizBuilderView,
    TakeQuizView,
    QuizResultView,
)

app_name = 'learning'

urlpatterns = [
    path(
        'courses/<slug:course_slug>/lessons/<int:lesson_order>/',
        LessonDetailView.as_view(),
        name='lesson_detail'
    ),
    path(
        'paths/create/',
        LearningPathCreateView.as_view(),
        name='path_create'
    ),
    path(
        'paths/<int:pk>/build/',
        PathBuilderView.as_view(),
        name='path_builder'
    ),
    path(
        'courses/<int:pk>/manage/',
        CourseManageView.as_view(),
        name='course_manage'
    ),
    path(
        'courses/<int:pk>/add-lesson/',
        LessonCreateView.as_view(),
        name='lesson_add'
    ),
    path(
        'courses/<int:course_pk>/lessons/<int:lesson_id>/quiz-builder/',
        QuizBuilderView.as_view(),
        name='quiz_builder'
    ),
    path(
        'courses/<int:course_pk>/lessons/<int:lesson_id>/take-quiz/',
        TakeQuizView.as_view(),
        name='take_quiz'
    ),
    path(
        'enrollment/<int:enrollment_pk>/quiz-result/<str:attempt_id>/',
        QuizResultView.as_view(),
        name='quiz_result'
    ),
]