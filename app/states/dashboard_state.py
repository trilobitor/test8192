import reflex as rx
from typing import TypedDict, Literal


class Ticker(TypedDict):
    symbol: str
    price: str
    change: str


class ChartData(TypedDict):
    date: str
    value: float
    volume: int
    MSFT: float
    GOOGL: float


class NewsArticle(TypedDict):
    title: str
    source: str
    snippet: str
    time: str
    thumbnail: str
    category: str


class WatchlistItem(TypedDict):
    symbol: str
    price: str
    change: str
    change_percent: str


class MarketMover(TypedDict):
    symbol: str
    name: str
    price: str
    change: str
    change_percent: str


class StockDetail(TypedDict):
    symbol: str
    name: str
    price: str
    change: str
    change_percent: str
    market_cap: str
    volume: str
    high_52wk: str
    low_52wk: str
    pe_ratio: str | None


class SectorPerformanceData(TypedDict):
    name: str
    change: str


class CurrencyPair(TypedDict):
    pair: str
    price: str
    change: str


class Commodity(TypedDict):
    name: str
    price: str
    change: str


class EconomicEvent(TypedDict):
    date: str
    time: str
    country: str
    event: str
    impact: Literal["High", "Medium", "Low"]


class DashboardState(rx.State):
    tickers: list[Ticker] = [
        {"symbol": "S&P 500", "price": "4,510.32", "change": "+25.18 (+0.56%)"},
        {"symbol": "NASDAQ", "price": "14,120.75", "change": "+112.43 (+0.80%)"},
        {"symbol": "DOW JONES", "price": "35,300.12", "change": "-50.67 (-0.14%)"},
        {"symbol": "RUSSELL 2000", "price": "1,890.55", "change": "+15.22 (+0.81%)"},
        {"symbol": "FTSE 100", "price": "7,650.98", "change": "+30.11 (+0.39%)"},
        {"symbol": "NIKKEI 225", "price": "33,450.78", "change": "-150.23 (-0.45%)"},
        {"symbol": "BITCOIN", "price": "$43,567.89", "change": "+1,234.56 (+2.91%)"},
        {"symbol": "ETHEREUM", "price": "$2,345.67", "change": "+88.12 (+3.90%)"},
        {"symbol": "GOLD", "price": "$2,030.50", "change": "-5.25 (-0.26%)"},
        {"symbol": "SILVER", "price": "$24.15", "change": "+0.18 (+0.75%)"},
    ]
    active_range: str = "1D"
    chart_data: list[ChartData] = [
        {
            "date": "2023-01-01",
            "value": 150.0,
            "volume": 10000,
            "MSFT": 300.0,
            "GOOGL": 2800.0,
        },
        {
            "date": "2023-01-02",
            "value": 152.5,
            "volume": 12000,
            "MSFT": 302.5,
            "GOOGL": 2825.0,
        },
        {
            "date": "2023-01-03",
            "value": 151.8,
            "volume": 11000,
            "MSFT": 301.8,
            "GOOGL": 2818.0,
        },
        {
            "date": "2023-01-04",
            "value": 155.2,
            "volume": 15000,
            "MSFT": 305.2,
            "GOOGL": 2852.0,
        },
        {
            "date": "2023-01-05",
            "value": 154.75,
            "volume": 14000,
            "MSFT": 304.75,
            "GOOGL": 2847.5,
        },
        {
            "date": "2023-01-06",
            "value": 157.9,
            "volume": 16000,
            "MSFT": 307.9,
            "GOOGL": 2879.0,
        },
        {
            "date": "2023-01-07",
            "value": 156.8,
            "volume": 13000,
            "MSFT": 306.8,
            "GOOGL": 2868.0,
        },
        {
            "date": "2023-01-08",
            "value": 158.3,
            "volume": 17000,
            "MSFT": 308.3,
            "GOOGL": 2883.0,
        },
        {
            "date": "2023-01-09",
            "value": 160.1,
            "volume": 18000,
            "MSFT": 310.1,
            "GOOGL": 2901.0,
        },
        {
            "date": "2023-01-10",
            "value": 159.5,
            "volume": 17500,
            "MSFT": 309.5,
            "GOOGL": 2895.0,
        },
    ]
    comparison_mode: bool = False
    all_stocks: list[str] = ["MSFT", "GOOGL", "AMZN", "TSLA"]
    selected_stocks: list[str] = []
    market_status: str = "Market Open"
    is_market_open: bool = True
    news: list[NewsArticle] = [
        {
            "title": "Fed holds interest rates steady, signals potential cuts in 2024",
            "source": "Reuters",
            "snippet": "The Federal Reserve kept interest rates unchanged on Wednesday and signaled it is still leaning towards eventual reductions...",
            "time": "25m ago",
            "thumbnail": "/placeholder.svg",
            "category": "Economics",
        },
        {
            "title": "Tech stocks rally on strong earnings reports from chipmakers",
            "source": "Bloomberg",
            "snippet": "Shares of major semiconductor companies surged after posting quarterly results that beat Wall Street expectations...",
            "time": "1h ago",
            "thumbnail": "/placeholder.svg",
            "category": "Technology",
        },
        {
            "title": "Oil prices slide as inventories rise more than expected",
            "source": "WSJ",
            "snippet": "Crude futures fell sharply after the EIA reported a larger-than-expected build in U.S. crude stockpiles.",
            "time": "3h ago",
            "thumbnail": "/placeholder.svg",
            "category": "Commodities",
        },
        {
            "title": "EV maker announces record delivery numbers for Q4",
            "source": "CNBC",
            "snippet": "The electric vehicle manufacturer surpassed analyst estimates for fourth-quarter deliveries, sending its stock price soaring.",
            "time": "5h ago",
            "thumbnail": "/placeholder.svg",
            "category": "Technology",
        },
    ]
    active_news_filter: str = "latest"
    watchlist: list[WatchlistItem] = [
        {
            "symbol": "AAPL",
            "price": "172.25",
            "change": "+1.50",
            "change_percent": "+0.88%",
        },
        {
            "symbol": "NVDA",
            "price": "875.28",
            "change": "-2.20",
            "change_percent": "-0.25%",
        },
    ]
    market_movers: list[MarketMover] = [
        {
            "symbol": "UPST",
            "name": "Upstart Holdings",
            "price": "25.50",
            "change": "+3.45",
            "change_percent": "+15.65%",
        },
        {
            "symbol": "RIVN",
            "name": "Rivian Automotive",
            "price": "10.20",
            "change": "-1.80",
            "change_percent": "-15.00%",
        },
        {
            "symbol": "PLTR",
            "name": "Palantir Technologies",
            "price": "23.80",
            "change": "+2.10",
            "change_percent": "+9.68%",
        },
        {
            "symbol": "SOFI",
            "name": "SoFi Technologies",
            "price": "7.30",
            "change": "-0.55",
            "change_percent": "-7.01%",
        },
    ]
    movers_sort: Literal["gainers", "losers"] = "gainers"
    stock_search_query: str = ""
    show_stock_detail: bool = False
    selected_stock_detail: StockDetail | None = None

    @rx.event
    def set_active_range(self, new_range: str):
        self.active_range = new_range

    @rx.event
    def toggle_comparison_mode(self):
        self.comparison_mode = not self.comparison_mode
        if not self.comparison_mode:
            self.selected_stocks = []

    @rx.event
    def toggle_stock_selection(self, stock_symbol: str):
        if stock_symbol in self.selected_stocks:
            self.selected_stocks.remove(stock_symbol)
        else:
            self.selected_stocks.append(stock_symbol)

    @rx.event
    def set_news_filter(self, new_filter: str):
        self.active_news_filter = new_filter

    @rx.event
    def add_to_watchlist(self, stock_symbol: str):
        if not any((item["symbol"] == stock_symbol for item in self.watchlist)):
            new_item = {
                "symbol": stock_symbol,
                "price": "100.00",
                "change": "+1.00",
                "change_percent": "+1.00%",
            }
            self.watchlist.append(new_item)

    @rx.event
    def remove_from_watchlist(self, stock_symbol: str):
        self.watchlist = [
            item for item in self.watchlist if item["symbol"] != stock_symbol
        ]

    @rx.var
    def filtered_stocks(self) -> list[str]:
        if not self.stock_search_query:
            return []
        return [
            s for s in self.all_stocks if self.stock_search_query.lower() in s.lower()
        ]

    @rx.event
    def open_stock_detail(self, stock_symbol: str):
        self.selected_stock_detail = {
            "symbol": stock_symbol,
            "name": f"{stock_symbol} Inc.",
            "price": "172.25",
            "change": "+1.50",
            "change_percent": "+0.88%",
            "market_cap": "$2.8T",
            "volume": "50M",
            "high_52wk": "198.23",
            "low_52wk": "124.17",
            "pe_ratio": "28.5",
        }
        self.show_stock_detail = True

    @rx.event
    def close_stock_detail(self):
        self.show_stock_detail = False
        self.selected_stock_detail = None

    @rx.event
    def set_movers_sort(self, sort_type: Literal["gainers", "losers"]):
        self.movers_sort = sort_type

    @rx.var
    def sorted_movers(self) -> list[MarketMover]:
        if self.movers_sort == "gainers":
            return sorted(
                [m for m in self.market_movers if m["change"].startswith("+")],
                key=lambda x: float(x["change_percent"][:-1]),
                reverse=True,
            )
        else:
            return sorted(
                [m for m in self.market_movers if m["change"].startswith("-")],
                key=lambda x: float(x["change_percent"][:-1]),
            )

    sectors: list[SectorPerformanceData] = [
        {"name": "Technology", "change": "+1.2%"},
        {"name": "Healthcare", "change": "-0.5%"},
        {"name": "Financials", "change": "+0.8%"},
        {"name": "Consumer Discretionary", "change": "+1.5%"},
        {"name": "Communication Services", "change": "+0.9%"},
        {"name": "Industrials", "change": "-0.2%"},
        {"name": "Consumer Staples", "change": "-0.1%"},
        {"name": "Energy", "change": "+2.1%"},
        {"name": "Utilities", "change": "-0.7%"},
        {"name": "Real Estate", "change": "+0.3%"},
        {"name": "Materials", "change": "-0.4%"},
    ]
    sector_sort: Literal["gainers", "losers"] = "gainers"
    currency_pairs: list[CurrencyPair] = [
        {"pair": "EUR/USD", "price": "1.0850", "change": "-0.0015"},
        {"pair": "GBP/USD", "price": "1.2720", "change": "+0.0030"},
        {"pair": "USD/JPY", "price": "148.50", "change": "+1.20"},
        {"pair": "USD/CHF", "price": "0.8650", "change": "-0.0025"},
        {"pair": "AUD/USD", "price": "0.6580", "change": "+0.0010"},
    ]
    selected_currency_pair: str = "EUR/USD"
    commodities: list[Commodity] = [
        {"name": "Gold", "price": "$2,030.50", "change": "-5.25"},
        {"name": "Silver", "price": "$24.15", "change": "+0.18"},
        {"name": "WTI Oil", "price": "$78.50", "change": "+1.20"},
        {"name": "Brent Oil", "price": "$82.80", "change": "+1.10"},
        {"name": "Natural Gas", "price": "$2.75", "change": "-0.05"},
        {"name": "Copper", "price": "$3.85", "change": "+0.02"},
    ]
    economic_events: list[EconomicEvent] = [
        {
            "date": "2024-03-15",
            "time": "08:30",
            "country": "USA",
            "event": "Retail Sales MoM",
            "impact": "High",
        },
        {
            "date": "2024-03-15",
            "time": "10:00",
            "country": "USA",
            "event": "Consumer Sentiment",
            "impact": "Medium",
        },
        {
            "date": "2024-03-16",
            "time": "04:30",
            "country": "EUR",
            "event": "ECB President Speaks",
            "impact": "High",
        },
        {
            "date": "2024-03-17",
            "time": "21:00",
            "country": "CHN",
            "event": "Industrial Production YoY",
            "impact": "Medium",
        },
        {
            "date": "2024-03-18",
            "time": "09:00",
            "country": "GER",
            "event": "ZEW Economic Sentiment",
            "impact": "Low",
        },
    ]
    calendar_filter: Literal["all", "high", "medium", "low"] = "all"

    @rx.event
    def set_sector_sort(self, sort_type: Literal["gainers", "losers"]):
        self.sector_sort = sort_type

    @rx.var
    def sorted_sectors(self) -> list[SectorPerformanceData]:
        if self.sector_sort == "gainers":
            return sorted(
                [s for s in self.sectors if s["change"].startswith("+")],
                key=lambda x: float(x["change"].replace("+", "").replace("%", "")),
                reverse=True,
            )
        else:
            return sorted(
                [s for s in self.sectors if s["change"].startswith("-")],
                key=lambda x: float(x["change"].replace("-", "").replace("%", "")),
            )

    @rx.event
    def set_currency_pair(self, pair: str):
        self.selected_currency_pair = pair

    @rx.var
    def currency_data(self) -> list[ChartData]:
        return [
            {
                "date": f"Day {i}",
                "value": 1.085 + i * 0.001,
                "volume": 0,
                "MSFT": 0,
                "GOOGL": 0,
            }
            for i in range(10)
        ]

    @rx.event
    def set_calendar_filter(self, filter_type: Literal["all", "high", "medium", "low"]):
        self.calendar_filter = filter_type

    @rx.var
    def filtered_events(self) -> list[EconomicEvent]:
        if self.calendar_filter == "all":
            return self.economic_events
        return [
            e
            for e in self.economic_events
            if e["impact"].lower() == self.calendar_filter
        ]