import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from ollama_test import interpret_command_with_ollama
from linnear_regression import dynamic_linear_regression

# Initialize session state
if "responses" not in st.session_state:
    st.session_state.responses = []

# Streamlit UI
st.title("Excel-Powered Data Analysis with LLM")

# File uploader for Excel files
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])
if uploaded_file:
    # Load the Excel file into a DataFrame
    df = pd.read_excel(uploaded_file)

    # Normalize column names to lowercase for consistency with the function
    df.columns = [col.lower() for col in df.columns]

    st.write("Data from the uploaded Excel file:")
    st.write(df)

    response_container = st.container()

    # Chat box for user input
    with st.container():
        user_query = st.text_input("Enter your question:")
        if st.button("Submit Query"):
            # Interpret the command using LLM
            response = interpret_command_with_ollama(user_query)

            # Parse the LLM response
            response_lines = response.lower().replace(", ", "\n").split("\n")
            keywords = {"action": None, "visualization": None, "x": None, "y": None}
            for line in response_lines:
                for key in keywords:
                    if line.startswith(f"{key}:"):
                        keywords[key] = line.split(":", 1)[1].strip()

            action = keywords["action"]
            visualization = keywords["visualization"]
            x_column = keywords["x"]
            y_column = keywords["y"]

            # Process the response
            if action == "linear regression" and x_column and y_column:
                # Normalize x_column and y_column for case-insensitive matching
                x_column = x_column.lower()
                y_column = y_column.lower()

                # Check if the specified columns exist
                if x_column not in df.columns or y_column not in df.columns:
                    st.session_state.responses.append(
                        {"text": f"Error: Columns '{x_column}' or '{y_column}' not found in the data."}
                    )
                else:
                    try:
                        # Run linear regression
                        regression_result = dynamic_linear_regression(df, x_column, y_column)

                        # Prepare response entry
                        response_entry = {"text": regression_result.get("message", "Linear regression completed.")}
                        if "type" in regression_result and regression_result["type"] == "plot":
                            response_entry["plot"] = regression_result["value"]

                        # Append to session state
                        st.session_state.responses.append(response_entry)
                    except Exception as e:
                        st.session_state.responses.append({"text": f"Error during execution: {e}"})
            else:
                # Handle other types of responses or errors
                st.session_state.responses.append({"text": response})

    # Display responses
    with response_container:
        for response in st.session_state.responses[::1]:
            st.write(response["text"])
            if "plot" in response:
                st.image(response["plot"], caption="Generated Plot")
