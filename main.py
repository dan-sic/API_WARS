from flask import Flask, request, json, render_template, url_for, redirect, flash, session
from database.data_manager import register_user
from utils import validate_registration_input, validate_user
import psycopg2
# import requests
app = Flask(__name__)
app.config['SECRET_KEY'] = '0b95219177b86d8db3fbde38daf944f0'


@app.route('/')
def home():
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
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)