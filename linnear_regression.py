import pandas as pd

def dynamic_linear_regression(df: pd.DataFrame, x_column: str, y_column: str):
    """
    Runs linear regression on a specified target variable and a predictor and returns the results along with a plot.
    Args:
        df (DataFrame): the given dataframe
        x_column (String): predictor
        y_column (string): target variable
    """
    if x_column not in df.columns or y_column not in df.columns:
        raise ValueError(f"Columns '{x_column}' or '{y_column}' not found in the DataFrame.")
    X = df[[x_column]].values
    y = df[y_column].values

    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as plt

    model = LinearRegression()
    model.fit(X, y)
    df['y_pred'] = model.predict(X)

    plt.scatter(df[x_column], df[y_column], color="blue", label="Actual Data")
    plt.plot(df[x_column], df['y_pred'], color="red", label="Regression Line")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f"{y_column} vs. {x_column}")
    plt.legend()
    plt.savefig("temp_chart.png")
    plt.show()
    result = {
        "type": "plot",
        "value": "temp_chart.png",
        "message": f"Linear regression completed. Coefficient: {model.coef_[0]}, Intercept: {model.intercept_}"
    }
    return result
