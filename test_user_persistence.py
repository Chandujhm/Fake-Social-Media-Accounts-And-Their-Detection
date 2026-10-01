#!/usr/bin/env python3
"""
Test script to demonstrate user persistence functionality
Run this script to test user registration and login persistence
"""

import json
import os
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

def load_users():
    """Load users from file"""
    try:
        if os.path.exists('users.json'):
            with open('users.json', 'r') as f:
                return json.load(f)
        return {}
    except:
        return {}

def save_users(users_data):
    """Save users to file"""
    try:
        with open('users.json', 'w') as f:
            json.dump(users_data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving users: {e}")
        return False

def test_user_creation():
    """Test creating a user and verifying persistence"""
    print("=== Testing User Persistence ===\n")
    
    # Load existing users
    users = load_users()
    print(f"Current users in database: {len(users)}")
    if users:
        for username in users:
            print(f"  - {username}")
    print()
    
    # Create a test user
    test_username = "testuser123"
    test_password = "testpass123"
    
    if test_username not in users:
        print(f"Creating test user: {test_username}")
        users[test_username] = {
            'password': generate_password_hash(test_password),
            'full_name': 'Test User',
            'email': 'test@example.com',
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        if save_users(users):
            print("✅ Test user created and saved successfully!")
        else:
            print("❌ Failed to save test user")
            return False
    else:
        print(f"Test user {test_username} already exists")
    
    # Verify user can be loaded and authenticated
    print("\nTesting authentication...")
    loaded_users = load_users()
    
    if test_username in loaded_users:
        stored_hash = loaded_users[test_username]['password']
        if check_password_hash(stored_hash, test_password):
            print("✅ Authentication successful!")
            print(f"   User: {loaded_users[test_username]['full_name']}")
            print(f"   Email: {loaded_users[test_username]['email']}")
            print(f"   Created: {loaded_users[test_username]['created_at']}")
            return True
        else:
            print("❌ Authentication failed - password mismatch")
            return False
    else:
        print("❌ User not found in loaded data")
        return False

def show_all_users():
    """Display all users in the database"""
    users = load_users()
    print(f"\n=== All Users in Database ({len(users)} total) ===")
    
    if not users:
        print("No users registered yet.")
        return
    
    for username, data in users.items():
        print(f"\nUsername: {username}")
        print(f"  Full Name: {data['full_name']}")
        print(f"  Email: {data['email']}")
        print(f"  Created: {data['created_at']}")

if __name__ == "__main__":
    print("SpamGuard AI - User Persistence Test\n")
    
    # Test user creation and persistence
    success = test_user_creation()
    
    # Show all users
    show_all_users()
    
    if success:
        print("\n✅ User persistence is working correctly!")
        print("\nNow you can:")
        print("1. Register a new account in the web app")
        print("2. Stop and restart the Flask server")
        print("3. Login with the same credentials - they will work!")
    else:
        print("\n❌ User persistence test failed")
        
    print("\nTo test in the web app:")
    print("1. Go to http://127.0.0.1:5000")
    print("2. Register a new account")
    print("3. Restart the Flask server")
    print("4. Login with the same credentials")