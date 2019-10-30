import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from sweetsplusapp.models import Category, Recipe
from sweetsplusapp.models import model_factory
from ..connection import Connection


def get_favorite(favorite_id):
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
        WHERE r.id = ?
        """, (favorite_id,))

        return db_cursor.fetchone()

# @login_required
# def favorite_details(request, favorite_id):
#     if request.method == 'GET':
#         favorite = get_favorite(favorite_id)
#         template_name = 'favorites/detail.html'
#         return render(request, template_name, {'favorite': favorite})

#     elif request.method == 'POST':
#         form_data = request.POST

#         # Check if this POST is for editing a category
#         if (
#             "actual_method" in form_data
#             and form_data["actual_method"] == "PUT"
#         ):
#             with sqlite3.connect(Connection.db_path) as conn:
#                 db_cursor = conn.cursor()

#                 db_cursor.execute("""
#                 UPDATE sweetsplusapp_category
#                 SET name = ?
#                 WHERE id = ?
#                 """,
#                 (
#                     form_data['name'], category_id,
#                 ))

#             return redirect(reverse('sweetsplusapp:categories'))