# frontend/app.py
import streamlit as st
import requests

st.title("AI Travel Planner")

destination = st.text_input("Destination city")
start_date = st.date_input("Start date")
end_date = st.date_input("End date")

if st.button("Plan Trip"):
    # Call backend API
    response = requests.get(
        "http://127.0.0.1:8000/plan",
        params={"destination": destination, "start_date": start_date, "end_date": end_date}
    )
    plan = response.json()

    st.subheader("Flight Options")
    for f in plan["flights"]:
        st.write(f"{f['airline']} - {f['price']} ({f['departure']} to {f['return']})")

    st.subheader("Hotel Options")
    for h in plan["hotels"]:
        st.write(f"{h['name']} - {h['price']} - Rating: {h['rating']}")

    st.subheader("Recommended Restaurants")
    for r in plan["restaurants"]:
        st.write(f"{r['name']} - {r['cuisine']} - Rating: {r['rating']}")