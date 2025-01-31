#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/complex.h>
#include <complex>
#include "FastGPL.h"

namespace py = pybind11;

// Function to evaluate any GPL G(a1, a2, ..., an; x) with optional signs
std::complex<double> GPL(std::vector<std::complex<double>> indices, double x, std::vector<int> signs = {}) {
    if (signs.empty()) {
        signs.resize(indices.size(), 1);  // Default all signs to +1 if not provided
    } else if (signs.size() != indices.size()) {
        throw std::invalid_argument("The number of signs must match the number of indices.");
    }

    return FastGPL::G(indices, signs, x);
}

// Pybind11 module
PYBIND11_MODULE(pyGPL, m) {
    m.doc() = "Python bindings for FastGPL";
    
    m.def("GPL", &GPL, 
          "Evaluate generalized polylogarithm G(a1, ..., an; x) with optional signs",
          py::arg("indices"), py::arg("x"), py::arg("signs") = std::vector<int>());
}

