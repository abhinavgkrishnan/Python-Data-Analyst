import pandas as pd
from ollama_test import interpret_command_with_ollama  # Import the LLM function
from linnear_regression import dynamic_linear_regression  # Import the regression function

# Load the dataset
file_path = "/Users/gk/Python-AI-Data-Analyst/sample_data_for_development.xlsx"
df = pd.read_excel(file_path)

# Define the query
command = "run a linear regression on age vs sales"

# Get the response from the LLM
response = interpret_command_with_ollama(command)
print("LLM Response:", response)

# Parse the response
response_lines = response.split("\n")
action = None
visualization = None
x_column = None
y_column = None

# Extract keywords from the LLM response
for line in response_lines:
    if line.startswith("action:"):
        action = line.split(":", 1)[1].strip()
    elif line.startswith("visualization:"):
        visualization = line.split(":", 1)[1].strip()
    elif line.startswith("x:"):
        x_column = line.split(":", 1)[1].strip()
    elif line.startswith("y:"):
        y_column = line.split(":", 1)[1].strip()

# Validate and execute the regression function
if action == "Linear Regression" and visualization == "Scatter Plot" and x_column and y_column:
    try:
        print(f"Running linear regression with x={x_column}, y={y_column}...")
        result = dynamic_linear_regression(df, x_column, y_column)
        print("Regression Result:", result)
    except Exception as e:
        print(f"Error: {e}")
else:
    print("No valid action or visualization detected.")