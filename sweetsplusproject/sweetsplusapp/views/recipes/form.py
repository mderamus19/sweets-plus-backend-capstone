import sqlite3
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from sweetsplusapp.models import Category
from sweetsplusapp.models import Recipe
from sweetsplusapp.models import model_factory
from ..connection import Connection


def get_categories():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            ct.id,
            ct.name
        from sweetsplusapp_category ct
        """)

        return db_cursor.fetchall()

# @login_required
def recipe_form(request):
    if request.method == 'GET':
        categories = get_categories()
        template = 'recipes/form.html'
        context = {
            'all_categories': categories
        }

        return render(request, template, context)

# @login_required
def recipe_edit_form(request, recipe_id):
    if request.method == 'GET':
        recipe = get_recipe(recipe_id)
        categories = get_categories()

        template = 'recipes/form.html'
        context = {
            'recipe': recipe,
            'all_categories': categories
        }

        return render(request, template, context)