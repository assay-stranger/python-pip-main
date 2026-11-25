"""Cold-run fixture: one pinned dependency, one call into it."""
import requests


def main() -> None:
    print(requests.utils.default_user_agent())


if __name__ == "__main__":
    main()
