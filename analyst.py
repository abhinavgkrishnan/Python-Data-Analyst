import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from ollama_llm import interpret_command_with_ollama
from data_functions import (
    dynamic_linear_regression, data_summary, data_cleaning, descriptive_statistics,
    correlation_analysis, logistic_regression, scatter_plot, histogram, line_graph, bar_chart,
    covariance_analysis, skewness_analysis, kurtosis_analysis, polynomial_regression,
    logistic_regression
)

if "responses" not in st.session_state:
    st.session_state.responses = []

st.title("AI Data Analyst with Ollama")

uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df.columns = [col.lower() for col in df.columns]
    st.write("Data from the uploaded Excel file:")
    st.write(df)
    response_container = st.container()

    with st.container():
        user_query = st.text_input("Enter your question:")
        if st.button("Submit Query"):
            response = interpret_command_with_ollama(user_query)
            response_lines = response.lower().replace(", ", "\n").split("\n")
            keywords = {"action": None, "x": None, "y": None}
            for line in response_lines:
                for key in keywords:
                    if line.startswith(f"{key}:"):
                        keywords[key] = line.split(":", 1)[1].strip()

            action = keywords["action"]
            x_column = keywords["x"]
            y_column = keywords["y"]

            if action == "linear regression" and x_column and y_column:
                x_column = x_column.lower()
                y_column = y_column.lower()
                if x_column not in df.columns or y_column not in df.columns:
                    st.session_state.responses.append(
                        {"query": user_query, "text": f"Error: Columns '{x_column}' or '{y_column}' not found in the data."}
                    )
                else:
                    try:
                        regression_result = dynamic_linear_regression(df, x_column, y_column)
                        response_entry = {"query": user_query, "text": regression_result.get("message", "Linear regression completed.")}
                        if "type" in regression_result and regression_result["type"] == "plot":
                            response_entry["plot"] = regression_result["value"]
                        st.session_state.responses.append(response_entry)
                    except Exception as e:
                        st.session_state.responses.append({"query": user_query, "text": f"Error during execution: {e}"})
            elif action == "polynomial regression" and x_column and y_column:
                x_column = x_column.lower()
                y_column = y_column.lower()
                if x_column not in df.columns or y_column not in df.columns:
                    st.session_state.responses.append(
                        {"query": user_query, "text": f"Error: Columns '{x_column}' or '{y_column}' not found in the data."}
                    )
                else:
                    try:
                        degree = 2
                        regression_result = polynomial_regression(df, x_column, y_column, degree=degree)
                        response_entry = {"query": user_query, "text": regression_result.get("message", "Polynomial regression completed.")}
                        if "type" in regression_result and regression_result["type"] == "plot":
                            response_entry["plot"] = regression_result["value"]
                        st.session_state.responses.append(response_entry)
                    except Exception as e:
                        st.session_state.responses.append({"query": user_query, "text": f"Error during execution: {e}"})
            elif action == "logistic regression" and x_column and y_column:
                x_column = x_column.lower()
                y_column = y_column.lower()
                if x_column not in df.columns or y_column not in df.columns:
                    st.session_state.responses.append(
                        {"query": user_query, "text": f"Error: Columns '{x_column}' or '{y_column}' not found in the data."}
                    )
                else:
                    try:
                        regression_result = logistic_regression(df, x_column, y_column)
                        response_entry = {"query": user_query, "text": regression_result.get("message", "Logistic regression completed.")}
                        if "type" in regression_result and regression_result["type"] == "plot":
                            response_entry["plot"] = regression_result["value"]
                        st.session_state.responses.append(response_entry)
                    except Exception as e:
                        st.session_state.responses.append({"query": user_query, "text": f"Error during execution: {e}"})
            elif action == "summary":
                summary_result = data_summary(df)
                response_entry = {"query": user_query, "text": summary_result.get("message")}
                st.session_state.responses.append(response_entry)
            elif action == "clean data":
                clean_data = data_cleaning(df)
                response_entry = {"query": user_query, "text": clean_data.get("message")}
                st.session_state.responses.append(response_entry)
            elif action == "describe":
                clean_data = descriptive_statistics(df)
                response_entry = {"query": user_query, "text": clean_data.get("message")}
                st.session_state.responses.append(response_entry)
            elif action == "correlation":
                corr = correlation_analysis(df)
                response_entry = {"query": user_query, "text": corr.get("message")}
                st.session_state.responses.append(response_entry)
            elif action == "covariance":
                cov = covariance_analysis(df)
                response_entry = {"query": user_query, "text": cov.get("message")}
                st.session_state.responses.append(response_entry)
            elif action == "skew":
                skew = skewness_analysis(df)
                response_entry = {"query": user_query, "text": skew.get("message")}
                st.session_state.responses.append(response_entry)
            elif action == "kurtosis":
                kurt = kurtosis_analysis(df)
                response_entry = {"query": user_query, "text": kurt.get("message")}
                st.session_state.responses.append(response_entry)
            elif action == "scatter plot" and x_column and y_column:
                x_column = x_column.lower()
                y_column = y_column.lower()
                if x_column not in df.columns or y_column not in df.columns:
                    st.session_state.responses.append(
                        {"query": user_query, "text": f"Error: Columns '{x_column}' or '{y_column}' not found in the data."}
                    )
                else:
                    try:
                        scatter_result = scatter_plot(df, x_column, y_column)
                        response_entry = {"query": user_query, "text": scatter_result.get("message")}
                        if "type" in scatter_result and scatter_result["type"] == "plot":
                            response_entry["plot"] = scatter_result["value"]
                        st.session_state.responses.append(response_entry)
                    except Exception as e:
                        st.session_state.responses.append({"query": user_query, "text": f"Error during execution: {e}"})
            elif action == "histogram" and x_column:
                x_column = x_column.lower()
                if x_column not in df.columns:
                    st.session_state.responses.append(
                        {"query": user_query, "text": f"Error: Column '{x_column}' not found in the data."}
                    )
                else:
                    try:
                        histogram_result = histogram(df, x_column)
                        response_entry = {"query": user_query, "text": histogram_result.get("message")}
                        if "type" in histogram_result and histogram_result["type"] == "plot":
                            response_entry["plot"] = histogram_result["value"]
                        st.session_state.responses.append(response_entry)
                    except Exception as e:
                        st.session_state.responses.append({"query": user_query, "text": f"Error during execution: {e}"})
            elif action == "bar chart" and x_column and y_column:
                x_column = x_column.lower()
                y_column = y_column.lower()
                if x_column not in df.columns or y_column not in df.columns:
                    st.session_state.responses.append(
                        {"query": user_query, "text": f"Error: Columns '{x_column}' or '{y_column}' not found in the data."}
                    )
                else:
                    try:
                        bar_result = bar_chart(df, x_column, y_column)
                        response_entry = {"query": user_query, "text": bar_result.get("message")}
                        if "type" in bar_result and bar_result["type"] == "plot":
                            response_entry["plot"] = bar_result["value"]
                        st.session_state.responses.append(response_entry)
                    except Exception as e:
                        st.session_state.responses.append({"query": user_query, "text": f"Error during execution: {e}"})
            elif action == "line graph" and x_column and y_column:
                x_column = x_column.lower()
                y_column = y_column.lower()
                if x_column not in df.columns or y_column not in df.columns:
                    st.session_state.responses.append(
                        {"query": user_query, "text": f"Error: Columns '{x_column}' or '{y_column}' not found in the data."}
                    )
                else:
                    try:
                        line_result = line_graph(df, x_column, y_column)
                        response_entry = {"query": user_query, "text": line_result.get("message")}
                        if "type" in line_result and line_result["type"] == "plot":
                            response_entry["plot"] = line_result["value"]
                        st.session_state.responses.append(response_entry)
                    except Exception as e:
                        st.session_state.responses.append({"query": user_query, "text": f"Error during execution: {e}"})
            else:
                st.session_state.responses.append({"query": user_query, "text": "please try again"})

            with response_container:
                for response in st.session_state.responses[::1]:
                    st.write(f"**User Query:** {response['query']}")
                    if "plot" in response:
                        st.image(response["plot"], caption=response["text"])
                    elif any(keyword in response["text"] for keyword in ("Data Summary:", "Data Description:", "Data After Cleaning:", "Correlation Analysis:", "Covariance Analysis:", "Skewness Analysis:", "Kurtosis Analysis:")):
                        st.code(response["text"], language="plaintext")
                    else:
                        st.write(response["text"])
