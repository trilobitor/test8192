import reflex as rx
from app.states.portfolio_state import PortfolioState


def portfolio_performance_chart() -> rx.Component:
    """Portfolio performance chart showing value over time."""
    return rx.el.div(
        rx.el.h3(
            "Portfolio Performance",
            class_name="text-lg font-semibold text-white mb-4",
        ),
        rx.recharts.area_chart(
            rx.recharts.area(
                data_key="total_value",
                stroke="#3b82f6",
                fill="url(#colorValue)",
                stroke_width=2,
            ),
            rx.recharts.x_axis(
                data_key="date",
                stroke="#6b7280",
                tick={"fill": "#9ca3af", "fontSize": 12},
            ),
            rx.recharts.y_axis(
                stroke="#6b7280",
                tick={"fill": "#9ca3af", "fontSize": 12},
                domain=["dataMin - 1000", "dataMax + 1000"],
            ),
            rx.recharts.cartesian_grid(
                stroke_dasharray="3 3",
                stroke="#374151",
            ),
            rx.recharts.graphing_tooltip(
                content_style={
                    "backgroundColor": "#1f2937",
                    "border": "1px solid #374151",
                    "borderRadius": "0.5rem",
                    "color": "#fff",
                },
                label_style={"color": "#9ca3af"},
            ),
            rx.html(
                """
                <defs>
                    <linearGradient id="colorValue" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#3b82f6" stopOpacity="0.8"/>
                        <stop offset="95%" stopColor="#3b82f6" stopOpacity="0.1"/>
                    </linearGradient>
                </defs>
                """
            ),
            data=PortfolioState.performance_data,
            width="100%",
            height=300,
        ),
        class_name="bg-gray-900 border border-gray-800 rounded-lg p-6 mb-6",
    )


def portfolio_gains_chart() -> rx.Component:
    """Chart showing gains/losses over time."""
    return rx.el.div(
        rx.el.h3(
            "Gains & Losses",
            class_name="text-lg font-semibold text-white mb-4",
        ),
        rx.recharts.bar_chart(
            rx.recharts.bar(
                data_key="gain_loss",
                fill="#10b981",
                radius=[8, 8, 0, 0],
            ),
            rx.recharts.x_axis(
                data_key="date",
                stroke="#6b7280",
                tick={"fill": "#9ca3af", "fontSize": 12},
            ),
            rx.recharts.y_axis(
                stroke="#6b7280",
                tick={"fill": "#9ca3af", "fontSize": 12},
            ),
            rx.recharts.cartesian_grid(
                stroke_dasharray="3 3",
                stroke="#374151",
            ),
            rx.recharts.graphing_tooltip(
                content_style={
                    "backgroundColor": "#1f2937",
                    "border": "1px solid #374151",
                    "borderRadius": "0.5rem",
                    "color": "#fff",
                },
                label_style={"color": "#9ca3af"},
            ),
            data=PortfolioState.performance_data,
            width="100%",
            height=250,
        ),
        class_name="bg-gray-900 border border-gray-800 rounded-lg p-6 mb-6",
    )
