# 📊 Data Collection & Automated Testing Project

## 📖 Overview
This project is designed to **collect financial and news data**, process it, and run automated tests using **pytest** and **GitHub Actions**.  
It gathers **stock market data, currency exchange rates, and news articles** using a combination of APIs and web scraping techniques.

---

## 📈 **Data Sources & Collection Methods**

### ✅ **1. Stock Market Data (Alpha Vantage API)**
- Retrieves **historical monthly adjusted stock data** for **Galp Energia (Ticker: `GALP.LS`)**.
- Uses **Alpha Vantage API** to access stock market data.
- The function `fetch_monthly_adjusted_data()` processes the API response into a **structured Pandas DataFrame**.

### ✅ **2. News Scraping (Lusa.pt)**
- **Web Scraping** with **Selenium** to extract **daily news articles from Lusa.pt** related to **Galp Energia**.
- The function `scrape_lusa_with_selenium()` searches for relevant articles and stores them in a CSV file.

### ✅ **3. Currency Exchange Rate (EUR → USD)**
- Uses **BeautifulSoup** to scrape the exchange rate from [x-rates.com](https://www.x-rates.com).
- The function `fetch_eur_to_usd_rate()` extracts the **EUR to USD** exchange rate and timestamps it.

---

## 🛠️ Tech Stack
- **Python 3.9+**
- **pytest** (Testing framework)
- **Selenium** (Web scraping with browser automation)
- **BeautifulSoup** (Web scraping for exchange rates)
- **Alpha Vantage API** (Stock market data)
- **GitHub Actions** (Automated testing with CI/CD)

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
