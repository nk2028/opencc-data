from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from setuptools import setup
from setuptools.command.build_py import build_py as _build_py


ROOT = Path(__file__).parent


def read_package_json() -> dict:
    return json.loads((ROOT / "package.json").read_text(encoding="utf-8"))


def read_long_description() -> str:
    def clean_language_link(text: str) -> str:
        lines = [
            line
            for line in text.splitlines()
            if line not in {"[繁體中文](README.zh-TW.md)", "[English](README.md)"}
        ]
        return "\n".join(lines).strip()

    english = clean_language_link((ROOT / "README.md").read_text(encoding="utf-8"))
    traditional_chinese = clean_language_link(
        (ROOT / "README.zh-TW.md").read_text(encoding="utf-8")
    )
    return f"{english}\n\n---\n\n{traditional_chinese}\n"


def python_version(npm_version: str) -> str:
    if re.fullmatch(r"\d+\.\d+\.\d+", npm_version):
        return npm_version

    dated_next = re.fullmatch(r"(\d+\.\d+\.\d+)-next\.(\d{8})", npm_version)
    if dated_next:
        return f"{dated_next.group(1)}.dev{dated_next.group(2)}"

    numbered_next = re.fullmatch(r"(\d+\.\d+\.\d+)-next\.(\d+)", npm_version)
    if numbered_next:
        return f"{numbered_next.group(1)}.dev{numbered_next.group(2)}"

    raise ValueError(
        f"{npm_version!r} is not a supported PyPI version. "
        "Use a release version like 1.3.2 or a next prerelease like "
        "1.4.0-next.20260628."
    )


class build_py(_build_py):
    def run(self) -> None:
        super().run()
        package_root = Path(self.build_lib) / "opencc_data"
        self.copy_tree(ROOT / "data", package_root / "data")
        self.copy_tree(ROOT / "test-data", package_root / "test_data")

    @staticmethod
    def copy_tree(src: Path, dst: Path) -> None:
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)


package_json = read_package_json()

setup(
    name="opencc-data",
    version=python_version(package_json["version"]),
    description="OpenCC dictionary data, configs, and test data",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    author="The Ngiox Khyen 2028 Project",
    license="Apache-2.0",
    url="https://github.com/nk2028/opencc-data",
    project_urls={
        "Homepage": "https://github.com/nk2028/opencc-data",
        "Bug Tracker": "https://github.com/nk2028/opencc-data/issues",
        "Source": "https://github.com/nk2028/opencc-data",
    },
    packages=["opencc_data"],
    include_package_data=True,
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: Chinese (Traditional)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Text Processing :: Linguistic",
    ],
    cmdclass={"build_py": build_py},
)
