import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Expense Tracker")

st.title("🎓 Student Expense Tracker")
st.write("Manage your daily expenses easily!")

if "expenses" not in st.session_state:
    st.session_state.expenses = []

st.subheader("Add New Expense")

name = st.text_input("Expense Name")
amount = st.number_input("Amount (₹)", min_value=0)
category = st.selectbox(
    "Category",
    ["Food", "Travel", "Books", "Shopping", "Other"]
)

if st.button("Add Expense"):
    if name and amount > 0:
        st.session_state.expenses.append({
            "Name": name,
            "Amount": amount,
            "Category": category
        })
        st.success("Expense Added Successfully!")

st.subheader("Your Expenses")

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.dataframe(df)

    st.metric("Total Expenses", f"₹{df['Amount'].sum()}")

    st.download_button(
        "Download Expenses",
        df.to_csv(index=False),
        "expenses.csv"
    )
else:
    st.info("No expenses added yet.")