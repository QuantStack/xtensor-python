# xtensor-python

[![Travis](https://travis-ci.org/QuantStack/xtensor.svg?branch=master)](https://travis-ci.org/QuantStack/xtensor-python)
[![Appveyor](https://ci.appveyor.com/api/projects/status/qx61nsg4ebxnj8s9?svg=true)](https://ci.appveyor.com/project/QuantStack/xtensor-python)
[![Documentation](http://readthedocs.org/projects/xtensor-python/badge/?version=latest)](https://xtensor-python.readthedocs.io/en/latest/?badge=latest)

Python bindings for the [xtensor](https://github.com/QuantStack/xtensor) C++ multi-dimensional array library.

 - `xtensor` is a C++ library for multi-dimensional arrays enabling numpy-style broadcasting and lazy computing.
 - `xtensor-python` enables inplace use of numpy arrays with all the benefits from `xtensor`

     - C++ universal function and broadcasting 
     - STL - compliant APIs.

The Python bindings for `xtensor` are based on the [pybind11](https://github.com/pybind/pybind11/) C++ library, which enables seemless interoperability between C++ and Python.

## Installation

`xtensor-python` is a header-only library. We provide a package for the conda package manager.

```bash
conda install -c conda-forge xtensor-python
```

## Usage

### Example 1: Use an algorithm of the C++ library on a numpy array inplace.

**C++ code**

```cpp
#include <numeric>                        // Standard library import for std::accumulate
#include "pybind11/pybind11.h"            // Pybind11 import to define Python bindings
#include "xtensor/xmath.hpp"              // xtensor import for the C++ universal functions
#include "xtensor-python/pyarray.hpp"     // Numpy bindings

double sum_of_sines(xt::pyarray<double> &m)
{
    auto sines = xt::sin(m);  // sines does not actually hold any value, which are only computed upon access
    return std::accumulate(sines.begin(), sines.end(), 0.0);
}

PYBIND11_PLUGIN(xtensor_python_test)
{
    pybind11::module m("xtensor_python_test", "Test module for xtensor python bindings");

    m.def("sum_of_sines", sum_of_sines, "Computes the sum of the sines of the values of the input array");

    return m.ptr();
}
```

**Python Code**

```python
import numpy as np
import xtensor_python_test as xt

a = np.arange(15).reshape(3, 5)
s = xt.sum_of_sines(v)
s
```

**Outputs**

```
1.2853996391883833
``` 

### Example 2: Create a universal function from a C++ scalar function

**C++ code**

```cpp
#include "pybind11/pybind11.h"
#include "xtensor-python/pyvectorize.hpp"
#include <numeric>
#include <cmath>

namespace py = pybind11;

double scalar_func(double i, double j)
{
    return std::sin(i) - std::cos(j);
}

PYBIND11_PLUGIN(xtensor_python_test)
{
    py::module m("xtensor_python_test", "Test module for xtensor python bindings");

    m.def("vectorized_func", xt::pyvectorize(scalar_func), "");

    return m.ptr();
}
```

**Python Code**

```python
import numpy as np
import xtensor_python_test as xt

x = np.arange(15).reshape(3, 5)
y = [1, 2, 3, 4, 5]
z = xt.vectorized_func(x, y)
z
```

**Outputs**

```
[[-0.540302,  1.257618,  1.89929 ,  0.794764, -1.040465],
 [-1.499227,  0.136731,  1.646979,  1.643002,  0.128456],
 [-1.084323, -0.583843,  0.45342 ,  1.073811,  0.706945]]
``` 

## Installation

We provide a package for the conda package manager.

```bash
conda install -c conda-forge xtensor-python
```

This will pull the dependencies to xtensor-python, that is `pybind11` and `xtensor`.

## Project cookiecutter

A template for a project making use of `xtensor-python` is available in the form of a cookie cutter [here](https://github.com/QuantStack/xtensor-cookiecutter).

This project is meant to help library authors get started with the xtensor python bindings.

It produces a project following the best practices for the packaging and distribution of Python extensions based on `xtensor-python`, including a `setup.py` file and a conda recipe.

## Building and Running the Tests

Testing `xtensor-python` requires `pytest`

  ``` bash
  py.test .
  ```

To pick up changes in `xtensor-python` while rebuilding, delete the `build/` directory. 

## Building the HTML Documentation

`xtensor-python`'s documentation is built with three tools

 - [doxygen](http://www.doxygen.org)
 - [sphinx](http://www.sphinx-doc.org)
 - [breathe](https://breathe.readthedocs.io)

While doxygen must be installed separately, you can install breathe by typing

```bash
pip install breathe
``` 

Breathe can also be installed with `conda`

```bash
conda install -c conda-forge breathe
```

Finally, build the documentation with

```bash
make html
```

from the `docs` subdirectory.

## License

We use a shared copyright model that enables all contributors to maintain the
copyright on their contributions.

This software is licensed under the BSD-3-Clause license. See the [LICENSE](LICENSE) file for details.
