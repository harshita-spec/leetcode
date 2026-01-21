# Copilot / AI Agent Instructions for this repository

This repository is a collection of standalone Python LeetCode solutions organized by topic. The guidance below helps AI coding agents be productive immediately without assumptions about hidden tooling.

- Repo layout: top-level folders are topic namespaces (for example `array/`, `binarysearch/`, `linkedlistt/`, `string/`). Each file is typically a single-solution script (e.g. `array/twosum.py`, `binarysearch/searchinrotatedarray.py`).
- Running code: most files execute example inputs at module load (they lack `if __name__ == "__main__"` guards). Do NOT import solution modules as libraries — running them will execute example code. Run a file explicitly with `python3 path/to/file.py`.
- Dependencies: no external dependencies or requirements files were found. Assume only the Python standard library is used.

- Coding patterns to follow when editing or adding files:
  - Keep solutions self-contained in their file. Many files define helper functions or classes then run a small example at the bottom.
  - Naming: filenames are lowercase with underscores, and directories reflect problem categories (match existing naming when adding files).
  - Output style: many scripts print results directly (e.g. `print(result)` in `array/twosum.py`). Some return unconventional types (for example `twosum` returns "yes"/"no"); preserve local project behavior unless asked to standardize.
  - Control flow: be aware that functions may call `sorted()` or mutate inputs locally (see `array/twosum.py`). Respect existing in-place vs copy semantics.

- Important gotchas for agents:
  - No tests or CI were detected — changes that add imports or change runtime behavior should be validated by running the modified script directly.
  - Because many modules run on import, avoid refactoring by moving code into new modules without adding `if __name__ == "__main__"` guards first.
  - Several scripts create example data inline (see `linkedlistt/singlylinkedlist.py`), so updates to example blocks must remain side-effect free for the rest of the repository.

- Quick examples:
  - To run the linked-list demo: `python3 linkedlistt/singlylinkedlist.py`.
  - To run a binary-search example: `python3 binarysearch/searchinrotatedarray.py`.

- When making larger changes (refactors or adding helpers):
  - Add `if __name__ == "__main__"` guards around example/demo code before converting functions into importable helpers.
  - Keep new helper modules minimal and document expected inputs/outputs at the top of the file.

If anything here is unclear or you want conventions tightened (for example standardized return types, tests, or a runner script), tell me which area to expand and I will update this file.
