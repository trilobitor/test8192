import reflex as rx
from app.states.dashboard_state import DashboardState, SectorPerformanceData


def sector_card(sector: SectorPerformanceData) -> rx.Component:
    return rx.el.div(
        rx.el.span(sector["name"], class_name="text-sm font-medium text-white"),
        rx.el.span(
            sector["change"],
            class_name=rx.cond(
                sector["change"].contains("+"), "text-green-500", "text-red-500"
            )
            + " text-sm font-semibold",
        ),
        class_name="flex items-center justify-between p-3 bg-gray-900 border border-gray-800 rounded-lg hover:bg-gray-800/50 transition-colors",
    )


def sector_performance_grid() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Sector Performance", class_name="text-xl font-bold text-white mb-4"),
        rx.el.div(
            rx.foreach(DashboardState.sectors, sector_card),
            class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4",
        ),
        class_name="bg-gray-900 border border-gray-800 rounded-lg p-4 md:p-6",
    )