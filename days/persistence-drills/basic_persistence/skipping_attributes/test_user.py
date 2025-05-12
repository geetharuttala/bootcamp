from user import User

user = User("Geetha", "geethar@gmail.com", "password123","9874563210")

print("Full User Object")
print(user)

print("\nSerialized User (Sensitive data skipped):")
print(user.to_safe_json())