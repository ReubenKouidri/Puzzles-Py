import os
from queue import Queue


def get_filepath_bfs(root_dir, filename):
    q = Queue()
    root = os.path.abspath(root_dir)
    q.put(root)

    while not q.empty():
        current_dir = q.get()

        try:
            for entry in os.listdir(current_dir):
                fp = os.path.join(current_dir, entry)
                if os.path.isfile(fp) and entry == filename:
                    return fp
                elif os.path.isdir(fp):
                    q.put(fp)
        except PermissionError:
            print(f"Permission denied: {current_dir}")

    return None


def get_filepath_dfs(root_dir, filename):
    q = Queue()
    root = os.path.abspath(root_dir)
    q.put(root)

    while not q.empty():
        ...


if __name__ == "__main__":
    print(get_filepath_bfs('/Users/hamidkouidri/Documents', "nonexistent.py"))
