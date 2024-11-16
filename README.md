# AI Data Analyst with Ollama

## Overview

This project is a **Streamlit-based AI-powered data analysis application** that leverages the Ollama LLM for interpreting user queries and provides analytical insights, visualizations, and statistical operations on uploaded datasets.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Local Codellama LLM instance (accessible via `http://localhost:11434/v1`).
- Required Python libraries:
  - `streamlit`
  - `pandas`
  - `matplotlib`
  - `sklearn`
  - `requests`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abhinavgkrishnan/Python-Data-Analyst
   cd Python-Data-Analyst
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

   If you don’t have a `requirements.txt`, here is the content you should include:
   ```text
   streamlit
   matplotlib
   pandas
   scikit-learn
   requests
   ```

4. Start the Streamlit application:
   ```bash
   streamlit run analyst.py
   ```
### Assumptions
- The uploaded Excel file has column names in the first row.
- The Ollama LLM is pre-configured and running locally.

---

## Documentation

### Key Files

#### 1. `ollama_llm.py`
This script communicates with the Ollama LLM to interpret user queries and extract actionable insights.

**Key Function:**
- `interpret_command_with_ollama(command: str) -> str`
  - Sends the user query to the Ollama LLM.
  - Extracts and returns the response in a structured format.

**Example Response Format:**
```
action: linear regression
x: income
y: sales
```

---

#### 2. `data_functions.py`
This script contains functions for performing various data analysis tasks and visualizations.

**Functions:**

- **Regression Models:**
  - `dynamic_linear_regression`: Fits a linear regression model and plots the results.
  - `polynomial_regression`: Fits a polynomial regression model of a specified degree.
  - `logistic_regression`: Fits a logistic regression model and plots the probability curve.

- **Descriptive and Cleaning Functions:**
  - `data_summary`: Provides metadata about the dataset (e.g., column types and counts).
  - `data_cleaning`: Cleans the dataset by removing duplicates and filling missing values.
  - `descriptive_statistics`: Generates statistical summaries of the dataset.

- **Statistical Analysis:**
  - `correlation_analysis`: Computes and returns the correlation matrix.
  - `covariance_analysis`: Computes and returns the covariance matrix.
  - `skewness_analysis`: Computes skewness for each column.
  - `kurtosis_analysis`: Computes kurtosis for each column.

- **Visualizations:**
  - `scatter_plot`: Generates a scatter plot for two variables.
  - `histogram`: Generates a histogram for a single variable.
  - `bar_chart`: Generates a bar chart for two variables.
  - `line_graph`: Generates a line graph for two variables.

**Unique Implementation Details:**
- Each visualization saves the plot with a timestamp to avoid overwriting files.
- Error handling ensures invalid column names are flagged gracefully.

---

#### 3. `analyst.py`
This is the main application script integrating Streamlit for user interaction.

**Features:**
- **File Upload:**
  Allows users to upload an Excel file for analysis.
- **User Query Input:**
  Accepts user queries in natural language.
- **LLM Interpretation:**
  Uses `ollama_llm.py` to interpret the query and determine the appropriate action.
- **Result Display:**
  Dynamically displays results or visualizations based on user queries.

**Supported Actions:**
- Linear Regression
- Polynomial Regression
- Logistic Regression
- Summary
- Describe (Descriptive Statistics)
- Correlation
- Covariance
- Skewness
- Kurtosis
- Scatter Plot
- Histogram
- Bar Chart
- Line Graph

**Key Implementation:**
- User queries are processed through the Ollama LLM to determine the required action and columns.
- Results are displayed alongside the user's query in the Streamlit interface.
- Responses persist in `st.session_state` to ensure previous results remain visible.

---

## Example Usage
1. Upload an Excel file containing your dataset (e.g., `Age`, `Income`, `Sales`).
2. Enter queries such as:
   - "Run linear regression on income vs sales"
   - "Show histogram of sales"
   - "Do descriptive analysis"
   - "Perform correlation analysis"
3. View results or visualizations directly in the Streamlit interface.

---


For any issues, suggestions, or contributions, please contact Abhinav G Krishnan at abhinavgkrishnan@gmail.com
