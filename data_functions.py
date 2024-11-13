import pandas as pd
import io
import time

def dynamic_linear_regression(df: pd.DataFrame, x_column: str, y_column: str):
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
    filename = f"linear_regression_{int(time.time())}.png"
    plt.savefig(filename)
    result = {
        "type": "plot",
        "value": filename,
        "message": f"Linear regression completed. Coefficient: {model.coef_[0]}, Intercept: {model.intercept_}"
    }
    return result

def data_summary(df: pd.DataFrame):
    buffer = io.StringIO()
    df.info(buf=buffer)
    summary = buffer.getvalue()
    buffer.close()
    result = {
        "message": f"Data Summary: \n {summary}"
    }
    return result

def data_cleaning(df: pd.DataFrame):
    df.drop_duplicates()
    df.fillna(df.mean())
    clean_data = df.head()
    result = {
        "message": f"Data After Cleaning: \n {clean_data}"
    }
    return result

def descriptive_statistics(df: pd.DataFrame):
    data_desc = df.describe()
    result = {
        "message": f"Data Description: \n {data_desc}"
    }
    return result
def correlation_analysis(df: pd.DataFrame):
    corr = df.corr()
    result = {
        "message": f"Correlation Analysis: \n {corr}"
    }
    return result
def scatter_plot(df: pd.DataFrame, x_column: str, y_column: str):
    import matplotlib.pyplot as plt

    plt.figure()
    plt.scatter(df[x_column], df[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f" Scatter Plot of {x_column.capitalize()} vs. {y_column.capitalize()}")
    filename = f"scatter_plot_{int(time.time())}.png"
    plt.savefig(filename)
    result = {
        "type": "plot",
        "value": filename,
        "message": "Scatter Plot"
    }
    return result
def histogram(df: pd.DataFrame, x_column):

    import matplotlib.pyplot as plt

    plt.figure()
    plt.hist(df[x_column])
    plt.xlabel(x_column)
    plt.ylabel("Frequency")
    plt.title(f"{x_column} Distribution")
    filename = f"histogram_{int(time.time())}.png"
    plt.savefig(filename)
    result = {
        "type": "plot",
        "value": filename,
        "message": "Histogram"
    }
    return result
