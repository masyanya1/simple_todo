from flask import Blueprint, current_app, render_template, redirect, session
from db import get_tasks

tasks_view = Blueprint('tasks_view', __name__)

@tasks_view.route('/tasks')
@tasks_view.route('/')
def show_all_tasks() -> None:
    return render_template('tasks_view.html', tasks=get_tasks())
