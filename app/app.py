import reflex as rx
from app.states.dashboard_state import DashboardState, Ticker
from app.states.auth_state import AuthState
from app.components.chart import stock_chart


def login_dialog() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.trigger(
            rx.el.button(
                "Sign In",
                class_name="text-sm font-medium text-white bg-gray-700 px-3 py-1.5 rounded-md hover:bg-gray-600",
            )
        ),
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(
                class_name="fixed inset-0 bg-black/50 backdrop-blur-sm z-40"
            ),
            rx.radix.primitives.dialog.content(
                rx.radix.primitives.dialog.title(
                    "Sign In", class_name="text-2xl font-bold text-white mb-4"
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "Username",
                            class_name="text-sm font-medium text-gray-300 mb-1",
                        ),
                        rx.el.input(
                            name="username",
                            placeholder="Enter your username",
                            class_name="w-full bg-gray-800 border border-gray-700 rounded-md px-3 py-2 text-white focus:outline-none focus:ring-2 focus:ring-blue-500",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Password",
                            class_name="text-sm font-medium text-gray-300 mb-1",
                        ),
                        rx.el.input(
                            name="password",
                            type="password",
                            placeholder="Enter your password",
                            class_name="w-full bg-gray-800 border border-gray-700 rounded-md px-3 py-2 text-white focus:outline-none focus:ring-2 focus:ring-blue-500",
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Sign In",
                            type="submit",
                            class_name="w-full bg-blue-600 text-white font-semibold py-2 rounded-md hover:bg-blue-700 transition-colors",
                        )
                    ),
                    on_submit=AuthState.login,
                    reset_on_submit=True,
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
        open=AuthState.show_login_dialog,
        on_open_change=AuthState.set_show_login_dialog,
    )


def register_dialog() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.trigger(
            rx.el.button(
                "Sign Up",
                class_name="text-sm font-medium text-white bg-blue-600 px-3 py-1.5 rounded-md hover:bg-blue-700",
            )
        ),
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(
                class_name="fixed inset-0 bg-black/50 backdrop-blur-sm z-40"
            ),
            rx.radix.primitives.dialog.content(
                rx.radix.primitives.dialog.title(
                    "Create an Account", class_name="text-2xl font-bold text-white mb-4"
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "Username",
                            class_name="text-sm font-medium text-gray-300 mb-1",
                        ),
                        rx.el.input(
                            name="username",
                            placeholder="Choose a username",
                            class_name="w-full bg-gray-800 border border-gray-700 rounded-md px-3 py-2 text-white focus:outline-none focus:ring-2 focus:ring-blue-500",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Password",
                            class_name="text-sm font-medium text-gray-300 mb-1",
                        ),
                        rx.el.input(
                            name="password",
                            type="password",
                            placeholder="Choose a password",
                            class_name="w-full bg-gray-800 border border-gray-700 rounded-md px-3 py-2 text-white focus:outline-none focus:ring-2 focus:ring-blue-500",
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Create Account",
                            type="submit",
                            class_name="w-full bg-blue-600 text-white font-semibold py-2 rounded-md hover:bg-blue-700 transition-colors",
                        )
                    ),
                    on_submit=AuthState.register,
                    reset_on_submit=True,
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
        open=AuthState.show_register_dialog,
        on_open_change=AuthState.set_show_register_dialog,
    )


def ticker_item(ticker: Ticker) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                ticker["symbol"], class_name="font-medium text-sm text-gray-400"
            ),
            rx.el.span(ticker["price"], class_name="font-semibold text-sm"),
            class_name="flex items-center gap-2",
        ),
        rx.el.span(
            ticker["change"],
            class_name=rx.cond(
                ticker["change"].contains("+"), "text-green-500", "text-red-500"
            ),
        ),
        class_name="flex items-center gap-4 px-4",
    )


def ticker_bar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.foreach(DashboardState.tickers, ticker_item),
            rx.foreach(DashboardState.tickers, ticker_item),
            class_name="flex animate-marquee",
        ),
        class_name="w-full overflow-hidden bg-gray-900/50 py-2 border-y border-gray-700 whitespace-nowrap",
    )


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.icon("bar-chart-big", class_name="h-6 w-6 text-white"),
                rx.el.h1(
                    "Bloomberg",
                    class_name="text-2xl font-bold text-white tracking-tighter",
                ),
                rx.el.div(
                    rx.el.div(
                        class_name=rx.cond(
                            DashboardState.is_market_open,
                            "h-2 w-2 rounded-full bg-green-500 animate-pulse",
                            "h-2 w-2 rounded-full bg-red-500",
                        )
                    ),
                    rx.el.span(DashboardState.market_status, class_name="text-xs"),
                    class_name="flex items-center gap-2 ml-4",
                ),
                class_name="flex items-center gap-2",
            ),
            rx.el.nav(
                rx.el.a(
                    "Markets", href="#", class_name="text-gray-300 hover:text-white"
                ),
                rx.el.a(
                    "Technology", href="#", class_name="text-gray-300 hover:text-white"
                ),
                rx.el.a(
                    "Politics", href="#", class_name="text-gray-300 hover:text-white"
                ),
                rx.el.a(
                    "Economics", href="#", class_name="text-gray-300 hover:text-white"
                ),
                rx.el.a(
                    "Analytics",
                    href="/analytics",
                    class_name="text-gray-300 hover:text-white",
                ),
                rx.el.a("More", href="#", class_name="text-gray-300 hover:text-white"),
                class_name="hidden md:flex items-center gap-6 text-sm font-medium",
            ),
            rx.el.div(
                rx.icon("search", class_name="h-5 w-5 text-gray-400"),
                login_dialog(),
                register_dialog(),
                class_name="flex items-center gap-4",
            ),
            class_name="flex items-center justify-between h-16 px-4 md:px-6",
        ),
        ticker_bar(),
        class_name="bg-gray-900 border-b border-gray-800",
    )


def news_card(article: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=article["thumbnail"], class_name="w-32 h-20 object-cover rounded-md"
            ),
            rx.el.div(
                rx.el.span(
                    article["category"].upper(),
                    class_name="text-xs font-semibold text-blue-400",
                ),
                rx.el.h3(
                    article["title"],
                    class_name="font-semibold text-white mt-1 leading-tight",
                ),
                rx.el.div(
                    rx.el.span(article["source"], class_name="text-xs text-gray-400"),
                    rx.el.span("•", class_name="text-xs text-gray-500"),
                    rx.el.span(article["time"], class_name="text-xs text-gray-500"),
                    class_name="flex items-center gap-2 mt-1",
                ),
                class_name="flex-1",
            ),
            class_name="flex gap-4",
        ),
        class_name="bg-gray-900 border border-gray-800 rounded-lg p-4 hover:bg-gray-800/50 transition-colors",
    )


def market_news_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2("Market News", class_name="text-xl font-bold text-white"),
            rx.el.div(
                rx.foreach(
                    ["latest", "trending", "technology", "economics"],
                    lambda item: rx.el.button(
                        item.capitalize(),
                        on_click=lambda: DashboardState.set_news_filter(item),
                        class_name=rx.cond(
                            DashboardState.active_news_filter == item,
                            "px-3 py-1 text-sm font-medium text-white bg-gray-700 rounded-md",
                            "px-3 py-1 text-sm font-medium text-gray-400 hover:text-white hover:bg-gray-800 rounded-md",
                        ),
                    ),
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.div(
            rx.foreach(DashboardState.news, news_card),
            class_name="grid gap-4 md:grid-cols-2",
        ),
        class_name="bg-gray-900 border border-gray-800 rounded-lg p-4 md:p-6",
    )


def watchlist_item(item: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(item["symbol"], class_name="font-semibold"),
            rx.el.span(item["price"], class_name="text-sm"),
            class_name="flex flex-col",
        ),
        rx.el.div(
            rx.el.span(
                item["change"],
                class_name=rx.cond(
                    item["change"].contains("+"), "text-green-500", "text-red-500"
                ),
            ),
            rx.el.span(
                item["change_percent"],
                class_name=rx.cond(
                    item["change_percent"].contains("+"),
                    "text-green-500",
                    "text-red-500",
                ),
            ),
            class_name="flex flex-col items-end text-sm",
        ),
        class_name="flex items-center justify-between p-2 rounded-md hover:bg-gray-800",
    )


def market_movers_item(item: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(item["symbol"], class_name="font-semibold"),
            rx.el.span(item["name"], class_name="text-xs text-gray-400 truncate"),
            class_name="flex flex-col w-24",
        ),
        rx.el.div(
            rx.el.span(item["price"], class_name="text-sm"),
            rx.el.span(
                f"{item['change']} ({item['change_percent']})",
                class_name=rx.cond(
                    item["change"].contains("+"), "text-green-500", "text-red-500"
                )
                + " text-sm",
            ),
            class_name="flex flex-col items-end",
        ),
        class_name="flex items-center justify-between p-2 rounded-md hover:bg-gray-800",
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.h2("Watchlist", class_name="text-xl font-bold text-white mb-4 px-4"),
            rx.el.div(
                rx.foreach(DashboardState.watchlist, watchlist_item),
                class_name="flex flex-col gap-1",
            ),
            class_name="mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h2("Market Movers", class_name="text-xl font-bold text-white"),
                rx.el.div(
                    rx.el.button(
                        "Gainers",
                        on_click=lambda: DashboardState.set_movers_sort("gainers"),
                        class_name=rx.cond(
                            DashboardState.movers_sort == "gainers",
                            "text-white",
                            "text-gray-400",
                        ),
                    ),
                    rx.el.button(
                        "Losers",
                        on_click=lambda: DashboardState.set_movers_sort("losers"),
                        class_name=rx.cond(
                            DashboardState.movers_sort == "losers",
                            "text-white",
                            "text-gray-400",
                        ),
                    ),
                ),
                class_name="flex justify-between items-center mb-4 px-4",
            ),
            rx.el.div(
                rx.foreach(DashboardState.sorted_movers, market_movers_item),
                class_name="flex flex-col gap-1",
            ),
        ),
        class_name="w-80 bg-gray-900 border-l border-gray-800 p-6 hidden xl:flex flex-col gap-6",
    )


from app.components.sector_performance import sector_performance_grid


def index() -> rx.Component:
    return rx.el.div(
        header(),
        rx.el.div(
            rx.el.main(
                rx.el.div(
                    stock_chart(),
                    market_news_section(),
                    sector_performance_grid(),
                    class_name="grid gap-6",
                ),
                class_name="flex-1 p-4 md:p-6",
            ),
            sidebar(),
            class_name="flex",
        ),
        class_name="min-h-screen bg-gray-950 text-gray-50 font-['Inter']",
    )


from app.analytics import analytics_page

app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)
app.add_page(analytics_page, route="/analytics")