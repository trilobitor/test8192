import reflex as rx
from app.states.portfolio_state import PortfolioState, PortfolioHolding, Transaction
from app.components.portfolio_chart import (
    portfolio_performance_chart,
    portfolio_gains_chart,
)
from app.components.preferences_dialog import preferences_dialog, export_buttons


def portfolio_summary_card() -> rx.Component:
    """Portfolio summary showing total value and gains."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h3("Portfolio Value", class_name="text-sm font-medium text-gray-400"),
                rx.el.p(
                    f"${PortfolioState.total_portfolio_value:,.2f}",
                    class_name="text-3xl font-bold text-white mt-1",
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.h3("Total Gain/Loss", class_name="text-sm font-medium text-gray-400"),
                rx.el.div(
                    rx.el.span(
                        f"${PortfolioState.total_gain_loss:,.2f}",
                        class_name=rx.cond(
                            PortfolioState.total_gain_loss >= 0,
                            "text-2xl font-bold text-green-500",
                            "text-2xl font-bold text-red-500",
                        ),
                    ),
                    rx.el.span(
                        f" ({PortfolioState.total_gain_loss_percent:+.2f}%)",
                        class_name=rx.cond(
                            PortfolioState.total_gain_loss >= 0,
                            "text-lg font-semibold text-green-500 ml-2",
                            "text-lg font-semibold text-red-500 ml-2",
                        ),
                    ),
                    class_name="flex items-baseline mt-1",
                ),
                class_name="flex-1",
            ),
            class_name="flex gap-8",
        ),
        class_name="bg-gray-900 border border-gray-800 rounded-lg p-6 mb-6",
    )


def holding_row(holding: PortfolioHolding) -> rx.Component:
    """Single row in holdings table."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    holding["symbol"],
                    class_name="font-semibold text-white text-base",
                ),
                rx.el.span(
                    holding["name"],
                    class_name="text-sm text-gray-400",
                ),
                class_name="flex flex-col",
            ),
            class_name="flex-1",
        ),
        rx.el.div(
            f"{holding['shares']:.2f}",
            class_name="w-24 text-right text-gray-300",
        ),
        rx.el.div(
            f"${holding['avg_buy_price']:.2f}",
            class_name="w-32 text-right text-gray-300",
        ),
        rx.el.div(
            f"${holding['current_price']:.2f}",
            class_name="w-32 text-right text-white font-semibold",
        ),
        rx.el.div(
            f"${holding['total_value']:,.2f}",
            class_name="w-36 text-right text-white font-semibold",
        ),
        rx.el.div(
            rx.el.div(
                f"${holding['gain_loss']:,.2f}",
                class_name=rx.cond(
                    holding["gain_loss"] >= 0,
                    "text-green-500 font-semibold",
                    "text-red-500 font-semibold",
                ),
            ),
            rx.el.div(
                f"({holding['gain_loss_percent']:+.2f}%)",
                class_name=rx.cond(
                    holding["gain_loss"] >= 0,
                    "text-green-500 text-sm",
                    "text-red-500 text-sm",
                ),
            ),
            class_name="w-36 text-right",
        ),
        class_name="flex items-center gap-4 p-4 hover:bg-gray-800/50 border-b border-gray-800 last:border-b-0",
    )


def holdings_table() -> rx.Component:
    """Table showing all portfolio holdings."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2("Holdings", class_name="text-xl font-bold text-white"),
                rx.el.button(
                    rx.icon("plus", class_name="h-4 w-4 mr-2"),
                    "Add Transaction",
                    on_click=lambda: PortfolioState.set_show_add_transaction_dialog(True),
                    class_name="flex items-center bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 text-sm font-medium",
                ),
                class_name="flex items-center justify-between mb-4",
            ),
            rx.el.div(
                # Header
                rx.el.div(
                    rx.el.div("Stock", class_name="flex-1 text-gray-400 text-sm font-medium"),
                    rx.el.div("Shares", class_name="w-24 text-right text-gray-400 text-sm font-medium"),
                    rx.el.div("Avg Price", class_name="w-32 text-right text-gray-400 text-sm font-medium"),
                    rx.el.div("Current Price", class_name="w-32 text-right text-gray-400 text-sm font-medium"),
                    rx.el.div("Total Value", class_name="w-36 text-right text-gray-400 text-sm font-medium"),
                    rx.el.div("Gain/Loss", class_name="w-36 text-right text-gray-400 text-sm font-medium"),
                    class_name="flex items-center gap-4 p-4 border-b-2 border-gray-700",
                ),
                # Rows
                rx.foreach(PortfolioState.holdings, holding_row),
                class_name="bg-gray-900 border border-gray-800 rounded-lg overflow-hidden",
            ),
        ),
        class_name="mb-6",
    )


def transaction_row(txn: Transaction) -> rx.Component:
    """Single row in transaction history."""
    return rx.el.div(
        rx.el.div(
            f"{txn['date']} {txn['time']}",
            class_name="w-40 text-gray-300 text-sm",
        ),
        rx.el.div(
            txn["type"].upper(),
            class_name=rx.cond(
                txn["type"] == "buy",
                "w-20 text-green-500 font-semibold text-sm uppercase",
                "w-20 text-red-500 font-semibold text-sm uppercase",
            ),
        ),
        rx.el.div(
            txn["symbol"],
            class_name="w-24 text-white font-semibold",
        ),
        rx.el.div(
            f"{txn['shares']:.2f}",
            class_name="w-24 text-right text-gray-300",
        ),
        rx.el.div(
            f"${txn['price']:.2f}",
            class_name="w-28 text-right text-gray-300",
        ),
        rx.el.div(
            f"${txn['total']:,.2f}",
            class_name="w-32 text-right text-white font-semibold",
        ),
        rx.el.div(
            f"${txn['fees']:.2f}",
            class_name="w-24 text-right text-gray-400 text-sm",
        ),
        class_name="flex items-center gap-4 p-3 hover:bg-gray-800/50 border-b border-gray-800 last:border-b-0",
    )


def transaction_history() -> rx.Component:
    """Transaction history table."""
    return rx.el.div(
        rx.el.div(
            rx.el.h2("Transaction History", class_name="text-xl font-bold text-white mb-4"),
            rx.el.div(
                # Header
                rx.el.div(
                    rx.el.div("Date & Time", class_name="w-40 text-gray-400 text-sm font-medium"),
                    rx.el.div("Type", class_name="w-20 text-gray-400 text-sm font-medium"),
                    rx.el.div("Symbol", class_name="w-24 text-gray-400 text-sm font-medium"),
                    rx.el.div("Shares", class_name="w-24 text-right text-gray-400 text-sm font-medium"),
                    rx.el.div("Price", class_name="w-28 text-right text-gray-400 text-sm font-medium"),
                    rx.el.div("Total", class_name="w-32 text-right text-gray-400 text-sm font-medium"),
                    rx.el.div("Fees", class_name="w-24 text-right text-gray-400 text-sm font-medium"),
                    class_name="flex items-center gap-4 p-3 border-b-2 border-gray-700",
                ),
                # Rows
                rx.foreach(PortfolioState.sorted_transactions, transaction_row),
                class_name="bg-gray-900 border border-gray-800 rounded-lg overflow-hidden max-h-96 overflow-y-auto",
            ),
        ),
        class_name="mb-6",
    )


def add_transaction_dialog() -> rx.Component:
    """Dialog for adding a new transaction."""
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(
                class_name="fixed inset-0 bg-black/50 backdrop-blur-sm z-40"
            ),
            rx.radix.primitives.dialog.content(
                rx.radix.primitives.dialog.title(
                    "Add Transaction", class_name="text-2xl font-bold text-white mb-4"
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "Transaction Type",
                            class_name="text-sm font-medium text-gray-300 mb-2 block",
                        ),
                        rx.el.div(
                            rx.el.button(
                                "Buy",
                                type="button",
                                on_click=lambda: PortfolioState.set_transaction_type("buy"),
                                class_name=rx.cond(
                                    PortfolioState.transaction_type == "buy",
                                    "flex-1 bg-green-600 text-white font-semibold py-2 rounded-md",
                                    "flex-1 bg-gray-700 text-gray-300 font-semibold py-2 rounded-md hover:bg-gray-600",
                                ),
                            ),
                            rx.el.button(
                                "Sell",
                                type="button",
                                on_click=lambda: PortfolioState.set_transaction_type("sell"),
                                class_name=rx.cond(
                                    PortfolioState.transaction_type == "sell",
                                    "flex-1 bg-red-600 text-white font-semibold py-2 rounded-md",
                                    "flex-1 bg-gray-700 text-gray-300 font-semibold py-2 rounded-md hover:bg-gray-600",
                                ),
                            ),
                            class_name="flex gap-2",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Stock Symbol",
                            class_name="text-sm font-medium text-gray-300 mb-1 block",
                        ),
                        rx.el.input(
                            name="symbol",
                            placeholder="e.g., AAPL",
                            required=True,
                            class_name="w-full bg-gray-800 border border-gray-700 rounded-md px-3 py-2 text-white focus:outline-none focus:ring-2 focus:ring-blue-500",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.label(
                                "Shares",
                                class_name="text-sm font-medium text-gray-300 mb-1 block",
                            ),
                            rx.el.input(
                                name="shares",
                                type="number",
                                step="0.01",
                                placeholder="10.00",
                                required=True,
                                class_name="w-full bg-gray-800 border border-gray-700 rounded-md px-3 py-2 text-white focus:outline-none focus:ring-2 focus:ring-blue-500",
                            ),
                            class_name="flex-1",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Price per Share",
                                class_name="text-sm font-medium text-gray-300 mb-1 block",
                            ),
                            rx.el.input(
                                name="price",
                                type="number",
                                step="0.01",
                                placeholder="150.00",
                                required=True,
                                class_name="w-full bg-gray-800 border border-gray-700 rounded-md px-3 py-2 text-white focus:outline-none focus:ring-2 focus:ring-blue-500",
                            ),
                            class_name="flex-1",
                        ),
                        class_name="flex gap-4 mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Transaction Fees",
                            class_name="text-sm font-medium text-gray-300 mb-1 block",
                        ),
                        rx.el.input(
                            name="fees",
                            type="number",
                            step="0.01",
                            placeholder="4.95",
                            value="4.95",
                            class_name="w-full bg-gray-800 border border-gray-700 rounded-md px-3 py-2 text-white focus:outline-none focus:ring-2 focus:ring-blue-500",
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Cancel",
                            type="button",
                            on_click=lambda: PortfolioState.set_show_add_transaction_dialog(
                                False
                            ),
                            class_name="flex-1 bg-gray-700 text-white font-semibold py-2 rounded-md hover:bg-gray-600",
                        ),
                        rx.el.button(
                            "Add Transaction",
                            type="submit",
                            class_name="flex-1 bg-blue-600 text-white font-semibold py-2 rounded-md hover:bg-blue-700",
                        ),
                        class_name="flex gap-3",
                    ),
                    on_submit=PortfolioState.add_transaction,
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
        open=PortfolioState.show_add_transaction_dialog,
        on_open_change=PortfolioState.set_show_add_transaction_dialog,
    )


def portfolio_page() -> rx.Component:
    """Main portfolio page."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Portfolio",
                    class_name="text-3xl font-bold text-white mb-2",
                ),
                rx.el.div(
                    rx.el.p(
                        "Track your investments and monitor performance",
                        class_name="text-gray-400",
                    ),
                    rx.el.div(
                        rx.el.button(
                            rx.icon("settings", class_name="h-4 w-4 mr-2"),
                            "Preferences",
                            on_click=lambda: PortfolioState.set_show_preferences_dialog(True),
                            class_name="flex items-center bg-gray-700 text-white px-4 py-2 rounded-md hover:bg-gray-600 text-sm font-medium",
                        ),
                        class_name="flex gap-3",
                    ),
                    class_name="flex items-center justify-between",
                ),
                class_name="mb-6",
            ),
            portfolio_summary_card(),
            rx.el.div(
                rx.el.div(
                    portfolio_performance_chart(),
                    portfolio_gains_chart(),
                    class_name="flex-1",
                ),
                rx.el.div(
                    export_buttons(),
                    class_name="w-80",
                ),
                class_name="flex gap-6 mb-6",
            ),
            holdings_table(),
            transaction_history(),
            add_transaction_dialog(),
            preferences_dialog(),
            class_name="max-w-7xl mx-auto",
        ),
        class_name="min-h-screen bg-gray-950 text-gray-50 p-6",
    )
