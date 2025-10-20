import streamlit as st

st.title("Job Shop Lean Assessment Tool")

#st.write("Welcome! This is where the questionnaire will appear.")
#st.subheader('Section 1')

#Question 1
q1 = st.radio('1. Toyota is a low-mix high-volume manufacturer of a limited variety of similar assemblies. Compared to Toyota, would you say that you are a high-mix low-volume manufacturer of a large variety of dissimilar components? ', ("Yes", "No"))

#Question 2
q2 = st.radio('2. Several performance measures, such as Order Flow Time, Inventory Dollar Days (Work-In-Process Inventory) and $ Shipped per Day (Throughput), focus on the speed with which an order is shipped to and paid for by a customer (Cash Flow Velocity). Now, Lean recommends to focus on the elimination of the Seven Wastes (Overproduction, Waiting, Transportation, Over-processing, Inventory, Operator Motion and Scrap/Rework). Can the impact of Waste Elimination be measured using Cash Flow Velocity? ', ("Yes", "No"))

#Question 3
#q3 = st.radio('3. ', ("Yes", "No"))


# Submit button
if st.button("Submit"):
    # Scoring logic
    score = 0
    if q1 == "Yes":  # correct answer
        score += 1
    if q2 == "Yes":  # correct answer
        score += 1

    total = 2
    percentage = (score / total) * 100

    st.success(f"Your score: {percentage:.0f}%")


     # Recommendations
    if q1 == "No":
        st.warning("Q1: Wrong Answer. Rcommendation.")
    if q2 == "No":
        st.warning("Q2: Wrong Answer. Recommendation.")



    # Report download (simple text)
    report = f"JSLAT Assessment Report\n\nScore: {percentage:.0f}%\n\nRecommendations:\n"
    if q1 == "No":
        report += "- Recommendation for question 1.\n"
    if q2 == "No":
        report += "- Recommendation for question 2.\n"

    st.download_button(" Download Report", report, file_name="JSLAT report.txt")
