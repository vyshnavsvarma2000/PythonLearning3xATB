import os
for root, dir, files in os.walk("C:\\Users\\VYSHNAV S VARMA\\PycharmProjects\\PythonLearning3xATB\\ex5july2024"):
    print(f"Current directory - {root}")
    print(f" Sub directories - {dir}")
    print(f"Files - {files}")
    print(f"Files - {len(files)}")
