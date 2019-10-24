from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

app_name = "sweetsplusapp"

urlpatterns = [
    url(r'^$',home, name='home'),
    url(r'^categories$',list_categories, name='categories'),
    path(r'^categories/<int:category_id>/', category_details, name='category'),
    url(r'^recipes$',list_recipes, name='recipes'),
    url(r'^recipes/form$',recipe_form, name='recipe'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),


]
