# itinerary_agent.py
from agents.flight_agent import flight_agent
from agents.hotel_agent import hotel_agent
from agents.food_agent import food_agent

def itinerary_agent(destination, start_date, end_date):
    flights = flight_agent(destination, start_date, end_date)
    hotels = hotel_agent(destination, start_date, end_date)
    restaurants = food_agent(destination)
    return {
        "destination": destination,
        "dates": f"{start_date} to {end_date}",
        "flights": flights,
        "hotels": hotels,
        "restaurants": restaurants
    }