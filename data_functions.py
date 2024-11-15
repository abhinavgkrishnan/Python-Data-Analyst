import pandas as pd
import io
import time

def dynamic_linear_regression(df: pd.DataFrame, x_column: str, y_column: str):
    X = df[[x_column]].values
    y = df[y_column].values

    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as plt

    model = LinearRegression()
    model.fit(X, y)
    df['y_pred'] = model.predict(X)

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
    
def polynomial_regression(df: pd.DataFrame, x_column: str, y_column: str, degree: int = 2):
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as plt
    import numpy as np

    X = df[[x_column]].to_numpy()
    y = df[y_column].to_numpy()

    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)

    model = LinearRegression()
    model.fit(X_poly, y)
    y_pred = model.predict(X_poly)

    plt.scatter(X, y, color="blue", label="Actual Data")
    plt.plot(X, y_pred, color="red", label=f"Polynomial Regression (Degree {degree})")
    plt.xlabel(x_column.capitalize())
    plt.ylabel(y_column.capitalize())
    plt.title(f"{y_column.capitalize()} vs. {x_column.capitalize()} (Polynomial Regression)")
    plt.legend()
    filename = f"polynomial_regression_{int(time.time())}.png"
    plt.savefig(filename)
    result = {
        "type": "plot",
        "value": filename,
        "message": f"Polynomial regression completed with degree {degree}."
    }
    return result
    
def logistic_regression(df: pd.DataFrame, x_column: str, y_column: str):
    from sklearn.linear_model import LogisticRegression
    import matplotlib.pyplot as plt
    import numpy as np

    X = df[[x_column]].to_numpy()
    y = df[y_column].to_numpy()

    model = LogisticRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    y_prob = model.predict_proba(X)[:, 1]

    plt.scatter(X, y, color="blue", label="Actual Data")
    plt.plot(X, y_prob, color="red", label="Logistic Regression Curve")
    plt.xlabel(x_column.capitalize())
    plt.ylabel(f"Probability of {y_column.capitalize()}")
    plt.title(f"{y_column.capitalize()} vs. {x_column.capitalize()} (Logistic Regression)")
    plt.legend()
    filename = f"logistic_regression_{int(time.time())}.png"
    plt.savefig(filename)
    result = {
        "type": "plot",
        "value": filename,
        "message": f"Logistic regression completed. Coefficients: {model.coef_[0]}, Intercept: {model.intercept_}"
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

def covariance_analysis(df: pd.DataFrame):
    cov = df.cov()
    formatted_cov = cov.to_string()
    result = {
        "message": f"Covariance Analysis: \n {formatted_cov}"
    }
    return result
    
def skewness_analysis(df: pd.DataFrame):
    skew = df.skew()
    result = {
        "message": f"Skewness Analysis: \n{skew}"
    }
    return result
def kurtosis_analysis(df: pd.DataFrame):
    kurt = df.kurtosis()
    result = {
        "message": f"Kurtosis Analysis: \n{kurt}"
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
def bar_chart(df: pd.DataFrame, x_column: str, y_column: str):
    import matplotlib.pyplot as plt

    plt.figure()
    plt.bar(df[x_column], df[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f"Bar Chart of {y_column.capitalize()} by {x_column.capitalize()}")
    filename = f"bar_chart_{int(time.time())}.png"
    plt.savefig(filename)
    result = {
        "type": "plot",
        "value": filename,
        "message": "Bar Chart"
    }
    return result
def line_graph(df: pd.DataFrame, x_column: str, y_column: str):
    import matplotlib.pyplot as plt

    plt.figure()
    plt.plot(df[x_column], df[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f"Line Graph of {y_column.capitalize()} vs. {x_column.capitalize()}")
    filename = f"line_graph_{int(time.time())}.png"
    plt.savefig(filename)
    result = {
        "type": "plot",
        "value": filename,
        "message": "Line Graph"
    }
    return result
