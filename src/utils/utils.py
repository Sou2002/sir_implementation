# Importing necessary libraries
import numpy as np
from typing import Any

# Function to generate the dataset
def generate_sir_dataset(N: int, I0: int, num_of_days: int, beta: float, gamma: float) -> np.ndarray[Any, int]:
    '''
    Computes the S-I-R (Suceptible-Infected-Recovered) dataset for the given parameters.

    All of the parameters are necessary otherwise it can not compute.

    # Parameters
    ------------
    N: int
        Total number of population.
    I0: int
        Initial number of infected people, can't be less than 1.
    num_of_days: int
        Calculated data upto this number of days.

    beta: float
        Transmission Rate of the disease.
    gamma: float
        Recovery Rate of the disease.

    # Returns
    ---------
    data: ndarray, dtype=int
        Returns the array of shape=(num_of_days, 3).
    '''
    S0: int = N - I0

    S: list = [S0]
    I: list = [I0]
    R: list = [0]

    for days in range(1, num_of_days):
        dS = - beta * S[days - 1] * I[days - 1] / N
        dI = (beta * S[days - 1] * I[days - 1] / N) - gamma * I[days - 1]
        dR = gamma * I[days - 1]

        S.append(S[days - 1] + dS)
        I.append(I[days - 1] + dI)
        R.append(R[days - 1] + dR)

    data = np.array([S, I, R]).T
    data = np.floor(data).astype(int)

    return data
