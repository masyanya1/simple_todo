from flask import Blueprint, render_template, request, redirect, flash
from db import get_task, delete_task

action_task_view = Blueprint('action_task', __name__)

@action_task_view.route('/task/<int:task_id>')
def get_one_task(task_id: int = None) -> None:
    task_info = get_task(task_id)

    if not task_info:
        flash('No such task')
        return render_template('task_view.html', task=None)

    else:
        return render_template('task_view.html', task=task_info)

@action_task_view.route('/task/complete/<int:task_id>')
def complete_task_url(task_id: int = None) -> None:
    delete_task(task_id)

    return redirect('/')

@action_task_view.route('/task/delete/<int:task_id>')
def delete_task_url(task_id: int = None) -> None:
    delete_task(task_id)

    return redirect('/')
