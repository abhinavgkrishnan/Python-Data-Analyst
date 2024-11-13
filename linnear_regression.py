import pandas as pd

def dynamic_linear_regression(df: pd.DataFrame, x_column: str, y_column: str):
    # Normalize column names in the DataFrame to lowercase for case-insensitive lookup
    df.columns = [col.lower() for col in df.columns]

    # Normalize input column names to lowercase
    x_column = x_column.lower()
    y_column = y_column.lower()

    # Check if specified columns exist
    if x_column not in df.columns or y_column not in df.columns:
        raise ValueError(f"Columns '{x_column}' or '{y_column}' not found in the DataFrame.")

    # Extract X and y values
    X = df[[x_column]].values
    y = df[y_column].values

    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as plt

    # Perform linear regression
    model = LinearRegression()
    model.fit(X, y)
    df['y_pred'] = model.predict(X)

    # Plot the regression results
    plt.scatter(df[x_column], df[y_column], color="blue", label="Actual Data")
    plt.plot(df[x_column], df['y_pred'], color="red", label="Regression Line")
    plt.xlabel(x_column.capitalize())
    plt.ylabel(y_column.capitalize())
    plt.title(f"{y_column.capitalize()} vs. {x_column.capitalize()}")
    plt.legend()
    plt.savefig("temp_chart.png")
    result = {
        "type": "plot",
        "value": "temp_chart.png",
        "message": f"Linear regression completed. Coefficient: {model.coef_[0]}, Intercept: {model.intercept_}"
    }
    return result
