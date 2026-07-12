from django.conf import settings


def set_auth_cookies(response, access_token, refresh_token):
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="Lax",
    )

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=False,
        samesite="Lax",
    )


def clear_auth_cookies(response):
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")


def set_access_cookie(response, access_token):
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="Lax",
    )
