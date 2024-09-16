import requests
import pandas as pd

API_KEY = "YOUR_API_KEY"

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}  
        
    def add_stock(self, symbol, shares):
        
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
            
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol} to your portfolio.")
        

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            
            if self.portfolio[symbol] > shares:
                self.portfolio[symbol] -= shares
                print(f"Removed {shares} shares of {symbol} from your portfolio.")
                
            elif self.portfolio[symbol] == shares:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol} from your portfolio.")
                
            else:
                print(f"You don't have enough shares of {symbol} to remove.")
                
        else:
            print(f"{symbol} is not in your portfolio.")
            

    def get_real_time_data(self, symbol):
        try:
            url = f"https://api.example.com/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={API_KEY}"
            response = requests.get(url)
            data = response.json()

            latest_close = list(data['Time Series (1min)'].values())[0]['4. close']
            return float(latest_close)

        except Exception as e:
            print(f"Error fetching stock data for {symbol}: {e}")
            return None

    def view_portfolio(self):

        print("\nYour Portfolio:")
        portfolio_value = 0
        stock_data = []

        for symbol, shares in self.portfolio.items():
            price = self.get_real_time_data(symbol)
            if price:
                total_value = price * shares
                portfolio_value += total_value
                stock_data.append([symbol, shares, price, total_value])

        df = pd.DataFrame(stock_data, columns=['Stock Symbol', 'Shares Owned', 'Current Price', 'Total Value'])
        print(df)
        print(f"\nTotal Portfolio Value: ${portfolio_value:.2f}\n")


def main():
    portfolio = StockPortfolio()
    
    while True:
        print("\n1. Add Stock\n2. Remove Stock\n3. View Portfolio\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)

        elif choice == "2":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.remove_stock(symbol, shares)

        elif choice == "3":
            portfolio.view_portfolio()

        elif choice == "4":
            print("Exiting the tool. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()




