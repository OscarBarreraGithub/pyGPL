# pyGPL (Python Bindings for FastGPL)

This repository provides **Python bindings for [FastGPL](https://github.com/llyang/FastGPL)**, 
allowing users to evaluate **Generalized Polylogarithms (GPLs)** in Python without manually compiling C++.

## Acknowledgments
This project is based on **FastGPL**, developed by:
- **Yuxuan Wang**, **Li Lin Yang**, and **Bin Zhou**  
- Original repository: [FastGPL on GitHub](https://github.com/llyang/FastGPL)  
For usage, please refer to [arXiv:2112.04122]

FastGPL is a **C++ library for fast GPL evaluation**, and this project only provides a **Python wrapper using Pybind11**.

## Installation

Clone the repository and install using `pip`:

```bash
git clone https://github.com/OscarBarreraGithub/pyGPL.git
cd pyGPL
pip install .
