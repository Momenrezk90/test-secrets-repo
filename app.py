import requests

# Database credentials
DB_USER = "admin"
DB_PASS = "hardcoded_password_123"

# API configuration
API_KEY = "sk-1234567890abcdefghijklmnopqrstuvwxyz"
SECRET_TOKEN = "ghp_RealLookingGitHubToken1234567890ABCDEF"

def connect_db():
    conn_string = f"mysql://{DB_USER}:{DB_PASS}@localhost/myapp"
    return conn_string

# AWS credentials (bad practice!)
aws_access = "AKIAIOSFODNN7EXAMPLE"
aws_secret = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
