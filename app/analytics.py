import reflex as rx
from app.states.dashboard_state import DashboardState
from app.app import header, ticker_bar

TOOLTIP_PROPS = {
    "content_style": {
        "background": "#1E293B",
        "border_color": "#334155",
        "color": "#F1F5F9",
        "border_radius": "0.5rem",
    },
    "label_style": {"color": "#CBD5E1"},
}


def sector_heatmap() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Sector Performance Heatmap", class_name="text-xl font-bold text-white"
            ),
            rx.el.div(
                rx.el.button(
                    "Gainers",
                    on_click=lambda: DashboardState.set_sector_sort("gainers"),
                    class_name=rx.cond(
                        DashboardState.sector_sort == "gainers",
                        "text-white",
                        "text-gray-400",
                    )
                    + " text-sm",
                ),
                rx.el.button(
                    "Losers",
                    on_click=lambda: DashboardState.set_sector_sort("losers"),
                    class_name=rx.cond(
                        DashboardState.sector_sort == "losers",
                        "text-white",
                        "text-gray-400",
                    )
                    + " text-sm",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.div(
            rx.foreach(
                DashboardState.sorted_sectors,
                lambda sector: rx.el.div(
                    rx.el.span(sector["name"], class_name="text-sm font-medium"),
                    rx.el.span(sector["change"], class_name="text-lg font-bold"),
                    class_name=rx.cond(
                        sector["change"].contains("+"),
                        "bg-green-500/20 text-green-300",
                        "bg-red-500/20 text-red-300",
                    )
                    + " flex flex-col items-center justify-center p-4 rounded-lg text-white aspect-square",
                ),
            ),
            class_name="grid grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-2",
        ),
        class_name="bg-gray-900 border border-gray-800 rounded-lg p-4 md:p-6",
    )


def market_breadth() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Market Breadth", class_name="text-xl font-bold text-white mb-4"),
        rx.el.div(
            rx.el.div(
                rx.el.span("Advancing", class_name="text-sm text-gray-400"),
                rx.el.span("1,850", class_name="text-2xl font-bold text-green-500"),
                class_name="flex flex-col items-center p-4 bg-gray-900 border border-gray-800 rounded-lg",
            ),
            rx.el.div(
                rx.el.span("Declining", class_name="text-sm text-gray-400"),
                rx.el.span("1,230", class_name="text-2xl font-bold text-red-500"),
                class_name="flex flex-col items-center p-4 bg-gray-900 border border-gray-800 rounded-lg",
            ),
            rx.el.div(
                rx.el.span("New Highs", class_name="text-sm text-gray-400"),
                rx.el.span("152", class_name="text-2xl font-bold text-white"),
                class_name="flex flex-col items-center p-4 bg-gray-900 border border-gray-800 rounded-lg",
            ),
            rx.el.div(
                rx.el.span("New Lows", class_name="text-sm text-gray-400"),
                rx.el.span("48", class_name="text-2xl font-bold text-white"),
                class_name="flex flex-col items-center p-4 bg-gray-900 border border-gray-800 rounded-lg",
            ),
            class_name="grid grid-cols-2 md:grid-cols-4 gap-4",
        ),
        class_name="bg-gray-900 border border-gray-800 rounded-lg p-4 md:p-6",
    )


def currency_widget() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2("Currency Exchange", class_name="text-xl font-bold text-white"),
            rx.el.select(
                rx.foreach(
                    DashboardState.currency_pairs,
                    lambda pair: rx.el.option(pair["pair"], value=pair["pair"]),
                ),
                on_change=DashboardState.set_currency_pair,
                value=DashboardState.selected_currency_pair,
                class_name="bg-gray-800 border border-gray-700 text-white rounded-md p-1",
            ),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.recharts.line_chart(
            rx.recharts.cartesian_grid(
                vertical=False, stroke_dasharray="3 3", stroke="#374151"
            ),
            rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
            rx.recharts.x_axis(
                data_key="date", stroke="#9CA3AF", tick_line=False, axis_line=False
            ),
            rx.recharts.y_axis(
                orientation="right",
                stroke="#9CA3AF",
                tick_line=False,
                axis_line=False,
                domain=["auto", "auto"],
            ),
            rx.recharts.line(
                data_key="value",
                type_="monotone",
                stroke="#3b82f6",
                stroke_width=2,
                dot=False,
            ),
            data=DashboardState.currency_data,
            height=200,
            width="100%",
        ),
        class_name="bg-gray-900 border border-gray-800 rounded-lg p-4 md:p-6",
    )


def commodities_widget() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Commodities", class_name="text-xl font-bold text-white mb-4"),
        rx.el.div(
            rx.foreach(
                DashboardState.commodities,
                lambda c: rx.el.div(
                    rx.el.span(c["name"], class_name="font-medium"),
                    rx.el.div(
                        rx.el.span(c["price"], class_name="font-bold"),
                        rx.el.span(
                            c["change"],
                            class_name=rx.cond(
                                c["change"].contains("+"),
                                "text-green-500",
                                "text-red-500",
                            )
                            + " text-sm",
                        ),
                        class_name="flex items-baseline gap-2",
                    ),
                    class_name="flex items-center justify-between p-3 bg-gray-800/50 rounded-lg",
                ),
            ),
            class_name="grid grid-cols-2 md:grid-cols-3 gap-4",
        ),
        class_name="bg-gray-900 border border-gray-800 rounded-lg p-4 md:p-6",
    )


def economic_calendar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2("Economic Calendar", class_name="text-xl font-bold text-white"),
            rx.el.div(
                rx.foreach(
                    ["all", "high", "medium", "low"],
                    lambda f: rx.el.button(
                        f.capitalize(),
                        on_click=lambda: DashboardState.set_calendar_filter(f),
                        class_name=rx.cond(
                            DashboardState.calendar_filter == f,
                            "text-white bg-gray-700",
                            "text-gray-400 hover:text-white",
                        )
                        + " px-3 py-1 text-sm rounded-md",
                    ),
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    rx.el.th(
                        "Date", class_name="text-left font-medium text-gray-400 p-2"
                    ),
                    rx.el.th(
                        "Time", class_name="text-left font-medium text-gray-400 p-2"
                    ),
                    rx.el.th(
                        "Country", class_name="text-left font-medium text-gray-400 p-2"
                    ),
                    rx.el.th(
                        "Event", class_name="text-left font-medium text-gray-400 p-2"
                    ),
                    rx.el.th(
                        "Impact", class_name="text-left font-medium text-gray-400 p-2"
                    ),
                )
            ),
            rx.el.tbody(
                rx.foreach(
                    DashboardState.filtered_events,
                    lambda event: rx.el.tr(
                        rx.el.td(event["date"], class_name="p-2"),
                        rx.el.td(event["time"], class_name="p-2"),
                        rx.el.td(event["country"], class_name="p-2"),
                        rx.el.td(event["event"], class_name="p-2"),
                        rx.el.td(
                            rx.el.span(
                                event["impact"],
                                class_name=rx.match(
                                    event["impact"],
                                    (
                                        "High",
                                        "bg-red-500/20 text-red-300 px-2 py-1 text-xs font-semibold rounded-full w-fit",
                                    ),
                                    (
                                        "Medium",
                                        "bg-yellow-500/20 text-yellow-300 px-2 py-1 text-xs font-semibold rounded-full w-fit",
                                    ),
                                    (
                                        "Low",
                                        "bg-green-500/20 text-green-300 px-2 py-1 text-xs font-semibold rounded-full w-fit",
                                    ),
                                    "bg-gray-500/20 text-gray-300 px-2 py-1 text-xs font-semibold rounded-full w-fit",
                                ),
                            ),
                            class_name="p-2",
                        ),
                    ),
                )
            ),
            class_name="w-full table-auto",
        ),
        class_name="bg-gray-900 border border-gray-800 rounded-lg p-4 md:p-6 overflow-x-auto",
    )


def analytics_page() -> rx.Component:
    return rx.el.div(
        header(),
        rx.el.div(
            rx.el.main(
                rx.el.div(
                    sector_heatmap(),
                    market_breadth(),
                    rx.el.div(
                        currency_widget(),
                        commodities_widget(),
                        class_name="grid md:grid-cols-2 gap-6",
                    ),
                    economic_calendar(),
                    class_name="grid gap-6",
                ),
                class_name="flex-1 p-4 md:p-6",
            ),
            class_name="flex",
        ),
        class_name="min-h-screen bg-gray-950 text-gray-50 font-['Inter']",
    )