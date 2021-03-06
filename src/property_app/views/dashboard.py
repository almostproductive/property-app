from starlette.authentication import requires

from property_app.lib.inertia import InertiaRequest, InertiaHTTPEndpoint


class Dashboard(InertiaHTTPEndpoint):
    @requires(["authenticated"], redirect="Index")
    def get(self, request: InertiaRequest):
        user = request.user

        return {
            "userProfile": {"name": user.name},
            "indexUrl": request.url_for("Index"),
            "signUpUrl": request.url_for("SignUp"),
            "signOutUrl": request.url_for("SignOut"),
            "dashboardUrl": request.url_for("Dashboard"),
            "usersUrl": request.url_for("UserList"),
        }
