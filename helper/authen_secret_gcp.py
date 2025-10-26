import os

def get_secret(secret_name):
    try:
        print("Trying to get secret from GCP ENV")
        secret_path = f"secrets/{secret_name}"
        if os.path.exists(secret_path):
            with open(secret_path, "r") as file:
                return file.read().strip()
        print("Get secret from GCP ENV")
        return os.getenv(secret_name)
    
    except Exception as e:
        print("Failed to get secret from GCP, fallback to local .env file")
        get_secret_name = os.getenv(secret_name)
    return get_secret_name
