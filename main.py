from flask import Flask, request, render_template, redirect, flash, session
from database.data_manager import register_user
from utils import validate_registration_input, validate_user, logged_only
import psycopg2
import os
# import requests
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('API_KEY')


@app.route('/')
def home():
    print(session)
    return render_template('_planet_list.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form_data = request.form
        validation_results = validate_registration_input(form_data)

        if not validation_results['success']:
            for error in validation_results['errors']:
                flash(error, 'danger')
            return redirect('/register')

        try:
            register_user(form_data)
            return redirect('/')
        except psycopg2.errors.UniqueViolation:
            flash(f'User already exists!', 'danger')
            return redirect('/register')
    return render_template('_register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(session)
    if request.method == 'POST':
        form_data = request.form
        validated_user = validate_user(form_data)

        if not validated_user:
            flash(f'Wrong credentials!', 'danger')
            return redirect('/login')

        session['username'] = form_data.get('username')
        return redirect('/')

    return render_template('_login.html')




    return render_template('_login.html')


@app.route('/logout')
def logout():
    session.pop('username')
    print(session)
    return redirect('/')


@app.route('/secret')
@logged_only
def secret():
    return 'This is secret!'


if __name__ == '__main__':
    app.run(debug=True)