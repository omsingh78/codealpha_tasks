import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 310,
    "GOOGL": 145,
    "AMZN": 135
}

def main():
    portfolio = {}
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Enter your stocks (type 'done' to finish):")

    while True:
        stock = input("Stock symbol: ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("❌ Stock not found in price list. Try again.")
            continue
        try:
            qty = int(input(f"Enter quantity of {stock}: "))
            portfolio[stock] = portfolio.get(stock, 0) + qty
        except ValueError:
            print("❌ Please enter a valid number for quantity.")

    print("\n--- Portfolio Summary ---")
    total = 0
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        print(f"{stock}: {qty} × ${stock_prices[stock]} = ${value}")
        total += value

    print(f"\n✅ Total Investment Value = ${total}")

    save_choice = input("\nDo you want to save results? (txt/csv/none): ").lower()

    if save_choice == "txt":
        with open("portfolio.txt", "w") as f:
            f.write("--- Portfolio Summary ---\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} × ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
            f.write(f"\nTotal Investment Value = ${total}\n")
        print("📄 Saved to portfolio.txt")

    elif save_choice == "csv":
        with open("portfolio.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])
            writer.writerow(["TOTAL", "", "", total])
        print("📊 Saved to portfolio.csv")

if __name__ == "__main__":
    main()
