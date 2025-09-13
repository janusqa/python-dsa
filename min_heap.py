class Solution:
    def __init__(self) -> None:
        self.data: list[int] = []
        self.size = 0

    def parent_idx(self, idx: int) -> int:
        return (idx - 1) // 2

    def left_child_idx(self, idx: int) -> int:
        return (idx * 2) + 1

    def right_child_idx(self, idx: int) -> int:
        return (idx * 2) + 2

    def heapify_up(self, idx: int) -> None:
        if idx == 0:
            return

        parent_idx = self.parent_idx(idx)
        parent_value = self.data[parent_idx]
        value = self.data[idx]

        if value < parent_value:
            self.data[parent_idx], self.data[idx] = (
                self.data[idx],
                self.data[parent_idx],
            )
            self.heapify_up(parent_idx)

    def heapify_down(self, idx: int) -> None:
        if idx >= self.size:
            return

        left_child_idx = self.left_child_idx(idx)
        right_child_idx = self.right_child_idx(idx)

        smallest_idx = idx

        if (
            right_child_idx < self.size
            and self.data[right_child_idx] < self.data[smallest_idx]
        ):
            smallest_idx = right_child_idx

        if (
            left_child_idx < self.size
            and self.data[left_child_idx] < self.data[smallest_idx]
        ):
            smallest_idx = left_child_idx

        if smallest_idx != idx:
            self.data[idx], self.data[smallest_idx] = (
                self.data[smallest_idx],
                self.data[idx],
            )
            self.heapify_down(smallest_idx)

    def insert(self, value: int) -> None:
        self.data.append(value)
        self.size += 1
        self.heapify_up(self.size - 1)

    def delete(self) -> int:
        if self.size == 0:
            raise IndexError("Heap is empty")

        value = self.data[0]

        if self.size == 1:
            self.data.pop()
            self.size -= 1
            return value

        self.data[0] = self.data.pop()
        self.size -= 1
        self.heapify_down(0)

        return value
