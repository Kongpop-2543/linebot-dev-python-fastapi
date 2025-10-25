from google.cloud import secretmanager
import os

def get_secret():
    try:
        print("Try to get secret from GCP Secret Manager")
        client = secretmanager.SecretManagerServiceClient()
        project_id = os.getenv("GCP_PROJECT_ID")

        access_token_name = f"projects/{project_id}/secrets/ACCESS_TOKEN/versions/latest"
        channel_secret_name = f"projects/{project_id}/secrets/CHANNEL_SECRET/versions/latest"

        access_token_response = client.access_secret_version(name=access_token_name)
        channel_secret_response = client.access_secret_version(name=channel_secret_name)

        get_access_token = access_token_response.payload.data.decode("UTF-8")
        get_channel_secret = channel_secret_response.payload.data.decode("UTF-8")
        print("Successfully get secret from GCP")
        return get_access_token, get_channel_secret
    
    except Exception as e:
        print("Failed to get secret from GCP, fallback to local .env file")
        get_access_token = os.getenv("ACCESS_TOKEN")
        get_channel_secret = os.getenv("CHANNEL_SECRET")
    return get_access_token, get_channel_secret