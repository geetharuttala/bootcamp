def is_valid_user(user):
    return user.get("active") and user.get("age", 0) >= 18

def process_users(users):
    for user in users:
        if is_valid_user(user):
            print(f"Processing: {user['name']}")

users = [{"name": "Geetha", "age": 20, "active": True}, {"name": "Bob", "age": 16, "active": True}]
process_users(users)
