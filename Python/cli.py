# Backwards-compatible shim: delegate CLI to `library.cli`
from library.cli import main  # type: ignore

if __name__ == "__main__":
    main()
