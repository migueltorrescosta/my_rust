import os
from dataclasses import dataclass
from setuptools_rust import Binding, RustExtension
from typing import Any, Dict


# Based on https://github.com/matrix-org/synapse/blob/develop/build_rust.py
def build(setup_kwargs: Dict[str, Any]) -> None:
    setup_kwargs.setdefault("rust_extensions", [])
    extension = RustExtension(
        target="my.rust.cluster",
        path="my/rust/bounding_box/Cargo.toml",
        binding=Binding.PyO3,
        py_limited_api=True,
        debug=False,
    )
    setup_kwargs["rust_extensions"].append(extension)
    setup_kwargs["zip_safe"] = False
