import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required
from sweetsplusapp.models import Category
from sweetsplusapp.models import model_factory
from ..connection import Connection

# @login_required
def list_categories(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                ct.id,
                ct.name
            from sweetsplusapp_category ct
            """)

            all_categories = db_cursor.fetchall()

        template_name = 'categories/list.html'
        return render(request, template_name, {'all_categories': all_categories})

        # return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

    # ???are placeholders to validate parameters
            db_cursor.execute("""
            INSERT INTO sweetsplusapp_category
            (
                name
            )
            VALUES (?)
            """,
            # this is the second argument which is the data dictionary
            (form_data['name']))

# this is now a GET request from the redirect
        return redirect(reverse('sweetsplusapp:categories'))