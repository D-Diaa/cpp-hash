from setuptools import setup, Extension
from torch.utils import cpp_extension
import os

# Get the path to the Conda environment
conda_env_path = os.environ.get('CONDA_PREFIX', '')

# Construct the library directory path
lib_dir = os.path.join(conda_env_path, 'lib')

setup(
    name='hash_cpp',
    ext_modules=[
        cpp_extension.CUDAExtension(
            'hash_cpp',
            ['hash.cpp', 'hash_kernel.cu'],
            libraries=["ssl", "crypto"],
            library_dirs=["/usr/lib", lib_dir],
        )
    ],
    cmdclass={'build_ext': cpp_extension.BuildExtension}
)
