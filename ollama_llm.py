import requests

def interpret_command_with_ollama(command):
    api_base = "http://localhost:11434/v1"
    model_name = "codellama"

    prompt = (
        "You are an assistant specializing in data analysis tasks. "
        "Interpret the user’s query and identify the most relevant statistical action or visualization type. "
        "Respond strictly in the following format: "
        "action: [specific action, concise and descriptive, such as 'linear regression', 'clustering', 'summary', 'clean', 'describe', 'correlation' or leave empty if not applicable. 'descriptive analysis' in query means action is 'describe', 'summary' in query means action is summary 'histogram' in query means action is histogram] "
        "visualization: [specific visualization type, concise and descriptive, such as 'scatter plot', 'bar chart', 'histogram' or leave empty if not applicable] "
        "x: [x-axis column or leave empty if not applicable, only take column name from the query. 'histogram' in query means only 'x-axis' column] "
        "y: [y-axis column or leave empty if not applicable, only take column name from the query] "
        "Do not elaborate, explain, or use phrases. Keep the action concise without verbs or unnecessary details."
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
