# 📊 Data Collection & Automated Testing Project  

## 📖 Overview  
This project automates **financial and news data collection**, processes it, and runs **automated tests** using **pytest** and **GitHub Actions**.  
It gathers **stock market data, currency exchange rates, and news articles** using APIs and web scraping techniques.  

The collected data is **stored in PostgreSQL**, transformed using **dbt**, and continuously tested through **CI/CD pipelines**.  

---

## 📈 Data Sources & Collection Methods  

### ✅ 1. Stock Market Data (Alpha Vantage API)  
- Retrieves **historical monthly adjusted stock data** for **Galp Energia (`GALP.LS`)**.  
- Uses **Alpha Vantage API** to access stock market data.  
- Processes API responses into a structured **Pandas DataFrame**.  
- Stores data in **PostgreSQL** via **SQLAlchemy**.  

### ✅ 2. News Scraping (Lusa.pt)  
- Uses **Selenium** for automated web scraping.  
- Extracts **daily news articles** related to **Galp Energia** from **Lusa.pt**.  
- Saves results in a structured **CSV file** for further analysis.  

### ✅ 3. Currency Exchange Rate (EUR → USD)  
- Uses **BeautifulSoup** to scrape the latest exchange rate from **x-rates.com**.  
- The function `fetch_eur_to_usd_rate()` extracts the **EUR to USD** exchange rate and timestamps it.  

---

## 🛠️ Tech Stack  
- **Python 3.9+**  
- **Airflow** (Task orchestration)  
- **pytest** (Automated testing framework)  
- **Selenium** (Web scraping with browser automation)  
- **BeautifulSoup** (Web scraping for exchange rates)  
- **Alpha Vantage API** (Stock market data)  
- **PostgreSQL** (Database for storing collected data)  
- **SQLAlchemy** (Database ORM for Python)  
- **dbt** (Data transformation and aggregation)  
- **Docker** (Containerized execution)  
- **GitHub Actions** (Automated testing with CI/CD)  

---

## 🔧 Installation & Setup  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
