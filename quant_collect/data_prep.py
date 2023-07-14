import pandas as pd

# Specify the path to the downloaded dataset files
path = "path/to/dataset/files/"

# Read the portfolio dataset files
portfolio_returns = pd.read_csv(path + "portfolios.csv")
portfolio_factors = pd.read_csv(path + "factors.csv")

# Set the date column as the index
portfolio_returns.set_index("date", inplace=True)
portfolio_factors.set_index("date", inplace=True)

# Convert the date index to pandas DateTimeIndex
portfolio_returns.index = pd.to_datetime(portfolio_returns.index)
portfolio_factors.index = pd.to_datetime(portfolio_factors.index)

# Subset the required columns
portfolio_returns = portfolio_returns[["Mkt-RF", "RF"]]
portfolio_factors = portfolio_factors[["Mkt-RF", "SMB", "HML", "RF"]]

# Calculate excess returns by subtracting the risk-free rate
portfolio_returns["Excess_Returns"] = portfolio_returns["Mkt-RF"] - portfolio_returns["RF"]

# Calculate excess factor returns by subtracting the risk-free rate
portfolio_factors["Excess_Mkt_RF"] = portfolio_factors["Mkt-RF"] - portfolio_factors["RF"]

# Save the processed data to new CSV files
portfolio_returns.to_csv("processed_portfolio_returns.csv")
portfolio_factors.to_csv("processed_portfolio_factors.csv")
