"""Simple linked list example."""


from __future__ import annotations
from typing import Optional


class Node:
    """Single linked list Node."""
    data: int
    n: Optional[Node]

    def __init__(self, data: int, n: Optional[Node]):
        """Constructor."""
        self.data = data
        self.n = n


def count(head: Optional[Node]) -> int:
    """Counter."""
    if head is None:
        return 0
    else:
        return 1 + count(head.n)


c_node: Node = Node(3, None)
b_node: Node = Node(2, c_node)
a_node: Node = Node(1, b_node)

print(count(a_node))

print(count(b_node))

print(count(c_node))
