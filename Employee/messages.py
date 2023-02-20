
Validation = {
    'first_name': {
        "blank": "Please provide a first name.",
        "invalid": "First name cannot be blank. First name must contain only alphabetic characters, and no spaces",
    },
    'last_name': {
        "blank": "Please provide a last name.",
        "invalid": "Last name cannot be blank.Last name must contain only alphabetic characters, and no spaces",
    },
    'email':{
        "blank": "Please provide a email.",
        "invalid": "Email is not valid",
        "exists": "Email already exists",
    },
    'username': {
        "blank": "Please provide a username.",
        "invalid": "Username must contain alphanumeric characters, and no spaces",
        "exists": "Username already taken",

    },
    'password': {
        "blank": "Please provide a username.",
        "invalid": "Password is invalid.Password must contain uppercase, lowercase, digit, and special character and no spaces.",
        "do_not_match":"Passwords do not match."
    },
}

RESPONSE_MESSAGES = {
    "registration":{
    "success":"Employee register successfully",
    "failed":"Invalid Credentials"
    },
    "login":{
        "success":"Login successfully",
        "failed":"Login failed.Invalid Credentials",
        }
}
SUCCESS_MESSAGES = {
    "CREATED_SUCCESSFULLY" : "Employee created successfully",
    "UPDATE_SUCCESSFULLY": "Employee updated successfully",
    "DELETE_SUCCESSFULLY": "Employee deleted successfully",

}

