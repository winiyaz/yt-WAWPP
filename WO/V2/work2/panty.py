# --- imports
from rich.traceback import install
from src.ban import banner
from src.p1 import p1F
from src.p12 import p12F

install(show_locals=True)
# ----


def main():
    banner("Work Continuation Here")
    p12F()


if __name__ == "__main__":
    main()
