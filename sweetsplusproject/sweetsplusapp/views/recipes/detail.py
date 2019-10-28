import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from sweetsplusapp.models import Category, Recipe, Cook
from sweetsplusapp.models import model_factory
from ..connection import Connection


def get_recipe(recipe_id):
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
            r.cook_id
            from sweetsplusapp_recipe r
        WHERE r.id = ?
        """, (recipe_id,))

        return db_cursor.fetchone()

@login_required
def recipe_details(request, recipe_id):
    if request.method == 'GET':
        recipe = get_recipe(recipe_id)
        template_name = 'recipes/detail.html'
        return render(request, template_name, {'recipe': recipe})

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a recipe
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE sweetsplusapp_recipe
                SET id = ?,
                    name = ?,
                    description = ?,
                    ingredients = ?,
                    cook_time = ?,
                    instructions = ?,
                    category_id = ?,
                    cook_id = ?
                WHERE id = ?
                """,
                (
                    form_data['name'], form_data['description'],
                    form_data['ingredients'], form_data['cook_time'],
                    form_data["instructions"], form_data["category"],
                    form_data["cook"], recipe_id,
                ))

            return redirect(reverse('sweetsplusapp:recipes'))

        # Check if this POST is for deleting a recipe
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                    DELETE FROM sweetsplusapp_recipe
                    WHERE id = ?
                """, (recipe_id,))

            return redirect(reverse('sweetsplusapp:recipes'))