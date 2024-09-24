from src.ban import banner
from rich.traceback import install
from src.p1 import m_F1

install(show_locals=True)


def main():
    banner("Continuing work from \n V1 - p1.py")
    m_F1()


if __name__ == "__main__":
    main()
