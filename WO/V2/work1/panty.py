from src.ban import banner
from rich.traceback import install
from src.p2 import m_F2

install(show_locals=True)


def main():
    banner("Execute p2.py - Loops through list of urls and creates screenshots")
    m_F2()


if __name__ == "__main__":
    main()
