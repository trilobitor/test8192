import reflex as rx
from typing import TypedDict, Literal
from datetime import datetime


class PortfolioHolding(TypedDict):
    symbol: str
    name: str
    shares: float
    avg_buy_price: float
    current_price: float
    total_value: float
    gain_loss: float
    gain_loss_percent: float


class Transaction(TypedDict):
    id: str
    date: str
    time: str
    type: Literal["buy", "sell"]
    symbol: str
    shares: float
    price: float
    total: float
    fees: float


class PortfolioPerformance(TypedDict):
    date: str
    total_value: float
    gain_loss: float


class UserPreferences(TypedDict):
    theme: Literal["dark", "light"]
    default_view: Literal["markets", "portfolio", "analytics"]
    notifications_enabled: bool
    email_alerts: bool
    price_alerts_enabled: bool


class PortfolioState(rx.State):
    # Portfolio holdings
    holdings: list[PortfolioHolding] = [
        {
            "symbol": "AAPL",
            "name": "Apple Inc.",
            "shares": 50.0,
            "avg_buy_price": 150.00,
            "current_price": 172.25,
            "total_value": 8612.50,
            "gain_loss": 1112.50,
            "gain_loss_percent": 14.83,
        },
        {
            "symbol": "MSFT",
            "name": "Microsoft Corp.",
            "shares": 30.0,
            "avg_buy_price": 320.00,
            "current_price": 378.50,
            "total_value": 11355.00,
            "gain_loss": 1755.00,
            "gain_loss_percent": 18.28,
        },
        {
            "symbol": "GOOGL",
            "name": "Alphabet Inc.",
            "shares": 25.0,
            "avg_buy_price": 130.00,
            "current_price": 142.80,
            "total_value": 3570.00,
            "gain_loss": 320.00,
            "gain_loss_percent": 9.85,
        },
        {
            "symbol": "NVDA",
            "name": "NVIDIA Corp.",
            "shares": 15.0,
            "avg_buy_price": 450.00,
            "current_price": 875.28,
            "total_value": 13129.20,
            "gain_loss": 6379.20,
            "gain_loss_percent": 94.43,
        },
    ]

    # Transaction history
    transactions: list[Transaction] = [
        {
            "id": "txn_001",
            "date": "2024-01-15",
            "time": "09:30",
            "type": "buy",
            "symbol": "AAPL",
            "shares": 50.0,
            "price": 150.00,
            "total": 7500.00,
            "fees": 4.95,
        },
        {
            "id": "txn_002",
            "date": "2024-02-10",
            "time": "10:15",
            "type": "buy",
            "symbol": "MSFT",
            "shares": 30.0,
            "price": 320.00,
            "total": 9600.00,
            "fees": 4.95,
        },
        {
            "id": "txn_003",
            "date": "2024-02-20",
            "time": "14:20",
            "type": "buy",
            "symbol": "GOOGL",
            "shares": 25.0,
            "price": 130.00,
            "total": 3250.00,
            "fees": 4.95,
        },
        {
            "id": "txn_004",
            "date": "2024-03-05",
            "time": "11:45",
            "type": "buy",
            "symbol": "NVDA",
            "shares": 15.0,
            "price": 450.00,
            "total": 6750.00,
            "fees": 4.95,
        },
    ]

    # Portfolio performance over time
    performance_data: list[PortfolioPerformance] = [
        {"date": "2024-01-15", "total_value": 27100.00, "gain_loss": 0.00},
        {"date": "2024-01-30", "total_value": 27850.00, "gain_loss": 750.00},
        {"date": "2024-02-15", "total_value": 28920.00, "gain_loss": 1820.00},
        {"date": "2024-02-28", "total_value": 30150.00, "gain_loss": 3050.00},
        {"date": "2024-03-15", "total_value": 31800.00, "gain_loss": 4700.00},
        {"date": "2024-03-31", "total_value": 33450.00, "gain_loss": 6350.00},
        {"date": "2024-04-15", "total_value": 34200.00, "gain_loss": 7100.00},
        {"date": "2024-04-30", "total_value": 35100.00, "gain_loss": 8000.00},
        {"date": "2024-05-15", "total_value": 35850.00, "gain_loss": 8750.00},
        {"date": "2024-05-31", "total_value": 36666.70, "gain_loss": 9566.70},
    ]

    # User preferences
    user_preferences: UserPreferences = {
        "theme": "dark",
        "default_view": "markets",
        "notifications_enabled": True,
        "email_alerts": False,
        "price_alerts_enabled": True,
    }

    # UI state
    show_add_transaction_dialog: bool = False
    show_preferences_dialog: bool = False
    transaction_type: Literal["buy", "sell"] = "buy"
    selected_export_format: Literal["csv", "pdf"] = "csv"

    @rx.var
    def total_portfolio_value(self) -> float:
        """Calculate total portfolio value."""
        return sum(holding["total_value"] for holding in self.holdings)

    @rx.var
    def total_gain_loss(self) -> float:
        """Calculate total gain/loss."""
        return sum(holding["gain_loss"] for holding in self.holdings)

    @rx.var
    def total_gain_loss_percent(self) -> float:
        """Calculate total gain/loss percentage."""
        total_invested = sum(
            holding["shares"] * holding["avg_buy_price"] for holding in self.holdings
        )
        if total_invested == 0:
            return 0.0
        return (self.total_gain_loss / total_invested) * 100

    @rx.var
    def sorted_transactions(self) -> list[Transaction]:
        """Get transactions sorted by date (newest first)."""
        return sorted(
            self.transactions,
            key=lambda x: f"{x['date']} {x['time']}",
            reverse=True,
        )

    @rx.event
    def set_show_add_transaction_dialog(self, value: bool):
        """Toggle add transaction dialog."""
        self.show_add_transaction_dialog = value

    @rx.event
    def set_show_preferences_dialog(self, value: bool):
        """Toggle preferences dialog."""
        self.show_preferences_dialog = value

    @rx.event
    def set_transaction_type(self, txn_type: Literal["buy", "sell"]):
        """Set transaction type."""
        self.transaction_type = txn_type

    @rx.event
    def add_transaction(self, form_data: dict):
        """Add a new transaction."""
        new_transaction: Transaction = {
            "id": f"txn_{len(self.transactions) + 1:03d}",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M"),
            "type": self.transaction_type,
            "symbol": form_data.get("symbol", ""),
            "shares": float(form_data.get("shares", 0)),
            "price": float(form_data.get("price", 0)),
            "total": float(form_data.get("shares", 0)) * float(form_data.get("price", 0)),
            "fees": float(form_data.get("fees", 0)),
        }
        self.transactions.append(new_transaction)
        self.show_add_transaction_dialog = False
        self._update_holdings(new_transaction)

    def _update_holdings(self, transaction: Transaction):
        """Update holdings based on transaction."""
        symbol = transaction["symbol"]
        existing_holding = next(
            (h for h in self.holdings if h["symbol"] == symbol), None
        )

        if transaction["type"] == "buy":
            if existing_holding:
                # Update existing holding
                total_shares = existing_holding["shares"] + transaction["shares"]
                total_cost = (
                    existing_holding["shares"] * existing_holding["avg_buy_price"]
                    + transaction["shares"] * transaction["price"]
                )
                existing_holding["shares"] = total_shares
                existing_holding["avg_buy_price"] = total_cost / total_shares
                existing_holding["total_value"] = (
                    total_shares * existing_holding["current_price"]
                )
                existing_holding["gain_loss"] = (
                    existing_holding["total_value"] - total_cost
                )
                existing_holding["gain_loss_percent"] = (
                    (existing_holding["gain_loss"] / total_cost) * 100
                )
            else:
                # Add new holding
                new_holding: PortfolioHolding = {
                    "symbol": symbol,
                    "name": f"{symbol} Inc.",
                    "shares": transaction["shares"],
                    "avg_buy_price": transaction["price"],
                    "current_price": transaction["price"],
                    "total_value": transaction["total"],
                    "gain_loss": 0.0,
                    "gain_loss_percent": 0.0,
                }
                self.holdings.append(new_holding)
        elif transaction["type"] == "sell" and existing_holding:
            # Reduce shares
            existing_holding["shares"] -= transaction["shares"]
            if existing_holding["shares"] <= 0:
                self.holdings = [
                    h for h in self.holdings if h["symbol"] != symbol
                ]
            else:
                existing_holding["total_value"] = (
                    existing_holding["shares"] * existing_holding["current_price"]
                )
                total_cost = (
                    existing_holding["shares"] * existing_holding["avg_buy_price"]
                )
                existing_holding["gain_loss"] = (
                    existing_holding["total_value"] - total_cost
                )
                existing_holding["gain_loss_percent"] = (
                    (existing_holding["gain_loss"] / total_cost) * 100
                    if total_cost > 0
                    else 0.0
                )

    @rx.event
    def update_preference(self, key: str, value: str | bool):
        """Update user preference."""
        self.user_preferences[key] = value

    @rx.event
    def export_data(self, format: Literal["csv", "pdf"]):
        """Export portfolio data."""
        self.selected_export_format = format
        # In a real app, this would trigger file download
        # For now, we'll just log it
        print(f"Exporting portfolio data as {format}")

    @rx.event
    def save_preferences(self, form_data: dict):
        """Save user preferences."""
        self.user_preferences["theme"] = form_data.get("theme", "dark")
        self.user_preferences["default_view"] = form_data.get("default_view", "markets")
        self.user_preferences["notifications_enabled"] = form_data.get(
            "notifications_enabled", True
        )
        self.user_preferences["email_alerts"] = form_data.get("email_alerts", False)
        self.user_preferences["price_alerts_enabled"] = form_data.get(
            "price_alerts_enabled", True
        )
        self.show_preferences_dialog = False
