# agents/flight_agent.py
def flight_agent(destination, start_date, end_date):
    # In real project, call an API like Skyscanner or Kayak
    # Here we mock the output
    flights = [
        {"airline": "Air Canada", "price": "$500", "departure": start_date, "return": end_date},
        {"airline": "Delta", "price": "$450", "departure": start_date, "return": end_date},
    ]
    return flights