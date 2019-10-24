import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from sweetsplusapp.models import Category
from sweetsplusapp.models import model_factory
from ..connection import Connection


def get_category(category_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Category)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            ct.id,
            ct.name
        FROM sweetsplusapp_category ct
        WHERE ct.id = ?
        """, (category_id,))

        return db_cursor.fetchone()

@login_required
def category_details(request, category_id):
    if request.method == 'GET':
        category = get_category(category_id)
        template_name = 'categories/detail.html'
        return render(request, template_name, {'category': category})

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a category
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE sweetsplusapp_category
                SET name = ?
                WHERE id = ?
                """,
                (
                    form_data['name'], category_id,
                ))

            return redirect(reverse('sweetsplusapp:categories'))
