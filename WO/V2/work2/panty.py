# --- imports
from rich.traceback import install
from src.ban import banner
from src.p1 import p1F

install(show_locals=True)
# ----


def main():
    banner("Work Continuation Here")
    p1F()


if __name__ == "__main__":
    main()
