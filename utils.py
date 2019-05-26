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