from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings

# Custom authentication handling for JWT cookies. This should be the first pass, with a
# second authentication backend for standard JWT handling in case the cookie isn't found.
# https://stackoverflow.com/a/74353216
class JWTCookieAuthentication(JWTAuthentication):
    def authenticate(self, request):
        cookie = request.COOKIES.get(settings.JWT_COOKIE_NAME)
        if cookie is None:
            return None

        raw_token = cookie.encode(HTTP_HEADER_ENCODING)
        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token