# AI Data Analyst with Ollama

## Overview

AI Data Analyst with Ollama is a Streamlit-based application that allows users to analyze their datasets using advanced machine learning models and statistical methods. It leverages natural language queries interpreted by a locally hosted LLM (Codellama) to execute tasks such as generating visualizations, performing regression analysis, and more.

## Features

- Interpret user queries via a locally hosted LLM (Codellama).
- Support for various statistical operations:
  - Descriptive Statistics
  - Correlation and Covariance Analysis
  - Skewness and Kurtosis
- Machine Learning Models:
  - Linear Regression
  - Polynomial Regression
  - Logistic Regression
- Generate visualizations:
  - Scatter Plot
  - Histogram
  - Line Graph
  - Bar Chart

## Setup and Installation

### Prerequisites

- Python 3.9+
- Local Codellama LLM instance (accessible via `http://localhost:11434/v1`).
- Streamlit for UI rendering.
- Matplotlib, Pandas, Scikit-learn for data analysis and visualization.

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:
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

3. Start the local Codellama LLM instance:
   Ensure your LLM is running and accessible via `http://localhost:11434/v1`.

4. Run the Streamlit app:
   ```bash
   streamlit run analyst.py
   ```

## Usage

1. Upload an Excel file via the UI.
2. Enter your query in plain English. Example queries:
   - "Run linear regression on income vs sales"
   - "Show a scatter plot of age vs income"
   - "Perform correlation analysis"
3. View the results and generated visualizations directly in the Streamlit interface.

## Key Files

### `analyst.py`
The main entry point for the application. Handles:
- UI rendering using Streamlit.
- Query input from the user.
- Calling the LLM for query interpretation.
- Mapping the interpreted commands to respective functions.

### `ollama_llm.py`
Interacts with the locally hosted Codellama LLM to interpret user queries. Key considerations:
- Follows a strict format for the LLM's response.
- Processes the LLM response to extract the `action`, `x`, and `y`.

### `data_functions.py`
Contains the core logic for data analysis and visualization:

- **Regression Models**
  - `dynamic_linear_regression(df, x_column, y_column)`: Performs linear regression.
  - `polynomial_regression(df, x_column, y_column, degree)`: Polynomial regression with a specified degree.
  - `logistic_regression(df, x_column, y_column)`: Logistic regression.

- **Statistical Analysis**
  - `data_summary(df)`: Provides dataset metadata.
  - `data_cleaning(df)`: Cleans the dataset by dropping duplicates and filling missing values.
  - `descriptive_statistics(df)`: Generates descriptive statistics.
  - `correlation_analysis(df)`: Computes and displays the correlation matrix.
  - `covariance_analysis(df)`: Computes and displays the covariance matrix.
  - `skewness_analysis(df)`: Computes skewness for all numeric columns.
  - `kurtosis_analysis(df)`: Computes kurtosis for all numeric columns.

- **Visualizations**
  - `scatter_plot(df, x_column, y_column)`: Generates a scatter plot.
  - `histogram(df, x_column)`: Generates a histogram.
  - `bar_chart(df, x_column, y_column)`: Generates a bar chart.
  - `line_graph(df, x_column, y_column)`: Generates a line graph.

## Assumptions

1. Column names in the dataset are case-insensitively matched to the queries.
2. All datasets are in Excel format (`.xls` or `.xlsx`).
3. The local LLM is pre-configured and operational.
4. User queries adhere to the supported actions and column names available in the dataset.

## Notes
- Ensure that the uploaded Excel file contains appropriate column names and data types.
- The polynomial regression function defaults to degree 2 unless specified otherwise.
- Logistic regression assumes the dependent variable (`y`) is binary.

## Contributions
Feel free to submit issues or pull requests for additional features or bug fixes.

## License
This project is licensed under the MIT License.

