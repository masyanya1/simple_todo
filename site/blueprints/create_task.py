from flask import Blueprint, render_template, request, json, flash, redirect
from db import create_task

create_task_view = Blueprint('create_task', __name__)

# in future add parametrs title, description etc.
@create_task_view.route('/task/create', methods=['GET', 'POST'])
def create_task_page() -> None:
    if request.method == 'POST':
        form_data = request.form

        result = create_task(
                title=form_data['title'],
                description=form_data['description'],
                date=form_data['compl-date']
                )

        if not result:
            flash('Произошла ошибка, невернно введены поля или попробуйте позже')
            return redirect('/task/create')
        else:
            return redirect('/')

    return render_template('create_task.html')
