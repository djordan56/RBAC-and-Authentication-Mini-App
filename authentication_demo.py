
# Basic Authentication and Role-Based Access Control

# Create users and their roles
users = {
    "david": "admin",
    "kevin": "user",
}

# Ask the user to log in
username = input("Enter your username (david, kevin): ").lower()

# Authenticate the user
if username in users:

    role = users[username]

    print("\nLogin successful!")
    print("Welcome,", username)
    print("Your role is:", role)

    # Admin protected action
    def admin_dashboard():
        print("Access granted: Welcome to the Admin Dashboard.")

    # Regular user protected action
    def user_dashboard():
        print("Access granted: Welcome to the User Dashboard.")

    # Check permissions
    if role == "admin":
        admin_dashboard()
    else:
        print("Access denied: Admin privileges required.")

    if role == "user":
        user_dashboard()
    else:
        print("Access denied: User privileges required.")

else:
    print("\nLogin failed: Username not found.")

# CIA Triad - Confidentiality:
# The program demonstrates confidentiality by restricting
# access to functions based on the user's assigned role.
# Only authorized users can access their permitted dashboards.

