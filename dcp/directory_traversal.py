import os
from queue import Queue
from collections import deque
from time import time


def get_filepath_bfs(root_dir, filename):
    q = Queue()
    root = os.path.abspath(root_dir)
    q.put(root)

    while not q.empty():
        current_dir = q.get()
        try:
            for item in os.listdir(current_dir):
                path = os.path.join(current_dir, item)
                if os.path.isfile(path) and item == filename:
                    return path
                elif os.path.isdir(path):
                    q.put(path)
        except PermissionError:
            print(f"Permission denied: {current_dir}")

    return None


def get_filepath_dfs(root_dir, filename):
    stack = deque()
    root = os.path.abspath(root_dir)
    stack.append(root)

    while stack:
        current_dir = stack.pop()  # LIFO
        try:
            for entry in os.listdir(current_dir):
                full_path = os.path.join(current_dir, entry)
                if os.path.isfile(full_path) and entry == filename:
                    return full_path
                elif os.path.isdir(full_path):
                    stack.append(full_path)
                    # Add directories to the stack to explore them next
        except PermissionError:
            print(f"Permission denied: {current_dir}")

    return None


if __name__ == "__main__":
    bfs_start = time()
    print(get_filepath_bfs('/Users/hamidkouidri/Documents',
                           "directory_traversal.py"))
    bfs_total = time() - bfs_start
    print(bfs_total)

    dfs_start = time()
    print(get_filepath_dfs('/Users/hamidkouidri/Documents',
                           "directory_traversal.py"))
    dfs_total = time() - dfs_start
    print(dfs_total)
