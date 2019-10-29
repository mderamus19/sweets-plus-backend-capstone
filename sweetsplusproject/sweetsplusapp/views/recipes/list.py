import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from sweetsplusapp.models import Recipe, Category
from sweetsplusapp.models import model_factory
from ..connection import Connection

@login_required
def list_recipes(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
            r.id,
            r.name,
            r.description,
            r.ingredients,
            r.cook_time,
            r.instructions,
            r.category_id,
            ct.name category_name,
            ct.id,
            r.cook_id
            from sweetsplusapp_recipe r
            JOIN sweetsplusapp_category ct on r.category_id = ct.id
            WHERE ct.id = ?
            """)

            all_recipes = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                recipe = Recipe()
                recipe.id = row["id"]
                recipe.name = row["name"]
                recipe.category_id = row["category_id"]
                all_recipes.append(recipe)

        template_name = 'categories/detail.html'
        return render(request, template_name, {'all_recipes': all_recipes})

        # return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

    # ???are placeholders to validate parameters
            db_cursor.execute("""
            INSERT INTO sweetsplusapp_recipe
            (
                name,
                description,
                ingredients,
                cook_time,
                instructions,
                category_id,
                cook_id
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            # this is the second argument which is the data dictionary
            (form_data['name'], form_data['description'],
                form_data['ingredients'], form_data['cook_time'],
                form_data["instructions"], form_data["category"], request.user.cook.id))

# this is now a GET request from the redirect
        return redirect(reverse('sweetsplusapp:recipes'))