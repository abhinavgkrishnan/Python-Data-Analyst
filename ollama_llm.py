import requests

def interpret_command_with_huggingface(command):
    api_url = "https://api-inference.huggingface.co/models/meta/codellama"
    headers = {"Authorization": f"Bearer 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"}

    prompt = (
        "You are an assistant specializing in data analysis tasks. "
        "Interpret the user’s query and identify the most relevant statistical action or visualization type. "
        "Always respond in the following format: "
        "action: [specific action, concise, only as 'linear regression', 'logistic regression', 'polynomial regression', 'summary', 'describe', 'correlation', 'scatter plot', 'histogram', 'clean data', 'line graph', 'bar chart', 'covariance', 'skew', 'kurtosis'] "
        "x: [x-axis column or leave empty if not applicable] "
        "y: [y-axis column or leave empty if not applicable] "
        "Definitions: "
        "For 'describe data' or 'do descriptive analysis', always use action: 'describe'. "
        "For 'show covariance matrix' or 'do covariance analysis', always use action: 'covariance'. "
        "Instructions: "
        "- Always match the column names ('x' or 'y') exactly as they appear in the query without substituting or changing them. "
        "- Do not include quotes around column names in the response. Write them plainly (e.g., x: sales). "
        "- Do not respond in a single line. Each key ('action', 'x', 'y') must be on a separate line in the response. "
        "- Ensure that 'y' is only included if the query explicitly involves comparing two columns, such as in scatter plots, linear regression, polynomial regression, logistic regression, bar chart, line graph. "
        "- For 'histogram', only include the 'x' column based on the query and leave 'y' empty. "
        "Do not elaborate, explain, or use phrases. Only respond in the specified format."
    )

    payload = {"inputs": f"User Query: {command}\n{prompt}"}

    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["generated_text"]
    else:
        raise RuntimeError(f"Error from Hugging Face API: {response.text}")