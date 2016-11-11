import os
import sys
import subprocess

# Build the test extension

here = os.path.abspath(os.path.dirname(__file__))
subprocess.check_call([sys.executable, os.path.join(here, 'setup.py'), 'build_ext', '--inplace'], cwd=here)

# Test it!

from unittest import TestCase
import xtensor_python_test as xt
import numpy as np

class ExampleTest(TestCase):

    def test_example1(self):
        self.assertEqual(4, xt.example1([4, 5, 6]))

    def test_example2(self):
        x = np.array([[0., 1.], [2., 3.]])
        res = np.array([[2., 3.], [4., 5.]])
        y = xt.example2(x)
        np.testing.assert_allclose(y, res, 1e-12)

    def test_vectorize(self):
        x1 = np.array([[0, 1], [2, 3]])
        x2 = np.array([0, 1])
        res = np.array([[0, 2], [2, 4]])
        y = xt.vectorize_example1(x1, x2)
        np.testing.assert_array_equal(y, res)

    def test_readme_example1(self):
        v = np.arange(15).reshape(3, 5)
        y = xt.readme_example1(v)
        np.testing.assert_allclose(y, 1.2853996391883833, 1e-12)
