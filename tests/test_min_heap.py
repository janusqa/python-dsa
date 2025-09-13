from src.min_heap import Solution  # Replace with your actual module name


class TestMinHeap:
    def test_empty_heap_initialization(self) -> None:
        """Test creating an empty heap."""
        heap = Solution()
        if heap.data != []:
            raise AssertionError("Empty heap should have empty data list")
        if heap.size != 0:
            raise AssertionError("Empty heap should have size 0")

    def test_insert_into_empty_heap(self) -> None:
        """Test inserting into an empty heap."""
        heap = Solution()
        heap.insert(5)
        if heap.data != [5]:
            raise AssertionError("Heap should contain the inserted value")
        if heap.size != 1:
            raise AssertionError("Heap size should be 1 after insertion")

    def test_insert_multiple_values(self) -> None:
        """Test inserting multiple values maintains heap property."""
        heap = Solution()
        values = [5, 3, 8, 1, 2]

        for value in values:
            heap.insert(value)

        # After all insertions, the root should be the smallest value
        if heap.data[0] != 1:
            raise AssertionError("Root should be the smallest value after insertions")
        if heap.size != 5:
            raise AssertionError("Heap size should be 5 after all insertions")

    def test_delete_from_empty_heap(self) -> None:
        """Test deleting from empty heap raises error."""
        heap = Solution()
        try:
            heap.delete()
            raise AssertionError("Expected IndexError when deleting from empty heap")
        except IndexError as e:
            if "Heap is empty" not in str(e):
                raise AssertionError(
                    "Error message should indicate heap is empty",
                ) from e

    def test_delete_single_element(self) -> None:
        """Test deleting the only element from heap."""
        heap = Solution()
        heap.insert(42)
        result = heap.delete()

        if result != 42:
            raise AssertionError("Delete should return the only element")
        if heap.data != []:
            raise AssertionError("Heap should be empty after deletion")
        if heap.size != 0:
            raise AssertionError("Heap size should be 0 after deletion")

    def test_delete_maintains_heap_property(self) -> None:
        """Test multiple deletions maintain heap property."""
        heap = Solution()
        values = [5, 3, 8, 1, 2, 7]

        for value in values:
            heap.insert(value)

        # Delete all elements and verify they come out in sorted order
        extracted = []
        while heap.size > 0:
            extracted.append(heap.delete())

        expected = sorted(values)
        if extracted != expected:
            raise AssertionError("Extracted values should be in sorted order")
        if heap.data != []:
            raise AssertionError("Heap should be empty after all deletions")
        if heap.size != 0:
            raise AssertionError("Heap size should be 0 after all deletions")

    def test_heap_with_duplicate_values(self) -> None:
        """Test heap handles duplicate values correctly."""
        heap = Solution()
        values = [3, 1, 3, 1, 2, 2]

        for value in values:
            heap.insert(value)

        extracted = []
        while heap.size > 0:
            extracted.append(heap.delete())

        expected = [1, 1, 2, 2, 3, 3]
        if extracted != expected:
            raise AssertionError("Extracted values should handle duplicates correctly")
        if heap.size != 0:
            raise AssertionError("Heap should be empty after all deletions")

    def test_large_heap_operations(self) -> None:
        """Test heap with larger dataset."""
        heap = Solution()
        values = list(range(100, 0, -1))  # Reverse sorted: 100, 99, 98, ..., 1

        for value in values:
            heap.insert(value)

        # Should extract in ascending order
        extracted = []
        while heap.size > 0:
            extracted.append(heap.delete())

        expected = list(range(1, 101))
        if extracted != expected:
            raise AssertionError("Large dataset should extract in sorted order")
        if heap.size != 0:
            raise AssertionError("Heap should be empty after large operations")

    def test_heap_size_calculation(self) -> None:
        """Test that size is correctly maintained."""
        heap = Solution()
        if heap.size != 0:
            raise AssertionError("Initial size should be 0")

        heap.insert(5)
        if heap.size != 1:
            raise AssertionError("Size should be 1 after first insertion")

        heap.insert(3)
        if heap.size != 2:
            raise AssertionError("Size should be 2 after second insertion")

        heap.delete()
        if heap.size != 1:
            raise AssertionError("Size should be 1 after deletion")

        heap.delete()
        if heap.size != 0:
            raise AssertionError("Size should be 0 after all deletions")

    def test_edge_case_single_element(self) -> None:
        """Test edge case with single element multiple times."""
        heap = Solution()
        heap.insert(42)
        result = heap.delete()
        if result != 42:
            raise AssertionError("Should return the single element")
        if heap.size != 0:
            raise AssertionError("Should be empty after deletion")

        # Insert again after deletion
        heap.insert(100)
        result = heap.delete()
        if result != 100:
            raise AssertionError("Should return the newly inserted element")
        if heap.size != 0:
            raise AssertionError("Should be empty after second deletion")

    def test_mixed_operations_sequence(self) -> None:
        """Test complex sequence of insert and delete operations."""
        heap = Solution()

        # Phase 1: Insert some values
        heap.insert(10)
        heap.insert(5)
        heap.insert(15)
        result = heap.delete()
        if result != 5:
            raise AssertionError("First delete should return smallest value")

        # Phase 2: Insert more values
        heap.insert(3)
        heap.insert(8)
        result = heap.delete()
        if result != 3:
            raise AssertionError("Second delete should return new smallest value")

        # Phase 3: Final operations
        heap.insert(1)
        heap.insert(20)

        # Verify deletion sequence
        result = heap.delete()
        if result != 1:
            raise AssertionError("Third delete should return the smallest value")
        result = heap.delete()
        if result != 8:
            raise AssertionError("Fourth delete should return correct value")
        result = heap.delete()
        if result != 10:
            raise AssertionError("Fifth delete should return correct value")
        result = heap.delete()
        if result != 15:
            raise AssertionError("Sixth delete should return correct value")
        result = heap.delete()
        if result != 20:
            raise AssertionError("Seventh delete should return correct value")

        if heap.size != 0:
            raise AssertionError("Heap should be empty after all operations")
