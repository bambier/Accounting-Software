# Contributing to AccounterPro

First, thank you for considering contributing to AccounterPro.

Our goal is to build a clean, maintainable, cross-platform accounting application with a modular architecture, high code quality, and long-term maintainability.

Whether you are fixing bugs, improving documentation, adding features, or reviewing pull requests, your contributions are appreciated.

---

# Code of Conduct

Please be respectful and professional when interacting with other contributors.

Constructive criticism is welcome.
Personal attacks, harassment, discrimination, or hostile behavior will not be tolerated.

---

# Before You Start

Before beginning significant work:

- Search existing Issues to avoid duplicate work.
- Open an Issue to discuss large features before implementing them.
- Keep pull requests focused on a single change whenever possible.

---

# Development Philosophy

We prioritize:

- Readable code over clever code
- Simplicity over unnecessary abstraction
- Modular design
- Long-term maintainability
- Consistent architecture
- Cross-platform compatibility

Every contribution should improve the project without increasing unnecessary complexity.

---

# Project Architecture

The project follows a modular architecture.

Each component has a single responsibility.

Examples include:

- GUI
- Core
- Database
- Plugins
- Utilities
- Resources

When adding new functionality:

- place code in the correct module
- avoid circular imports
- avoid mixing UI logic with business logic
- avoid putting unrelated utilities into existing files

Please review the project structure inside the `STRUCTURE/` directory before making architectural changes [See Here] (https://github.com/bambier/Accounting-Software/tree/main/STRUCTURE).

---

# Directory Organization

New code should follow the architectural guidelines documented in [See Here] (https://github.com/bambier/Accounting-Software/tree/main/STRUCTURE):

```
STRUCTURE/
```

including:

- STRUCTURE.mermaid
- VIEW/
- recommended.md

These documents describe the intended long-term organization of the project.

If your contribution requires architectural changes, please discuss them in an Issue first.

---

# Coding Style

## Python

Follow:

- PEP 8
- PEP 257
- Type hints whenever practical

Example:

```python
def load_plugin(path: Path) -> Plugin:
    ...
```

Avoid:

- unnecessary global variables
- deeply nested logic
- duplicated code
- wildcard imports

Prefer:

- descriptive names
- small functions
- reusable components
- explicit imports

---

# GUI Guidelines

The application is built with PySide6.

GUI code should:

- remain responsive
- separate presentation from business logic
- avoid blocking the UI thread
- avoid embedding database logic directly inside widgets

Business operations should be delegated to the appropriate backend components.

---

# Database Changes

If your contribution modifies the database:

- maintain backward compatibility whenever possible
- document schema changes
- keep models consistent
- avoid breaking existing installations

---

# Plugin System

The project contains a plugin framework.

Plugin contributions should:

- inherit from the provided base classes
- follow the plugin template
- avoid modifying the plugin loader unnecessarily

New plugins should remain independent of core functionality whenever possible.

---

# Documentation

Documentation improvements are always welcome.

Please update documentation whenever you:

- introduce new features
- rename components
- modify architecture
- change public APIs

Good documentation is considered part of the contribution.

---

# Commit Messages

Write clear commit messages.

Good:

```
Add invoice filtering by customer
```

Good:

```
Fix plugin loading on Windows
```

Avoid:

```
update
```

```
fix stuff
```

```
changes
```

---

# Pull Requests

Before opening a Pull Request (PR):

- ensure the application starts successfully
- remove debugging code
- remove unused imports
- update documentation if needed
- keep the PR focused on a single topic

A good pull request explains:

- what changed
- why it changed
- any limitations
- screenshots (for UI changes)

---

# Feature Requests

Feature requests are welcome.

Please explain:

- the problem
- the proposed solution
- possible alternatives
- expected user benefit

---

# Bug Reports

Include as much information as possible:

- operating system
- Python version
- application version
- reproduction steps
- expected behavior
- actual behavior
- screenshots (if applicable)
- traceback (if available)

---

# What We're Looking For

Contributions are especially welcome in:

- Accounting features
- Reporting
- Inventory management
- Payroll
- Banking
- OCR improvements
- Plugin ecosystem
- Performance optimization
- UI/UX improvements
- Documentation
- Testing
- Localization
- Accessibility

---

# License

By contributing to this repository, you agree that your contributions are licensed under the same license as the project.

You confirm that you have the legal right to submit the contributed code.

---

# Questions

If you are unsure whether something belongs in the project, please open an Issue before investing significant development time.

We would rather discuss a proposal early than reject a large pull request later.

Thank you for helping improve AccounterPro.