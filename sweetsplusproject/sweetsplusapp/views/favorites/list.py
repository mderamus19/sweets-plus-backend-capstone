import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from sweetsplusapp.models import Category, Recipe, Favorite
from sweetsplusapp.models import model_factory
from ..connection import Connection

@login_required
def list_favorites(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                r.id,
                r.name,
                r.cook_id,
                r.category_id,
                f.recipe_id,
                f.id favorite_id,
                f.cook_id
            from sweetsplusapp_recipe r
            JOIN sweetsplusapp_favorite f
            """)

            all_favorites = db_cursor.fetchall()

        template_name = 'favorites/list.html'
        return render(request, template_name, {'all_favorites': all_favorites})

        # return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

    # ???are placeholders to validate parameters
            db_cursor.execute("""
            INSERT INTO sweetsplusapp_favorites
            (
                r.id
            )
            VALUES (?)
            """,
            # this is the second argument which is the data dictionary
            (form_data['name']))

# this is now a GET request from the redirect
        return redirect(reverse('sweetsplusapp:favorites'))