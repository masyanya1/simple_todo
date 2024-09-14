from flask import Blueprint, session, redirect
from .tasks import tasks_view
from .create_task import create_task_view
from .action_task import action_task_view

main_tasks = Blueprint('main_tasks', __name__)

main_tasks.register_blueprint(tasks_view)
main_tasks.register_blueprint(create_task_view)
main_tasks.register_blueprint(action_task_view)

@main_tasks.before_request
def not_authorized() -> None:
    if not session.get('authorized'):
        return redirect('/login')
