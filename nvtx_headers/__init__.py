"""Top-level package for nvtx-headers."""

__author__ = """Jonathan Dekhtiar"""
__email__ = 'jdekhtiar@nvidia.com'
__version__ = '0.1.0'

import os
import requests

import pathlib

__all__ = [
    "get_include_dir"
]

_HEADER_DIR = "include"
_HEADERS_FILES = [
    ("nvtx3.hpp", "https://raw.githubusercontent.com/jrhemstad/nvtx_wrappers/master/nvtx3.hpp")
]


def get_include_dir():
    return os.path.join(pathlib.Path(__file__).parent.absolute(), _HEADER_DIR)


for hdr_file, hdr_url in _HEADERS_FILES:
    hdr_path = os.path.join(get_include_dir(), hdr_file)
    if not os.path.exists(hdr_path):
        hdr_data = requests.get(hdr_url, allow_redirects=True)
        open(hdr_path, 'wb').write(hdr_data.content)
