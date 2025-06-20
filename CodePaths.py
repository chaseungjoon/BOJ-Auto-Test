import os

py_path = os.getenv("PY_PATH")
cpp_path = os.getenv("CPP_PATH").rsplit('.', 1)[0]
c_path = os.getenv("C_PATH").rsplit('.', 1)[0]