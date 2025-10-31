import reflex as rx
from app.states.portfolio_state import PortfolioState


def preferences_dialog() -> rx.Component:
    """User preferences dialog."""
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(
                class_name="fixed inset-0 bg-black/50 backdrop-blur-sm z-40"
            ),
            rx.radix.primitives.dialog.content(
                rx.radix.primitives.dialog.title(
                    "User Preferences", class_name="text-2xl font-bold text-white mb-6"
                ),
                rx.el.form(
                    # Theme preference
                    rx.el.div(
                        rx.el.label(
                            "Theme",
                            class_name="text-sm font-medium text-gray-300 mb-2 block",
                        ),
                        rx.el.select(
                            rx.el.option("Dark", value="dark"),
                            rx.el.option("Light", value="light"),
                            name="theme",
                            value=PortfolioState.user_preferences["theme"],
                            on_change=lambda val: PortfolioState.update_preference("theme", val),
                            class_name="w-full bg-gray-800 border border-gray-700 rounded-md px-3 py-2 text-white focus:outline-none focus:ring-2 focus:ring-blue-500",
                        ),
                        class_name="mb-4",
                    ),
                    # Default view
                    rx.el.div(
                        rx.el.label(
                            "Default View",
                            class_name="text-sm font-medium text-gray-300 mb-2 block",
                        ),
                        rx.el.select(
                            rx.el.option("Markets", value="markets"),
                            rx.el.option("Portfolio", value="portfolio"),
                            rx.el.option("Analytics", value="analytics"),
                            name="default_view",
                            value=PortfolioState.user_preferences["default_view"],
                            on_change=lambda val: PortfolioState.update_preference(
                                "default_view", val
                            ),
                            class_name="w-full bg-gray-800 border border-gray-700 rounded-md px-3 py-2 text-white focus:outline-none focus:ring-2 focus:ring-blue-500",
                        ),
                        class_name="mb-4",
                    ),
                    # Notifications
                    rx.el.div(
                        rx.el.div(
                            rx.el.input(
                                type="checkbox",
                                name="notifications_enabled",
                                checked=PortfolioState.user_preferences[
                                    "notifications_enabled"
                                ],
                                on_change=lambda val: PortfolioState.update_preference(
                                    "notifications_enabled", val
                                ),
                                class_name="h-4 w-4 rounded border-gray-700 bg-gray-800 text-blue-600 focus:ring-2 focus:ring-blue-500",
                            ),
                            rx.el.label(
                                "Enable Notifications",
                                class_name="ml-2 text-sm font-medium text-gray-300",
                            ),
                            class_name="flex items-center mb-3",
                        ),
                        rx.el.div(
                            rx.el.input(
                                type="checkbox",
                                name="email_alerts",
                                checked=PortfolioState.user_preferences["email_alerts"],
                                on_change=lambda val: PortfolioState.update_preference(
                                    "email_alerts", val
                                ),
                                class_name="h-4 w-4 rounded border-gray-700 bg-gray-800 text-blue-600 focus:ring-2 focus:ring-blue-500",
                            ),
                            rx.el.label(
                                "Email Alerts",
                                class_name="ml-2 text-sm font-medium text-gray-300",
                            ),
                            class_name="flex items-center mb-3",
                        ),
                        rx.el.div(
                            rx.el.input(
                                type="checkbox",
                                name="price_alerts_enabled",
                                checked=PortfolioState.user_preferences[
                                    "price_alerts_enabled"
                                ],
                                on_change=lambda val: PortfolioState.update_preference(
                                    "price_alerts_enabled", val
                                ),
                                class_name="h-4 w-4 rounded border-gray-700 bg-gray-800 text-blue-600 focus:ring-2 focus:ring-blue-500",
                            ),
                            rx.el.label(
                                "Price Alerts",
                                class_name="ml-2 text-sm font-medium text-gray-300",
                            ),
                            class_name="flex items-center",
                        ),
                        class_name="mb-6",
                    ),
                    # Buttons
                    rx.el.div(
                        rx.el.button(
                            "Cancel",
                            type="button",
                            on_click=lambda: PortfolioState.set_show_preferences_dialog(
                                False
                            ),
                            class_name="flex-1 bg-gray-700 text-white font-semibold py-2 rounded-md hover:bg-gray-600",
                        ),
                        rx.el.button(
                            "Save Preferences",
                            type="submit",
                            class_name="flex-1 bg-blue-600 text-white font-semibold py-2 rounded-md hover:bg-blue-700",
                        ),
                        class_name="flex gap-3",
                    ),
                    on_submit=PortfolioState.save_preferences,
                ),
                rx.radix.primitives.dialog.close(
                    rx.el.button(
                        rx.icon("x", class_name="h-4 w-4"),
                        class_name="absolute top-4 right-4 text-gray-400 hover:text-white",
                    )
                ),
                class_name="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-gray-900 border border-gray-800 rounded-lg p-8 w-full max-w-md z-50",
            ),
        ),
        open=PortfolioState.show_preferences_dialog,
        on_open_change=PortfolioState.set_show_preferences_dialog,
    )


def export_buttons() -> rx.Component:
    """Export functionality buttons."""
    return rx.el.div(
        rx.el.h3(
            "Export Data",
            class_name="text-lg font-semibold text-white mb-3",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("download", class_name="h-4 w-4 mr-2"),
                "Export as CSV",
                on_click=lambda: PortfolioState.export_data("csv"),
                class_name="flex items-center bg-gray-700 text-white px-4 py-2 rounded-md hover:bg-gray-600 text-sm font-medium",
            ),
            rx.el.button(
                rx.icon("file-text", class_name="h-4 w-4 mr-2"),
                "Export as PDF",
                on_click=lambda: PortfolioState.export_data("pdf"),
                class_name="flex items-center bg-gray-700 text-white px-4 py-2 rounded-md hover:bg-gray-600 text-sm font-medium",
            ),
            class_name="flex gap-3",
        ),
        class_name="bg-gray-900 border border-gray-800 rounded-lg p-6",
    )
