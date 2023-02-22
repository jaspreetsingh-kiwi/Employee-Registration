# Create messages here

Validation = {
    'first_name': {
        "blank": "Please provide a first name.",
        "invalid": "First name should not be blank."
                   "It must contain only alphabetic characters, and no spaces."
                   "Also make sure first name should start with a capital letter."
    },
    'last_name': {
        "blank": "Please provide a last name.",
        "invalid": "Last name should not be blank."
                   "It must contain only alphabetic characters, and no spaces."
                   "Also make sure last name should start with a capital letter.",
    },
    'email':{
        "blank": "Please provide a email.",
        "invalid": "email is not valid",
        "exists": "email already exists",
    },
    'username': {
        "blank": "Please provide a username.",
        "invalid": "Username must contain alpha or alphanumeric characters, and no spaces",
        "exists": "Username already taken",

    },
    'password': {
        "blank": "Please provide a password.",
        "invalid": "Password is invalid."
                   "It must contain an uppercase, lowercase, digit, and special character and no spaces.",
        "do_not_match":"Passwords do not match.",
    },
}
RESPONSE_MESSAGES = {
    "registration":{
    "success":"Employee register successfully",
    "failed":"Invalid Credentials"
    },
    "login":{
        "success":"Login successfully",
        "failed":"Login failed."
                 "Invalid Credentials",
        }
}
SUCCESS_MESSAGES = {
    "CREATED":{
    "SUCCESSFULLY" : "Department created successfully",
    },
    "UPDATED":{
    "SUCCESSFULLY": "Department updated successfully",
    },
    "DELETED":{
    "SUCCESSFULLY": "Department deleted successfully",
    }
}

