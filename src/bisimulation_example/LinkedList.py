from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, v: int) -> None:
        self.value = v
        self.next = None

    def equal(self, node: Node | None) -> bool:
        if node is None:
            return False
        return self.value == node.value and (
            (self.next is None and node.next is None) or (self.next is not None and self.next.equal(node.next))
        )

    def coequal(self, node: Node | None) -> bool:
        """Coinductive comparison of two Nodes."""
        if node is None:
            return False

        visited: set[tuple[Node | None, Node | None]] = set()
        todo: set[tuple[Node | None, Node | None]] = set()
        todo.add((self, node))

        while len(todo) != 0:
            s, t = todo.pop()
            if (s, t) in visited:
                continue
            if s is None or t is None:
                if s != t:
                    return False
                continue
            if s.value != t.value:
                return False
            todo.add((s.next, t.next))
            visited.add((s, t))
        return True
