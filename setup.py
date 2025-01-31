from setuptools import setup, Extension
import pybind11
import os

# Require a Conda environment
CONDA_PREFIX = os.getenv("CONDA_PREFIX")
if not CONDA_PREFIX:
    raise RuntimeError("FastGPL must be installed inside a Conda environment. Run `conda activate pyGPL` first.")

ext_modules = [
    Extension(
        "pyGPL.pyGPL",
        ["bindings/fastgpl_bind.cpp"],
        include_dirs=[pybind11.get_include(), f"{CONDA_PREFIX}/include"],
        libraries=["FastGPL"],
        library_dirs=[f"{CONDA_PREFIX}/lib"],
        extra_link_args=[f"-Wl,-rpath,{CONDA_PREFIX}/lib"],
        extra_compile_args=["-std=c++17", "-O3", "-fPIC"]
    )
]

setup(
    name="pyGPL",
    version="0.1",
    packages=["pyGPL"],
    ext_modules=ext_modules,
    install_requires=["pybind11"],
)

