from django.urls import path
from rest_framework.generics import get_object_or_404
from rest_framework.routers import SimpleRouter

from .views import (AvaliacaoAPIView, AvaliacaoViewSet, AvaliacoesAPIView,
                    CursoAPIView, CursosAPIView, CursoViewSet)

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cusros'),

    path('curso/<int:pk>/', CursoAPIView.as_view(), name='cusro'),
    path('curso/<int:curso_pk>/avaliacoes/',
         AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),

    path('curso/<int:curso_pk>/avaliacao/<int:avaliacao_pk>/',
         AvaliacaoAPIView.as_view(), name='curso_avaliacao'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacao/<int:avaliacao_pk>/',
         AvaliacaoAPIView.as_view(), name='avaliacao'),
]
