from urllib import request

from jose import jwt
from social_core.backends.oauth import BaseOAuth2


class StarballersAuthBackend(BaseOAuth2):
    name = 'starballers'
    SCOPE_SEPARATOR = " "
    AUTHORIZATION_URL = 'https://dev-4t6mw13o.us.auth0.com/authorize'
    ACCESS_TOKEN_URL = 'https://dev-4t6mw13o.us.auth0.com/oauth/token'
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [("picture", "picture"), ("email", "email")]
    REDIRECT_STATE = False

    def get_user_details(self, response):
        # Obtain JWT and the keys to validate the signature
        id_token = response.get("id_token")
        jwks = request.urlopen(
            "https://" + self.setting("DOMAIN") + "/.well-known/jwks.json"
        )
        issuer = "https://" + self.setting("DOMAIN") + "/"
        audience = self.setting("KEY")  # CLIENT_ID
        payload = jwt.decode(
            id_token,
            jwks.read(),
            algorithms=["RS256"],
            audience=audience,
            issuer=issuer,
        )
        return {
            "username": payload["nickname"],
            "first_name": payload["name"],
            "picture": payload["picture"],
            "user_id": payload["sub"],
            "email": payload["email"],
        }

    def get_user_id(self, details, response):
        """Return current user id."""
        return details["user_id"]

    def user_data(self, access_token, *args, **kwargs):
        print(access_token)
        return super().user_data(access_token, *args, **kwargs)

