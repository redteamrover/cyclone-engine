
from unittest import TestCase

from cyclone.engine import AdditionProblem, Problem


class TestProblem(TestCase):

    def test_problem_cannot_be_instatiated(self):
        self.assertRaises(TypeError, Problem)


class TestAdditionProblem(TestCase):

    def setUp(self) -> None:
        self.problem = AdditionProblem()
        self.answer = self.problem.a + self.problem.b

    def test_for_correctness(self):
        self.assertTrue(self.answer, self.problem.a + self.problem.b)
        self.assertFalse(self.answer + 1 == self.problem.a + self.problem.b)

    @classmethod
    def setUpClass(cls):
        pass
