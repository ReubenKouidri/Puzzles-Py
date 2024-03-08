from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    """Serialize a tree into a string."""

    # def serialize_helper(n):
    #     if n is None:
    #         return 'None,'
    #     return (f'{n.val},{serialize_helper(n.left)}'
    #             f'{serialize_helper(n.right)}')

    def serialize_helper(n):
        if n is None:
            return None
        left_s = serialize_helper(n.left)
        right_s = serialize_helper(n.right)
        return f"{n.val},{left_s},{right_s}"

    return serialize_helper(root)


def deserialize(s):
    """Deserialize a string back into a tree."""

    # def deserialize_helper(vals):
    #     if vals[0] == 'None':
    #         vals.pop(0)
    #         return None
    #     root = Node(vals[0])
    #     vals.pop(0)  # Move to the next value
    #     root.left = deserialize_helper(vals)
    #     root.right = deserialize_helper(vals)
    #     return root
    # values = s.split(',')
    # return deserialize_helper(values)

    def deserialize_helper(dq: deque):
        if dq[0] == 'None':
            dq.popleft()
            return None
        root = Node(dq.popleft())
        root.left = deserialize_helper(dq)
        root.right = deserialize_helper(dq)
        return root

    deq = deque(s.split(','))
    return deserialize_helper(deq)


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    serialized = serialize(node)
    deserialized = deserialize(serialized)
    assert deserialized.left.left.val == 'left.left'
    print("Test passed!")
