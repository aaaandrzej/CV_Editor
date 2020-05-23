from werkzeug.security import generate_password_hash

# API ON/ OFF
api_on = False

# admin username and password
admin_username = "admin"
admin_password = "admin"

#password hashing, do not edit:
admin_password_hashed = generate_password_hash(admin_password)
