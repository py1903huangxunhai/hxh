from django.conf.urls import url
# from .views import index,list
from . import views
app_name = "blog"

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name="index"),
    url(r'^details/(\d+)/$',views.DetailsView.as_view(),name="details"),
    url(r'^category/(\d+)/$',views.CategoryView.as_view(),name="category"),
    url(r'^whisper/$',views.WhisperView.as_view(),name="whisper"),
    url(r'^album/$',views.AlbumView.as_view(),name="album"),
    url(r'^leacots/$',views.LeacotsView.as_view(),name="leacots"),
    url(r'^about/$',views.AboutView.as_view(),name="about"),

]