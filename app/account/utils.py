import requests
from django.conf import settings


def verify_google_token(token):
    try:
        # Send the token to Google's OAuth2 token verification endpoint
        response = requests.get(
            "https://oauth2.googleapis.com/tokeninfo", params={"id_token": token}
        )

        # If the response is successful (status 200), process the token info
        if response.status_code == 200:
            token_info = response.json()

            # Verify the audience (client ID)
            if token_info["aud"] != settings.GOOGLE_CLIENT_ID:
                return None

            # Additional checks, e.g., for issuer
            if token_info["iss"] not in [
                "accounts.google.com",
                "https://accounts.google.com",
            ]:
                return None

            # Token is valid, return token information
            return token_info
        else:
            # Invalid token
            return None
    except requests.exceptions.RequestException:
        # Handle potential network issues
        return None
