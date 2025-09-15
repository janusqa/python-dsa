from typing import Generic, TypeVar

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class LRUNode(Generic[K, V]):
    def __init__(self, k: K, v: V) -> None:
        self.key = k
        self.value = v
        self.prev: LRUNode[K, V] | None = None
        self.next: LRUNode[K, V] | None = None


class LRU(Generic[K, V]):
    def __init__(self, capacity: int = 20) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")

        self.length = 0
        self.capacity = capacity
        self.lookup: dict[K, LRUNode[K, V]] = {}
        # self.reverse_lookup: dict[Node[K, V], K] = {}
        self.head: LRUNode[K, V] | None = None
        self.tail: LRUNode[K, V] | None = None

    def get(self, key: K) -> V | None:
        node = self.lookup.get(key)

        if node is None:
            return None

        self.detach(node)
        self.prepend(node)

        return node.value

    def put(self, key: K, value: V) -> None:
        node = self.lookup.get(key)

        if node is None:
            node = LRUNode(key, value)
            self.prepend(node)
            self.lookup[key] = node
            # self.reverse_lookup[node] = key
            self.length += 1
            self.trim()
        else:
            node.value = value
            self.detach(node)
            self.prepend(node)

    def detach(self, node: LRUNode[K, V]) -> None:
        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is not None:
            node.prev.next = node.next

        if self.head == node:
            self.head = self.head.next

        if self.tail == node:
            self.tail = self.tail.prev

        node.next = None
        node.prev = None

    def prepend(self, node: LRUNode[K, V]) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def trim(self) -> None:
        if self.length <= self.capacity:
            return

        if self.tail is None:
            return

        tail = self.tail
        key = tail.key
        # key = self.reverse_lookup[tail]

        if key is None:
            return

        self.detach(self.tail)

        del self.lookup[key]
        # del self.reverse_lookup[tail]

        self.length -= 1

        self.trim()
