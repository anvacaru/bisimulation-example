from __future__ import annotations

from .LinkedList import Node


def main() -> None:
    ones: Node = Node(1)
    ones.next = ones

    list_of_ones: Node = Node(1)
    list_of_ones.next = Node(1)
    list_of_ones.next.next = list_of_ones

    try:
        print(list_of_ones.equal(ones))
    except RecursionError:
        print('RecursionError: Reached maximum depth')

    print(list_of_ones.coequal(ones))


if __name__ == "__main__":
    main()
