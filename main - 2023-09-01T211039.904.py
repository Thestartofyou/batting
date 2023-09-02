def calculate_strikeout_probability(historical_strikeouts, total_at_bats, future_at_bats):
    # Calculate the strikeout rate from historical data
    strikeout_rate = historical_strikeouts / total_at_bats

    # Calculate the probability of striking out in future at-bats
    probability_strikeout = 1 - (1 - strikeout_rate) ** future_at_bats

    return probability_strikeout

# Example usage
historical_strikeouts = 50  # Number of strikeouts in the past
total_at_bats = 300       # Total number of at-bats in the past
future_at_bats = 10       # Number of future at-bats to predict

strikeout_probability = calculate_strikeout_probability(historical_strikeouts, total_at_bats, future_at_bats)

print(f"The probability of striking out in the next {future_at_bats} at-bats is {strikeout_probability:.2%}")
