from typing import overload


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def insert_end(self, new_value):
        new_node = Node(new_value)
        end_node = self.get_end_node()
        end_node.set_next_node(new_node)

    def get_end_node(self):
        current_node = self.head_node
        while current_node.next_node is not None:
            current_node = current_node.next_node
        return current_node

    def print_linked_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + ' '
            current_node = current_node.get_next_node()
        print(string_list)

    def remove_node(self, node_to_remove):
        current_node = self.head_node
        if current_node == node_to_remove:
            self.head_node = current_node.next_node
        else:
            while current_node:
                next_node = current_node.next_node
                if next_node == node_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node


def make_linked_list(l: list) -> LinkedList:
    ll = LinkedList(None)
    for val in reversed(l):
        ll.insert_beginning(val)

    return ll


def reverse_linked_list(ll: LinkedList) -> LinkedList:
    new_ll = LinkedList()
    if ll.head_node is not None:
        while ll.head_node.get_next_node() is not None:
            new_ll.insert_beginning(ll.head_node.get_value())
            ll.head_node = ll.head_node.next_node

    return new_ll


print("Original")
demo_list = make_linked_list([4, 8, 15])
demo_list.print_linked_list()
print("Reversed")
reverse = reverse_linked_list(demo_list)
reverse.print_linked_list()
print("Original Unchanged")
demo_list.print_linked_list()
