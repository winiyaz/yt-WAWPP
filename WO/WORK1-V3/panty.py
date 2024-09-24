# Entry point into application actual code will be in its own subdirectory
from src.p1 import m_F1
from src.p2 import m_F2
from src.p3 import m_F3
from src.p4 import m_F4
from src.ban import banner
from rich.traceback import install

install(show_locals=True)


def main():
    print("Hello from work1!")
    banner("Running m_F3 Using DIR as a list \n Looping through list of website")
    m_F4()


if __name__ == "__main__":
    main()
