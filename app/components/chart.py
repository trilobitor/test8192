import reflex as rx
from app.states.dashboard_state import DashboardState

TOOLTIP_PROPS = {
    "content_style": {
        "background": "#1E293B",
        "border_color": "#334155",
        "color": "#F1F5F9",
        "border_radius": "0.5rem",
    },
    "label_style": {"color": "#CBD5E1"},
}


def chart_header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2("AAPL", class_name="text-2xl font-bold text-white"),
            rx.el.p("Apple Inc.", class_name="text-sm text-gray-400"),
            class_name="flex items-baseline gap-2",
        ),
        rx.el.div(
            rx.el.button(
                "Compare",
                on_click=DashboardState.toggle_comparison_mode,
                class_name=rx.cond(
                    DashboardState.comparison_mode,
                    "px-3 py-1 text-sm font-medium text-white bg-blue-600 rounded-md",
                    "px-3 py-1 text-sm font-medium text-gray-400 hover:text-white hover:bg-gray-800 rounded-md",
                ),
            ),
            rx.foreach(
                ["1D", "5D", "1M", "6M", "1Y", "5Y"],
                lambda item: rx.el.button(
                    item,
                    on_click=lambda: DashboardState.set_active_range(item),
                    class_name=rx.cond(
                        DashboardState.active_range == item,
                        "px-3 py-1 text-sm font-medium text-white bg-gray-700 rounded-md",
                        "px-3 py-1 text-sm font-medium text-gray-400 hover:text-white hover:bg-gray-800 rounded-md",
                    ),
                ),
            ),
            class_name="flex items-center gap-2",
        ),
        class_name="flex items-center justify-between",
    )


def stock_selector() -> rx.Component:
    return rx.el.div(
        rx.foreach(
            DashboardState.all_stocks,
            lambda stock: rx.el.div(
                rx.el.input(
                    type="checkbox",
                    checked=DashboardState.selected_stocks.contains(stock),
                    on_change=lambda _: DashboardState.toggle_stock_selection(stock),
                    class_name="h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-600 cursor-pointer",
                ),
                rx.el.label(
                    stock,
                    class_name="ml-2 text-sm font-medium text-white cursor-pointer",
                ),
                class_name="flex items-center",
            ),
        ),
        class_name="flex items-center gap-4 mt-4",
    )


def html_legend() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(class_name="w-3 h-3 rounded-full bg-blue-500"),
            rx.el.span("AAPL", class_name="text-sm text-gray-400"),
            class_name="flex items-center gap-2",
        ),
        rx.foreach(
            DashboardState.selected_stocks,
            lambda stock: rx.el.div(
                rx.el.div(
                    class_name=rx.cond(
                        stock == "MSFT",
                        "w-3 h-3 rounded-full bg-green-500",
                        "w-3 h-3 rounded-full bg-orange-500",
                    )
                ),
                rx.el.span(stock, class_name="text-sm text-gray-400"),
                class_name="flex items-center gap-2",
            ),
        ),
        class_name="flex items-center justify-center gap-4 mt-4",
    )


def stock_chart() -> rx.Component:
    return rx.el.div(
        chart_header(),
        rx.cond(DashboardState.comparison_mode, stock_selector(), rx.fragment()),
        rx.cond(
            DashboardState.comparison_mode,
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
                ),
                rx.recharts.line(
                    data_key="value",
                    type_="monotone",
                    stroke="#3b82f6",
                    stroke_width=2,
                    dot=False,
                    name="AAPL",
                ),
                rx.foreach(
                    DashboardState.selected_stocks,
                    lambda stock: rx.recharts.line(
                        data_key=stock,
                        type_="monotone",
                        stroke=rx.cond(stock == "MSFT", "#22c55e", "#f97316"),
                        stroke_width=2,
                        dot=False,
                        name=stock,
                    ),
                ),
                data=DashboardState.chart_data,
                height=400,
                width="100%",
                margin={"top": 20, "right": 20, "left": 20, "bottom": 20},
            ),
            rx.recharts.composed_chart(
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
                    y_axis_id="left",
                ),
                rx.recharts.y_axis(
                    orientation="left",
                    stroke="#9CA3AF",
                    tick_line=False,
                    axis_line=False,
                    y_axis_id="right",
                ),
                rx.recharts.area(
                    data_key="value",
                    type_="monotone",
                    stroke="#3b82f6",
                    fill="url(#chart-gradient)",
                    stroke_width=2,
                    y_axis_id="left",
                    dot=False,
                ),
                rx.recharts.bar(
                    data_key="volume", fill="#4f46e5", bar_size=5, y_axis_id="right"
                ),
                rx.recharts.brush(data_key="date", stroke="#6b7280", fill="#1f2937"),
                data=DashboardState.chart_data,
                height=400,
                width="100%",
                margin={"top": 20, "right": 20, "left": 20, "bottom": 20},
            ),
        ),
        rx.cond(DashboardState.comparison_mode, html_legend(), rx.fragment()),
        rx.el.svg(
            rx.el.defs(
                rx.el.linear_gradient(
                    rx.el.stop(offset="5%", stop_color="#3b82f6", stop_opacity=0.8),
                    rx.el.stop(offset="95%", stop_color="#3b82f6", stop_opacity=0),
                    id="chart-gradient",
                    x1="0",
                    y1="0",
                    x2="0",
                    y2="1",
                )
            ),
            class_name="h-0 w-0 absolute",
        ),
        class_name="relative bg-gray-900 border border-gray-800 rounded-lg p-4 md:p-6",
    )