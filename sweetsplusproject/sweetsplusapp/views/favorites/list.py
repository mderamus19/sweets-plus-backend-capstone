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

            all_favorite_recipes = db_cursor.fetchall()

        template_name = 'favorites/list.html'
        return render(request, template_name, {'all_favorites': all_favorite_recipes})
#POST data submitted; process data
    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

    # ??? are placeholders to validate parameters
            db_cursor.execute("""
            INSERT INTO sweetsplusapp_favorites
            (
                r.name,
                f.cook_id
            )
            VALUES (?, ?)
            """,
            # this is the second argument which is the data dictionary
            (form_data['name'], request.user.cook.id))

# this is now a GET request from the redirect
        return redirect(reverse('sweetsplusapp:favorites'))

# Check if this POST is for deleting a recipe
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                    DELETE FROM sweetsplusapp_favorite
                    WHERE id = ?
                """, (favorite_id,))

            return redirect(reverse('sweetsplusapp:favorites'))