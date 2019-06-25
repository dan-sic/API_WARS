from database.data_manager import get_user
import bcrypt
from functools import wraps
from flask import session, redirect

def validate_registration_input(form_data):
    username = form_data.get('username')
    raw_password = form_data.get('password')
    validated = True
    errors = []

    if len(username) < 5:
        validated = False
        errors.append('Username must be at least 5 characters!')

    if len(raw_password) < 6:
        validated = False
        errors.append('Password must be at least 6 characters!')

    return {
        "success": validated,
        "errors": errors
    }


def validate_user(form_data):
    username = form_data.get('username')
    raw_password = form_data.get('password')
    user = get_user(username)

    if user:
        hashed_pw = user['password']
        hashed_pw_encoded = hashed_pw.encode('utf-8')
        valid_password = bcrypt.checkpw(raw_password.encode('utf-8'), hashed_pw_encoded)

    if not user or not valid_password:
        return False

    return True


def logged_only(fn):
    wraps(fn)
    def wrapper(*args, **kwargs):
        if not 'username' in session:
            return redirect('/')
        return fn(*args, **kwargs)
    return wrapper

