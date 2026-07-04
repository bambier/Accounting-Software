===============================
Contributing to AccounterPro
===============================

Thank you for your interest in contributing to **AccounterPro** - the free
open-source accounting software for small businesses[reference:4]. We welcome
contributions of all kinds: code, documentation, bug reports, design ideas, and
translations.

Please read this guide carefully. It explains our standards and processes, and
points you to the existing architecture documentation for details.

---

Table of Contents
=================

1. `Code of Conduct <#code-of-conduct>`_
2. `Getting Started <#getting-started>`_
3. `Project Architecture <#project-architecture>`_
4. `Development Environment <#development-environment>`_
5. `Coding Standards <#coding-standards>`_
6. `Commit & Pull Request Guidelines <#commit--pull-request-guidelines>`_
7. `Testing <#testing>`_
8. `Documentation <#documentation>`_
9. `Reporting Issues <#reporting-issues>`_
10. `Licensing & DCO <#licensing--dco>`_
11. `Need Help? <#need-help>`_

---

Code of Conduct
===============

We are committed to providing a friendly, safe, and welcoming environment for
all contributors. Please read and follow our full `Code of Conduct
<CODE_OF_CONDUCT.rst>`_. By participating, you agree to abide by its terms.

---

Getting Started
===============

If you are new to the project:

1. **Fork** the repository and **clone** your fork locally.
2. Set up your development environment (see `Development Environment`_).
3. Run the application to verify everything works.
4. Look for issues labelled **good first issue** or **help wanted** in the
   `issue tracker <https://github.com/Vahrka/Accounting-Software/issues>`_.

---

Project Architecture
====================

The software follows a **Model-View-Controller (MVC)** pattern, built with
**PySide6** for native cross-platform performance[reference:5]. The full architecture
is documented in the following files, available in the ``STRUCTURE/`` folder of
the repository[reference:6][reference:7]:

- **`STRUCTURE/STRUCTURE.mermaid`** - Complete class diagram covering all
  models, controllers, services, and UI views (core accounting, business
  management, technical layers, and security).
- **`STRUCTURE/VIEW/VIEWS.mermaid`** - Detailed UI view hierarchy, showing all
  pages, sub-views, and their relationships.
- **`STRUCTURE/STRUCTURE.md`** - Recommended folder structure and organisation
  of the source code.
- **`STRUCTURE/recommended.md`** - Additional guidance on project layout.

Please refer to these files for a comprehensive understanding of the codebase.
The key layers are:

- **UI (Views)** - PySide6 widgets grouped by feature (invoices, accounting,
  inventory, payroll, banking, settings).
- **Controllers** - Business logic, orchestrating services and updating views.
- **Services** - Low-level operations (database, encryption, backup, reporting,
  OCR, bank feeds).
- **Models** - Business entities (Account, Transaction, Invoice, etc.).
- **Qt Data Models** - Table/tree models that feed data to views.

When adding a new feature, follow the structure outlined in `STRUCTURE.md`.

---

Development Environment
=======================

Prerequisites
-------------

- Python 3.10 or higher
- `pip` and `virtualenv` (or `venv`)
- Git
- Optional: `Tesseract <https://github.com/tesseract-ocr/tesseract>`_ (for OCR)
- Optional: PostgreSQL (for testing the PostgreSQL backend)

Setup
-----

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/Vahrka/Accounting-Software
      cd Accounting-Software

2. Create and activate a virtual environment:

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

4. Run the application:

   .. code-block:: bash

      python3 main.py

Database
--------

By default, SQLite is used. To test with PostgreSQL, adjust the configuration
accordingly.

---

Coding Standards
================

- **Python**: Follow `PEP 8`_. Use `black`_ for formatting (default settings).
  Run ``black .`` before committing.
- **Type Hints**: All function and method signatures **must** include type
  hints.
- **Docstrings**: Use Google style docstrings for all public modules, classes,
  and functions.
- **Qt/PySide6**: Class names in ``CamelCase``; slot methods prefixed with
  ``on_``. Keep UI layout separate from business logic.
- **Imports**: Group as: standard library, third-party, local modules.
- **Line length**: 88 characters (black default).

Also run `isort`_ to sort imports: ``isort .``.

.. _PEP 8: https://peps.python.org/pep-0008/
.. _black: https://black.readthedocs.io/
.. _isort: https://pycqa.github.io/isort/

---

Commit & Pull Request Guidelines
================================

Commit Messages
---------------

We use `Conventional Commits`_. Format:

.. code-block::

   <type>(<scope>): <subject>
   <BLANK LINE>
   <body>
   <BLANK LINE>
   <footer>

Common types: ``feat``, ``fix``, ``docs``, ``style``, ``refactor``, ``test``, ``chore``.

Example:

.. code-block::

   feat(invoices): add OCR scanning for receipts

   Implemented receipt scanning using Tesseract. Added ReceiptScanView
   and integrated with InvoiceController to auto-match scanned receipts.

   Closes #123

.. _Conventional Commits: https://www.conventionalcommits.org/

Branching
---------

- ``main`` - stable, release-ready branch. All changes come via pull requests.
- Feature branches: name as ``feature/short-description`` or ``fix/issue-number``.

Pull Requests
-------------

1. Open a pull request against ``main``.
2. Fill out the PR template (provided in the repository).
3. Ensure all CI checks pass (linting, tests, build).
4. Request review from at least one maintainer.
5. After approval, a maintainer will merge your PR.

---

Testing
=======

We use `pytest`_ for testing. All new features must include tests.

- Unit tests: under ``tests/unit/``.
- Integration tests: under ``tests/integration/``.
- UI tests: under ``tests/ui/`` (using `pytest-qt`_).

Run the full suite with:

.. code-block:: bash

   pytest

Write tests that are clear, maintainable, and cover edge cases.

.. _pytest: https://docs.pytest.org/
.. _pytest-qt: https://pytest-qt.readthedocs.io/

---

Documentation
=============

- **Code**: Inline docstrings (Google style) for all public APIs.
- **User Guide**: We maintain a separate user manual in the ``docs/`` folder.
- **Architecture**: See the files mentioned in `Project Architecture`_.
- **README**: Keep the top-level README up-to-date with setup and basic usage.

When you add or change a feature, update the relevant documentation.

---

Reporting Issues
================

Use the `GitHub issue tracker <https://github.com/Vahrka/Accounting-Software/issues>`_
to report bugs or request features. Please include:

- A clear and descriptive title.
- Steps to reproduce the issue.
- Expected and actual behaviour.
- Screenshots or logs if applicable.
- Environment details (OS, Python version, database type, etc.).

---

Licensing & DCO
===============

This project is licensed under **strict open-source terms**[reference:8]. By
contributing, you agree that your contributions will be licensed under the same
terms.

We require a **Developer Certificate of Origin (DCO)** for all contributions.
Each commit must include a ``Signed-off-by`` line (you can use ``git commit -s``).
This certifies that you have the right to submit the contribution and agree to
the DCO terms (see `DCO 1.1 <https://developercertificate.org/>`_).

---

Need Help?
==========

If you have any questions or need guidance, feel free to:

- Open a discussion on the `GitHub Discussions <https://github.com/Vahrka/Accounting-Software/discussions>`_ page.
- Reach out to the maintainers via the repository.

We look forward to your contributions!