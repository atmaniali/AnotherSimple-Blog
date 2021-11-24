from django.urls import path
from .views import HomeView, ArticleDetail


urlpatterns = [
    path('', HomeView.as_view(), name = 'index'), # new
    path('article/<int:pk>', ArticleDetail.as_view(), name='detail-article')
]