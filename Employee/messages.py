# Dictionaries
ERROR_MESSAGES = {
    "FIRST_NAME_REQUIRED" : "Please provide a first name.",
    "LAST_NAME_REQUIRED" : "Please provide a last name.",
    "EMAIL_REQUIRED" : "Please provide an email.",
    "USERNAME_REQUIRED" : "Please provide a username.",
    "PASSWORD_REQUIRED" : "Please provide a password.",
    "PASSWORD_CONFIRMED": "Please confirm password.",
    "PASSWORDS_DO_NOT_MATCH" : "Passwords do not match.",

    "USERNAME_EXISTS": "Username already taken.",
    "EMAIL_EXISTS" : "Email already exists.",
    "INVALID_FIRST_NAME": "First name must contain only alphabetic characters, and no spaces",
    "INVALID_LAST_NAME": "Last name must contain only alphabetic characters, and no spaces",
    "INVALID_EMAIL": "Email address should be in a valid format, and contains no spaces",
    "INVALID_USERNAME": "Username must contain alphanumeric characters and underscores, and no spaces",
    "INVALID_PASSWORD": "Password is invalid.Password must contain uppercase, lowercase, digit, and special character and no spaces.",
    "UNAUTHORIZED": "Cannot create data",

}

# Define a nested dictionary
VALIDATION = {
    'required': {
        'first_name': ERROR_MESSAGES['FIRST_NAME_REQUIRED'],
        'last_name': ERROR_MESSAGES['LAST_NAME_REQUIRED'],
        'email': ERROR_MESSAGES['EMAIL_REQUIRED'],
        'username': ERROR_MESSAGES['USERNAME_REQUIRED'],
        'password': ERROR_MESSAGES['PASSWORD_REQUIRED'],
        'password_confirm': ERROR_MESSAGES['PASSWORD_CONFIRMED']
    },
    'invalid': {
        'first_name': ERROR_MESSAGES['INVALID_FIRST_NAME'],
        'last_name': ERROR_MESSAGES['INVALID_LAST_NAME'],
        'email': ERROR_MESSAGES['INVALID_EMAIL'],
        'username': ERROR_MESSAGES['INVALID_USERNAME'],
        'password': ERROR_MESSAGES['INVALID_PASSWORD']
    },
    'exists': {
        'username': ERROR_MESSAGES['USERNAME_EXISTS'],
        'email': ERROR_MESSAGES['EMAIL_EXISTS']
    },
    'password_mismatch': ERROR_MESSAGES['PASSWORDS_DO_NOT_MATCH']
}

SUCCESS_MESSAGES = {
    "CREATED_SUCCESSFULLY": 'Employee created successfully.',
    'LOGIN_SUCCESSFULLY': 'Employee login successfully.',
    "UPDATED_SUCCESSFULLY" : "Employee updated successfully",
    'DELETED_SUCCESSFULLY': 'Employee deleted successfully.',

}

