"""Main module."""
class BassModelPackageBase:
    """
    Base class for the Bass model package.
    """
    def __init__(self, data):
        """
        Initialize the Bass model package object.

        Parameters:
        - data: The input data for the model.

        Returns:
        None
        """
        self.data = data

    def calculate_bass_model(self, t, p, q, k):
        """
        Calculate the Bass model.

        Parameters:
        - t: Time parameter.
        - p: Coefficient of innovation.
        - q: Coefficient of imitation.
        - k: Coefficient of market potential.

        Returns:
        None
        """
        pass

    def fit(self):
        """
        Fit the data to the model.

        Returns:
        None
        """
        pass

    def predict(self):
        """
        Perform predictions using the fitted model.

        Returns:
        None
        """
        pass

    def plot(self):
        """
        Plot the prediction.

        Returns:
        None
        """
        pass

    def plot_cdf(self):
        """
        Plot the cumulative distribution function of the prediction.

        Returns:
        None
        """
        pass

    def summarize(self):
        """
        Summarize the results of the model prediction.

        Returns:
        None
        """
        pass

import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class BassOLSMP(BassModelPackageBase):
    """
    Model for implementing Bass Diffusion with OLS: ordinary least-squares method.
    """

    def __init__(self, data):
        """
         Method to initialize the object of Base model.
         Parameters
         ----------
         data : pandas.DataFrame
             Data to fit the model.
         Returns
         -------
         None
         """
        super().__init__(data)
        self.data = data
        self.q = None
        self.p = None
        self.cum_sales_sq = None
        self.m = None
        self.result = None
        self.cum_sales_forecast = None
        self.forecast = None
        self.model = None
        self.pars = None
        self.cum_sales = None

        if data is None:
            print("Error: No data provided. Please input data.")
        try:
            if data[-3:] == "csv":
                self.data = pd.read_csv(data)
                self.data = np.array(self.data)
            elif data[-4:] == "xlsx":
                self.data = pd.read_excel(data)
                self.data = np.array(self.data)
            else:
                self.data = np.genfromtxt(data, delimiter="\t", encoding="utf8")
        except OSError:
            print("Error: Data file not found. Please provide a valid data.")

        try:
            self.body = self.data[:, 1]
            self.time_range = range(1, len(self.body) + 1)
        except IndexError:
            print("Error: Incorrect data type. Please provide data in xlsx, txt, or csv format.")

def calculate_bass_model(p_coefficient, q_coefficient, time_interval, **kwargs):
    """
    Calculate the rate of change for the Bass model.
    
    Parameters:
    - p_coefficient: int
        Coefficient of innovation.
    - q_coefficient: int
        Coefficient of imitation.
    - time_interval: int
        Time interval.
    - **kwargs: additional keyword arguments (optional)
    
    Returns:
    - float
        Rate of change.
    """
    argument1 = time_interval * (p_coefficient + q_coefficient)
    exp_value = p_coefficient * np.exp(argument1)
    numerator = exp_value * (p_coefficient + q_coefficient) ** 2
    denominator = (exp_value * time_interval + q_coefficient) ** 2
    rate_of_change = numerator / denominator
    return rate_of_change

def calculate_parameters(self):
    """
    Calculate the maximum number of adopters, innovation coefficient, and imitation coefficient.
    
    Returns:
    - tuple of floats
        Maximum number of adopters, innovation coefficient, and imitation coefficient.
    """
    m1 = (-self.pars['Cum_Sales'] + np.sqrt(
        self.pars['Cum_Sales'] ** 2 - 4 * self.pars['Intercept'] * self.pars['Cum_Sales_Squared'])) / (
                 2 * self.pars['Cum_Sales_Squared'])  # calculate number of adopters
    m2 = (-self.pars['Cum_Sales'] - np.sqrt(
        self.pars['Cum_Sales'] ** 2 - 4 * self.pars['Intercept'] * self.pars['Cum_Sales_Squared'])) / (
                 2 * self.pars['Cum_Sales_Squared'])  # calculate number of adopters
    maximum_adopters = self.__max__(m1, m2)  # get the maximum number of adopters
    innovation_coefficient = self.pars['Intercept'] / maximum_adopters  # calculate innovation coefficient
    imitation_coefficient = self.pars['Cum_Sales_Squared'] * (-maximum_adopters)  # calculate imitation coefficient
    self.forecast = self.__bass_model__(innovation_coefficient, imitation_coefficient, self.time_range) * maximum_adopters  # save the forecast
    return maximum_adopters, innovation_coefficient, imitation_coefficient

import matplotlib.pyplot as plt

def visualize_forecast(self):
    """
    Visualize the forecasted sales using a line plot.
    
    Returns:
    - None
    """
    plt.plot(self.time_range, self.forecast, color='tomato', label='Forecasted Sales')
    plt.ylabel('Sales')
    plt.xlabel('Time')
    plt.title('Forecasted Sales using Bass Diffusion Model')
    plt.legend(loc='best')
    plt.grid()
    plt.show()

def get_maximum_value(self, value1, value2):
    """
    Get the maximum value between two numbers.
    
    Parameters:
    - value1: int or float
        First value.
    - value2: int or float
        Second value.
    
    Returns:
    - int or float
        Maximum value between value1 and value2.
    """
    if value1 > value2:
        return value1
    return value2
