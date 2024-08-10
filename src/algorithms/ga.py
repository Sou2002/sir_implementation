# Importing necessary libraries
import numpy as np
from pymoo.problems.functional import FunctionalProblem
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.optimize import minimize
from src.utils.utils import generate_sir_dataset


# Genetic Algorithm class for S-I-R model
class GeneticAlgorithm:
    '''
    A class to solve S-I-R model with Genetic Algorithm.

    Methods
    -------
    find_optima(verbose=True):
        Finds the optimum value of beta and gamma.
    '''

    def __init__(self, data: np.ndarray, N: int, I0: int = 1) -> None:
        '''
        Constructs all the necessary attributes for the GeneticAlgorithm object.

        Parameters
        ----------
        data : ndarray
            The dataset as an array format.
        N : int
            Total population.
        I0 : int, optional
            Initial number of infected people.
        '''
        # Data
        self.__data = data
        self.__I_actual, self.__R_actual = self.__data[:, 1], self.__data[:, 2]

        # Problem Environment
        self.__N: int = N
        self.__I0: int = I0
        self.__num_of_days: int = self.__data.shape[0]

        # Problem Initializtion
        self.__bounds = np.array([[0, 0],
                                  [1, 1]])
        self.__problem = FunctionalProblem(n_var=2,
                                           objs=self.__fitness_mse,
                                           xl=self.__bounds[0],
                                           xu=self.__bounds[1])

        # Algorithm
        self.__algorithm = GA(pop_size=200)

    # Evaluation Function
    def __fitness_mse(self, params: list[float]) -> float:
        '''
        Finds the fitness value of a solution.

        Parameters
        ----------
        params: list[float]
            Generated by the algorithm.

        Returns
        -------
        error: float
            Error/Fitness value of the solution.
        '''
        beta, gamma = params

        pred_data = generate_sir_dataset(N=self.__N,
                                         I0=self.__I0,
                                         num_of_days=self.__num_of_days,
                                         beta=beta,
                                         gamma=gamma)

        I_pred, R_pred = pred_data[:, 1], pred_data[:, 2]

        # Mean Absolute Error
        error: float = np.mean(np.abs(self.__I_actual - I_pred) +
                               np.abs(self.__R_actual - R_pred))
        return error

    # Call this function to get result
    def find_optima(self, verbose: bool = True) -> np.ndarray:
        '''
        Finds the optimum value of beta and gamma.

        Parameters
        ----------
        verbose: bool, optional
            Additional information per generation.

        Returns
        -------
        result: ndarray
            Resultant beta and gamma value.
        '''
        self.result = minimize(
            self.__problem, self.__algorithm, seed=1, verbose=verbose)

        return self.result.X
