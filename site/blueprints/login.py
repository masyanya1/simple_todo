from flask import (Blueprint, request, redirect, session, render_template, 
                   current_app, flash)
from datetime import timedelta

login_view = Blueprint('login_view', __name__)

@login_view.route('/login', methods=['GET', 'POST'])
def login_page() -> None:
    if request.method == 'POST':
        data_user = (current_app.config['USERNAME'], current_app.config['PASSWORD'])
        request_data = tuple(request.form.values())

        if data_user == request_data:
            session['authorized'] = True
            session.permanent = True
            session.permanent_lifetime = timedelta(days=7)
            return redirect('/')
        else:
            flash('Wrong password or username')
        return redirect('/login')

    if session.get('authorized') == True:
        return redirect('/')
    return render_template('login.html')
