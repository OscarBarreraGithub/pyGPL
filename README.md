# pyGPL

This repository provides **Python bindings for [FastGPL](https://github.com/llyang/FastGPL)**, allowing users to evaluate **Generalized Polylogarithms (GPLs)** in Python without manually compiling C++.

Generalized Polylogarithms (GPLs) are a family of special functions defined by iterated integrals of the form:

$$G(a_1, a_2, \dots, a_n; x) = \int_0^x \frac{dt}{t - a_1} G(a_2, \dots, a_n; t)$$

where the recursion starts with $G($ $;$ $x) = 1$. These functions naturally generalize classical polylogarithms and arise frequently in the evaluation of Feynman integrals.


---

## Requirements

### 1. C++ Compiler (Clang for macOS)
Since `pyGPL` includes a **C++ extension**, you must have a C++ compiler installed.  
On **macOS**, check if you have **Xcode Command Line Tools** installed by running:

```bash
xcode-select --version
```

If it’s not installed, run:
```bash
xcode-select --install
```

For **Linux**, install `g++`:
```bash
sudo apt install g++  # Debian/Ubuntu
```

---

### 2. Pybind11
The package **requires Pybind11**. 

To install via conda,
```bash
conda install -c conda-forge pybind11 
```

If you prefer to install it with pip, run:
```bash
pip install pybind11
```

---

## Installation

*Ensure you have pybind11 and a C++ compiler installed.*

Clone the repository and install the package using `pip`
   ```bash
   git clone https://github.com/OscarBarreraGithub/pyGPL.git
   cd pyGPL
   pip install .
   ```

---

## Usage

Once installed, you can import and use `pyGPL` in Python:
```python
import pyGPL
```

To evaluate the Generalized Polylogarithm **G**[1, 4, 2, x] at x = 1.3, use:

```python
pyGPL.GPL([complex(z) for z in [1, 4, 2]], 1.3)
```

See example usage in [`pyGPL/Example/`](pyGPL/Example/).


---

## Acknowledgments
This project is based on **FastGPL**, developed by:
- **Yuxuan Wang**, **Li Lin Yang**, and **Bin Zhou**  
- Original repository: [FastGPL on GitHub](https://github.com/llyang/FastGPL)  
- For more details, see [arXiv:2112.04122](https://arxiv.org/abs/2112.04122)

FastGPL is a **C++ library for fast GPL evaluation**, and this project provides a **Python wrapper using Pybind11**.

---
