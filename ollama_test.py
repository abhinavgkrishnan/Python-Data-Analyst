import requests

def interpret_command_with_ollama(command):
    api_base = "http://localhost:11434/v1"
    model_name = "codellama"

    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": "You are an assistant specializing in data analysis tasks. Interpret the user’s query and identify the most relevant statistical action or visualization type. If the query is about a statistical operation like regression or clustering, specify action (e.g., linear regression, clustering) and its associated visualization (e.g., scatter plot). For simple visualization requests like histograms or bar charts, omit the action and only specify visualization. Use the format: action: [specific action, if applicable] visualization: [specific visualization type] x: [x-axis column], y: [y-axis column] (if relevant) Be concise and do not include unrelated details or suggest multiple options."},
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