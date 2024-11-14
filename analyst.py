import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from ollama_llm import interpret_command_with_ollama
from data_functions import dynamic_linear_regression, data_summary, data_cleaning, descriptive_statistics, correlation_analysis, scatter_plot, histogram

# Initialize session state
if "responses" not in st.session_state:
    st.session_state.responses = []

# Streamlit UI
st.title("AI Data Analyst with Ollama")

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
            keywords = {"action": None, "x": None, "y": None}
            for line in response_lines:
                for key in keywords:
                    if line.startswith(f"{key}:"):
                        keywords[key] = line.split(":", 1)[1].strip()

            action = keywords["action"]
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
            elif action == "summary":
                summary_result = data_summary(df)
                response_entry = {"text": summary_result.get("message")}
                st.session_state.responses.append(response_entry)
            elif action == "clean data":
                clean_data = data_cleaning(df)
                response_entry = {"text": clean_data.get("message")}
                st.session_state.responses.append(response_entry)
            elif action == "describe":
                clean_data = descriptive_statistics(df)
                response_entry = {"text": clean_data.get("message")}
                st.session_state.responses.append(response_entry)
            elif action == "correlation":
                corr = correlation_analysis(df)
                response_entry = {"text": corr.get("message")}
                st.session_state.responses.append(response_entry)
            elif action == "scatter plot" and x_column and y_column:
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
                        scatter_result = scatter_plot(df, x_column, y_column)
                        response_entry = {"text": scatter_result.get("message")}
                        if "type" in scatter_result and scatter_result["type"] == "plot":
                            response_entry["plot"] = scatter_result["value"]
                        st.session_state.responses.append(response_entry)
                    except Exception as e:
                        st.session_state.responses.append({"text": f"Error during execution: {e}"})
            elif action == "histogram" and x_column:
                # Normalize x_column for case-insensitive matching
                x_column = x_column.lower()

                # Check if the specified column exists
                if x_column not in df.columns:
                    st.session_state.responses.append(
                        {"text": f"Error: Column '{x_column}' not found in the data."}
                    )
                else:
                    try:
                        histogram_result = histogram(df, x_column)
                        response_entry = {"text": histogram_result.get("message")}
                        if "type" in histogram_result and histogram_result["type"] == "plot":
                            response_entry["plot"] = histogram_result["value"]
                        st.session_state.responses.append(response_entry)
                    except Exception as e:
                        st.session_state.responses.append({"text": f"Error during execution: {e}"})
            else:
                # Append a generic "please try again" response if no valid action or visualization was detected
                st.session_state.responses.append({"text": "please try again"})

            # Display responses
            with response_container:
                for response in st.session_state.responses[::1]:  # Reverse order for latest response first
                    if "plot" in response:
                        st.image(response["plot"], caption="Generated Plot")
                    elif any(keyword in response["text"] for keyword in ("Data Summary:", "Data Description:", "Data After Cleaning:", "Correlation Analysis:")):
                        st.code(response["text"], language="plaintext")
                    else:
                        st.write(response["text"])
