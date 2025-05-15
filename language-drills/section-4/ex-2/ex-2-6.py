def role_required(required_role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get("role") == required_role:
                return func(user, *args, **kwargs)
            else:
                print("Access denied")
        return wrapper
    return decorator

@role_required("admin")
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")

admin = {"name": "Geetha", "role": "admin"}
guest = {"name": "Dhoni", "role": "guest"}

delete_user(admin, 101)
delete_user(guest, 102)
