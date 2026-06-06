import streamlit as st
import pandas as pd
import os
st.title("Expense Tracker")
date = st.date_input("Date")
cat = st.selectbox(
    "Category",
    ["Food", "Clothing", "Cosmetics", "College_Work", "Others"],
    index=None,
    key="entry_category",
    placeholder="Choose a category"
)
des = st.text_input("Description")
amt = st.number_input("Amount")
if st.button("Enter Expense"):
    df = pd.DataFrame({"Date": [date],
        "Category": [cat],
        "Description": [des],
        "Amount": [amt]
    })
    st.write("Expense noted")
    if os.path.exists("expense_tracker.csv"):
        old_df = pd.read_csv("expense_tracker.csv")
        combined_df = pd.concat(
            [old_df, df],
            ignore_index=True
        )
        combined_df.to_csv(
            "expense_tracker.csv",
            index=False
        )
    else:
        df.to_csv(
            "expense_tracker.csv",
            index=False
        )

if os.path.exists("expense_tracker.csv"):
    df = pd.read_csv("expense_tracker.csv")
    df["Date"] = pd.to_datetime(df["Date"])

else:
      df = pd.DataFrame(
        columns=["Date", "Category", "Description", "Amount"]
     )
st.write("Expense Calculator")
mon = st.number_input(
    "Enter month",
    min_value=1,
    max_value=12,
    value=None,
    placeholder="Enter month"
)
cate = st.selectbox(
    "Category",
    ["Food", "Clothing", "Cosmetics", "College_Work", "Others"],
    index=None,
    key="filter_category",
    placeholder="Choose a category"
)
year = st.number_input(
    "Enter year",
    min_value=2026,
    value=None,
    placeholder="Enter year"
)
def calc_exp(ca,mon,year):
    f_df = df[
    (df["Date"].dt.month == mon) &
    (df["Date"].dt.year == year) &
    (df["Category"] == ca)
    ]
    f_df = df

    if mon is not None:
        f_df=f_df[f_df["Date"].dt.month==mon]

    if year is not None:
        f_df=f_df[f_df["Date"].dt.year==year]

    if cate is not None:
        f_df=f_df[f_df["Category"]==cate]
    return f_df



if st.button("Calculate Expense"):
    result = calc_exp(cate, mon, year)

    st.dataframe(result)

    total = result["Amount"].sum()

    st.write("Total Expense:", total)
    
    st.write("Number of Expenses:", len(result))

