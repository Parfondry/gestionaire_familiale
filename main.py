from datetime import *
import os
from task import *
from reward import *
from task_history import *
from user import *
from children import Children
from datamanager import DataManager
from interface import *


if __name__ == "__main__":
    cls()
    data = DataManager()
    data.load_data()
try :
    user=connection(data)
    cls()
    menu(user,data)
    print(user.name)
except Exception as e:
    print("")
