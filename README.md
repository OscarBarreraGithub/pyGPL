# pyGPL

This repository provides **Python bindings for [FastGPL](https://github.com/llyang/FastGPL)**, allowing users to evaluate **Generalized Polylogarithms (GPLs)** in Python without manually compiling C++.

Generalized Polylogarithms (GPLs) are a family of special functions defined by iterated integrals of the form:

$$G(a_1, a_2, \dots, a_n; x) = \int_0^x \frac{dt}{t - a_1} G(a_2, \dots, a_n; t)$$

where the recursion starts with $G($ $;$ $x) = 1$. These functions naturally generalize classical polylogarithms and arise frequently in the evaluation of Feynman integrals.


---

## Installation

### 1. **Conda Required**

**Conda is required to install `pyGPL`.** If you do not have Conda installed, you must install it first. The recommended way is to install [Miniconda](https://docs.conda.io/en/latest/miniconda.html). Conda helps manage dependencies like `pybind11`, `cmake`, and `librhash`, ensuring compatibility and preventing version conflicts. This is especially important on macOS, where librhash can cause build failures due to missing or mismatched shared libraries

Once installed, create and activate a new Conda environment:

```bash
conda create -n pygpl
conda activate pygpl
```

### 2. Clone the Repository

Clone the `pyGPL` repository from GitHub:

```bash
git clone https://github.com/OscarBarreraGithub/pyGPL.git
cd pyGPL
```

### 3. Install Dependencies

Install the required dependencies using Conda:

```bash
conda install -c conda-forge pybind11 cmake
```

### 4. Build and Install `pyGPL`

Compile and install the package:

```bash
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=$CONDA_PREFIX ..
make
make install
```

Return to the main directory and install the Python package:

```bash
cd ..
pip install .
```

### 5. Potential `librhash` Issue (macOS)

If you encounter issues with `librhash` when running `CMake`, this is most likely due to a conflict in `librhash` version between Cmake and Conda.

To verify the available `librhash` shared libraries in your Conda environment, run:

```bash
ls -l $CONDA_PREFIX/lib/librhash*.dylib
```

To check which version CMake is trying to load:

```bash
otool -L $(which cmake)
```

It is possible that CMake is expecting `librhash.0.dylib` while Conda has updated to `librhash.1.dylib`. This is fixed by creating a symbolic link:

```bash
ln -s $CONDA_PREFIX/lib/librhash.1.dylib $CONDA_PREFIX/lib/librhash.0.dylib
```

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
