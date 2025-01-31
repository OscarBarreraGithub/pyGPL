from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "pyGPL.pyGPL",
        ["bindings/fastgpl_bind.cpp"],
        include_dirs=[pybind11.get_include(), "/usr/local/include"],
        libraries=["FastGPL"],
        library_dirs=["/usr/local/lib"],
        extra_compile_args=["-std=c++17", "-O3", "-shared", "-fPIC"]
    )
]

setup(
    name="pyGPL",
    version="0.1",
    packages=["pyGPL"],
    ext_modules=ext_modules,
    install_requires=["pybind11"],
)

