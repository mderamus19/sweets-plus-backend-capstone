from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

app_name = "sweetsplusapp"

urlpatterns = [
    url(r'^$',home, name='home'),
    url(r'^categories$',list_categories, name='categories'),
    path(r'^categories/<int:category_id>/', category_details, name='category'),

    url(r'^favorites$',list_favorites, name='favorites'),

    url(r'^recipes$',list_recipes, name='recipes'),
    url(r'^recipes/form$',recipe_form, name='recipe_form'),
    path('recipe/<int:recipe_id>/', recipe_details, name='recipe'),
    url(r'^recipe/(?P<recipe_id>[0-9]+)/form$', recipe_edit_form, name='recipe_edit_form'),

    url(r'^register/$',register_user, name='register'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'login/', auth_views.LoginView.as_view()),
    url(r'^logout/$', logout_user, name='logout'),

]
