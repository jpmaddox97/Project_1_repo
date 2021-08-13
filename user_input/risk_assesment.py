import fire
import questionary



# Still need a cyc function

def get_user_risk_tolerance():
    """
    Get user information to determine risk tolerance
    """
    risk_tolerance = questionary.select("What's your risk tolerance", choices=["Low", "Medium", "High"]).ask()

    indexes = questionary.select("Of the following indexes, select the index that best reflects your current portfolio.", choices=["NASDAQ", "DOW", "S&P 500"]).ask()

    crypto_benchmark = questionary.select("Would you like to benchmark your crypto against an index, a specific crypto, or a composite of cryptos?", choices=["Index", "Crypto", "Crypto Composite"]).ask()

    goals = questionary.select("Would you like to acomplish a dollar goal or a percentage return goal?", choices=["Dollar Goal", "Percentage Goal"]).ask()

    invest_amount = int(questionary.text("How much would you like to invest?").ask())

    user_dictionary = {"risk tolerance": risk_tolerance,
                        "index": indexes,
                        "Crypto Benchmark": crypto_benchmark,
                        "Investment Goals": goals,
                        "Investment Amount": invest_amount,}

    return user_dictionary