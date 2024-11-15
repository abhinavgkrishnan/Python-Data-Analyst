import pandas as pd
from ollama_llm import interpret_command_with_ollama  # Import the LLM function
from data_functions import dynamic_linear_regression, data_summary  # Import the regression function

# Load the dataset
file_path = "/Users/gk/Python-AI-Data-Analyst/Analyst/sample_data_for_development.xlsx"
df = pd.read_excel(file_path)

df.columns = [col.lower() for col in df.columns]

# Define the query
# command = "show summary"
# command = "show bar chart of income by age"
# command = "show line graph of age vs sales"
# command = "do descriptive analysis"
# command = "show scatter plot of age vs income"
# command = "show histogram of sales"
command = "run linear regression on income vs age"
# command = "clean data"
# command = "do correlation analysis"
# command = "do covariance analysis"

# Get the response from the LLM
response = interpret_command_with_ollama(command)
print("LLM Response:", response)

# Parse the response
response_lines = response.lower().replace(", ", "\n").split("\n")  # Handle inline key-value pairs
keywords = {"action": None, "x": None, "y": None}

# Extract key information from the response
for line in response_lines:
    for key in keywords:
        if line.startswith(f"{key}:"):
            keywords[key] = line.split(":", 1)[1].strip()

# Example: If "x: Age, y: Sales" is in a single line
if keywords["x"] is None and "x:" in response:
    pairs = response.lower().split(", ")
    for pair in pairs:
        for key in keywords:
            if pair.startswith(f"{key}:"):
                keywords[key] = pair.split(":", 1)[1].strip()

action = keywords["action"]
x_column = keywords["x"]
y_column = keywords["y"]

# Debugging: Print extracted values
print("Action:", action)
print("X-axis column:", x_column)
print("Y-axis column:", y_column)

# Validate and execute the regression function
if action == "linear regression" and x_column and y_column:
    try:
        x_column = x_column.lower()
        y_column = y_column.lower()
        print(f"Running linear regression with x={x_column}, y={y_column}...")
        result = dynamic_linear_regression(df, x_column, y_column)
        print("Regression Result:", result)
    except Exception as e:
        print(f"Error: {e}")

elif action == "summary":
    result = data_summary(df)
    print(result.get("message"))
else:
    print("No valid action or visualization detected.")
