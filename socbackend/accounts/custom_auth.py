from rest_framework_simplejwt.authentication import JWTAuthentication
import logging
logger = logging.getLogger(__name__)


class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        print("Starting authentication process")
        header = None
        try:
            header = super().authenticate(request)
        except Exception as e:
            logger.debug(f"Header login failed: {e}")

        
        if header is None:
            # Attempt to get token from the cookie
            token = request.COOKIES.get("auth")
            print(token)
            if token:
                # Return the user and the validated token
                validated_token = self.get_validated_token(token)
                print(validated_token)
                user = self.get_user(validated_token)
                if user:
                    return (user, validated_token)  # Correctly return user and token
            return None  # No valid authentication

        return header  # If header-based auth worked, return (user, token)