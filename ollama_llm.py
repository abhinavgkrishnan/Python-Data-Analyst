import requests

def interpret_command_with_ollama(command):
    api_base = "http://localhost:11434/v1"
    model_name = "codellama"

    prompt = (
        "You are an assistant specializing in data analysis tasks. "
        "Interpret the user’s query and identify the most relevant statistical action or visualization type. "
        "Always respond in the following format: "
        "action: [specific action, concise, such as 'linear regression', 'summary', 'describe', 'correlation', 'scatter plot', 'histogram', 'clean data', 'line graph', 'bar chart', 'covariance', 'skew', 'kurtosis'] "
        "x: [x-axis column or leave empty if not applicable] "
        "y: [y-axis column or leave empty if not applicable] "
        "Definitions: "
        "'summary' refers to displaying the metadata or structure of the dataset, such as column types and counts. "
        "'describe' refers to generating descriptive statistics of the dataset, such as mean, median, standard deviation, and quartiles. "
        "For 'describe data' or 'do descriptive analysis', always use action: 'describe'. "
        "For 'show covariance matrix' or 'do covariance analysis', always use action: 'covariance'. "
        "Instructions: "
        "- Always match the column names ('x' or 'y') exactly as they appear in the query without substituting or changing them. "
        "- Do not include quotes around column names in the response. Write them plainly (e.g., x: sales). "
        "- Do not respond in a single line. Each key ('action', 'x', 'y') must be on a separate line in the response. "
        "- Ensure that 'y' is only included if the query explicitly involves comparing two columns, such as in scatter plots or linear regression. "
        "- For 'histogram', only include the 'x' column based on the query and leave 'y' empty. "
        "Do not elaborate, explain, or use phrases. Only respond in the specified format."
    )

    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": command},
        ],
    }
    response = requests.post(
        f"{api_base}/chat/completions",
        json=payload,
    )

    # Debugging: Print the raw response
    print("Full API Response:", response.text)

    # Parse the response
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise RuntimeError(f"Error from LLaMA server: {response.text}")
