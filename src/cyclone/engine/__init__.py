
from abc import ABC, abstractmethod
from typing import Any, Dict

from numpy.random import default_rng
from sympy import Add, Eq, Id, Integer, Integral, Symbol, pi, cos, sin, tan, sympify


class Problem(ABC):

    def __init__(self, **kwargs: Dict[Any, Any]) -> None:
        self.rng = default_rng()

    @abstractmethod
    def __repr__(self) -> str:
        return "Problem()"

    @abstractmethod
    def check(self, response: str) -> bool:
        return False


class AdditionProblem(Problem):

    def __init__(self) -> None:

        # Ensure proper initialization by calling the super class constructor.
        super().__init__()

        # TODO: Determine the format of the AdditionProblem class.
        self.a: Integer = Integer(self.rng.poisson(4.5) + 1)
        self.b: Integer = Integer(self.rng.poisson(4.5) + 1)

        # Return the Sympy expression object, making sure to specify that it
        # should not be evaluated. Otherwise, Sympy takes care of what would
        # normally be a trivial and unproblematic simplification.
        self.statement = Add(self.a, self.b, evaluate=False)

    def __repr__(self) -> str:
        return f"AdditionProblem({self.a}, {self.b})"

    def __str__(self) -> str:
        return f"{self.a} + {self.b}"

    def check(self, response: str) -> bool:
        return False


class IntegrationProblem(Problem):
    """
    TODO: Subclass this class for each possible integration problem (i.e...
    integration by parts, u-substitution, trig substitution., etc.
    """

    def __init__(self) -> None:
        super().__init__()

        self.x = Symbol(self.rng.choice(['x', 'y', 'z', 'θ']), real=True)
        # Definite vs. Indefinite integrals are the perfect example of a subclass
        self.limits_of_integration = (self.rng.choice([0, 1]), pi / self.rng.choice([1, 2, 3, 4, 6]))
        self.statement = Integral(self.rng.choice([sin, cos, tan, Id])(self.x), (self.x, self.limits_of_integration[0], self.limits_of_integration[1]))

    def __repr__(self) -> str:
        return f"{self.statement}"

    def check(self, response: str) -> bool:
        return Eq(self.statement.doit(), sympify(response))
