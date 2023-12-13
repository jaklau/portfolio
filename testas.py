import airflow
from datetime import datetime
from os import environ
import time


print(environ['DATA_DIR'])
print(datetime.datetime.now(tz=datetime.timezone.utc))
# print(DAG)
print(airflow.__version__)
print(time.time())

testas = []


def testas1() -> None:
    """
    jdrhdfgjjdhgjdhjdghjdghj.

    :return:
    hj
    """
    print('testas')
    test2 = 2
    print(test2)

print(testas1())

class Testas:
    """
    jdrhdfgjjdhgjdhjdghjdghj.

    :return:
    hj
    """

    def __init__(self) -> None:
        self.testas = 1

    def testas1(self):
        print(self.testas)
