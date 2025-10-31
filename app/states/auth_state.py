import reflex as rx


class AuthState(rx.State):
    show_login_dialog: bool = False
    show_register_dialog: bool = False
    is_logged_in: bool = False
    username: str = ""

    @rx.event
    def set_show_login_dialog(self, value: bool):
        self.show_login_dialog = value

    @rx.event
    def set_show_register_dialog(self, value: bool):
        self.show_register_dialog = value

    @rx.event
    def toggle_login_dialog(self):
        self.show_login_dialog = not self.show_login_dialog

    @rx.event
    def login(self, form_data: dict):
        """Login the user."""
        self.is_logged_in = True
        self.username = form_data["username"]
        self.show_login_dialog = False

    @rx.event
    def register(self, provider: str):
        """Register the user via a third party provider."""
        self.is_logged_in = True
        self.username = f"User_{provider}"
        self.show_register_dialog = False

    @rx.event
    def logout(self):
        """Logout the user."""
        self.is_logged_in = False
        self.username = ""