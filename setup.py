#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup / build configuration for Ganzabara.

This file serves two purposes:
  1. Standard setuptools packaging metadata.
  2. Nuitka build configuration (`command_options["nuitka"]`) used to produce
     a standalone, native application for Windows and Linux.

macOS / iOS are intentionally NOT supported targets. Building or compiling
this Software for MacOS or iOS is explicitly prohibited by the project
license (NCHL-1.1, Section 3.e). Attempting to run this build on macOS
(Darwin) will abort immediately.
"""

import platform
import sys
from pathlib import Path

from setuptools import find_packages, setup

# --------------------------------------------------------------------------- #
# License-enforced platform guard
# --------------------------------------------------------------------------- #
# NCHL-1.1 §3.e: "Compile or build any kind of software for MacOS or IOS" is
# a prohibited action without a commercial agreement. We refuse to proceed
# rather than silently produce an unsupported/unlicensed build artifact.
if sys.platform == "darwin" or platform.system() == "Darwin":
    sys.exit(
        "\n"
        "Building Ganzabara for macOS/iOS is not permitted.\n"
        "See LICENSE (NCHL-1.1, Section 3.e). Supported build targets are\n"
        "Windows and Linux only. Contact Vahrka for commercial licensing\n"
        "options if macOS/iOS support is required.\n"
    )

ROOT = Path(__file__).resolve().parent
README = (ROOT / "README.md").read_text(encoding="utf-8")

# --------------------------------------------------------------------------- #
# Application metadata (single source of truth, mirrors src/utils/settings.py)
# --------------------------------------------------------------------------- #
APP_NAME = "Ganzabara"
APP_VERSION = "1.0.0"
APP_FILE_VERSION = "1.0.0.0"
APP_DESCRIPTION = "Free and open-source accounting software built with PySide6."
COMPANY_NAME = "Vahrka"
ORGANIZATION_DOMAIN = "ac.soft"
COPYRIGHT = "Copyright \u00a9 2025 Vahrka. All rights reserved."

# Icons live under src/resources/images and are tracked in git (not
# generated), so they can be referenced directly at build time.
ICON_ICO = "src/resources/images/icon.ico"
ICON_PNG = "src/resources/images/icon.png"

setup(
    name=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    author="Bambi Bambier",
    author_email="secret",
    maintainer="Vahrka Team",
    maintainer_email="No-EMAIL",
    license="NCHL-1.1",
    license_files=["LICENSE"],
    url="https://github.com/Vahrka/Ganzabara",
    download_url="https://github.com/Vahrka/Ganzabara/releases",
    project_urls={
        "Homepage": "https://github.com/Vahrka/Ganzabara",
        "Repository": "https://github.com/Vahrka/Ganzabara",
        "Issues": "https://github.com/Vahrka/Ganzabara/issues",
        "Releases": "https://github.com/Vahrka/Ganzabara/releases",
        "Discussions": "https://github.com/Vahrka/Ganzabara/discussions",
    },
    keywords=[
        "accounting",
        "finance",
        "bookkeeping",
        "erp",
        "invoicing",
        "double-entry",
        "qt",
        "pyside6",
        "nuitka",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Other Audience",
        "License :: Free To Use But Restricted",
        "Natural Language :: English",
        "Natural Language :: Persian",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Office/Business",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Software Development :: User Interfaces",
    ],
    python_requires=">=3.14",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "fpdf>=1.7.2",
        "jalali_core>=1.0.0",
        "jdatetime>=5.3.0",
        "Jinja2>=3.1.6",
        "MarkupSafe>=3.0.3",
        "numpy>=2.5.1",
        "ordered-set>=4.1.0",
        "pandas>=3.0.3",
        "patchelf>=0.17.2.4; sys_platform == 'linux'",
        "peewee>=4.1.2",
        "PySide6>=6.11.1",
        "python-dateutil>=2.9.0.post0",
        "pytz>=2026.2",
        "PyYAML>=6.0.3",
        "six>=1.17.0",
        "tzdata>=2026.3",
        "zstandard>=0.25.0",
    ],
    extras_require={
        "build": [
            "nuitka>=2.7",
            "ordered-set>=4.1.0",
            "zstandard>=0.25.0",
        ],
    },
    # ----------------------------------------------------------------- #
    # Nuitka build configuration
    #
    # Invoke with:  python setup.py build_nuitka   (or bdist_nuitka)
    # Target modes: --mode=standalone for Windows and Linux ONLY.
    # macOS/iOS are unsupported and blocked above.
    # ----------------------------------------------------------------- #
    command_options={
        "nuitka": {
            # Entry point ------------------------------------------------
            # main.py lives in src/ and uses sibling absolute imports
            # (e.g. `from app import Application`), so src/ must be on
            # the module search path at compile time (set PYTHONPATH=src
            # or run from within src/ — see CI workflows).
            "--mode": ("setup.py", "standalone"),
            "--follow-imports": ("setup.py", None),

            # Qt / PySide6 -------------------------------------------------
            "--enable-plugin": ("setup.py", "pyside6"),

            # Make sure our own packages/modules are always embedded, even
            # ones only reached through a dynamic/plugin import, or stub
            # packages not yet wired into any static import chain.
            "--include-module": ("setup.py", ["app", "main_window"]),
            "--include-package": (
                "setup.py",
                [
                    "controllers",
                    "data_models",
                    "models",
                    "plugins",
                    "services",
                    "ui",
                    "utils",
                    "widgets",
                ],
            ),

            # Output ----------------------------------------------------
            "--output-filename": ("setup.py", APP_NAME),
            "--remove-output": ("setup.py", None),
            "--assume-yes-for-downloads": ("setup.py", None),

            # Optimization ------------------------------------------------
            "--lto": ("setup.py", "yes"),
            "--jobs": ("setup.py", "8"),
            "--python-flag": (
                "setup.py",
                ["isolated", "no_docstrings"],
            ),

            # Metadata (shown in Windows file properties / Linux desktop
            # metadata) --------------------------------------------------
            "--company-name": ("setup.py", COMPANY_NAME),
            "--product-name": ("setup.py", APP_NAME),
            "--file-version": ("setup.py", APP_FILE_VERSION),
            "--product-version": ("setup.py", APP_FILE_VERSION),
            "--file-description": ("setup.py", APP_DESCRIPTION),
            "--copyright": ("setup.py", COPYRIGHT),
            "--trademarks": ("setup.py", APP_NAME),

            # Windows-specific (no effect on other platforms) -----------
            "--windows-console-mode": ("setup.py", "disable"),
            "--windows-icon-from-ico": ("setup.py", ICON_ICO),

            # Linux-specific (no effect on other platforms) -------------
            "--linux-icon": ("setup.py", ICON_PNG),
        },
    },
)