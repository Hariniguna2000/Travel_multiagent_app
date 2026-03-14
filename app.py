import streamlit as st
import pandas as pd            # <- Add this here
from agents.itinerary_agent import itinerary_agent
from datetime import date      # if you need to format dates
st.title("AI Travel Planner")

destination = st.text_input("Destination")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")
if st.button("Plan Trip"):
    itinerary = itinerary_agent(destination, start_date, end_date)

    # Optional: format dates
    for f in itinerary['flights']:
        f['departure'] = f['departure'].strftime("%Y-%m-%d")
        f['return'] = f['return'].strftime("%Y-%m-%d")

    # Display Flights table
    flights_df = pd.DataFrame(itinerary['flights'])
    st.subheader("Flights")
    st.table(flights_df)

    # Display Hotels table
    hotels_df = pd.DataFrame(itinerary['hotels'])
    st.subheader("Hotels")
    st.table(hotels_df)

    # Display Restaurants list
    st.subheader("Restaurants")
    for r in itinerary['restaurants']:
        st.write(f"{r['name']} ({r['cuisine']}, Rating: {r['rating']})")