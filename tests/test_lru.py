import pytest

from lru import LRU


class TestLRUCache:
    def test_initialization_with_positive_capacity_creates_empty_cache(self) -> None:
        """Test that LRU cache initializes with correct capacity and empty state."""
        cache = LRU[int, int](10)
        # Verify initial state is empty and capacity is set
        if hasattr(cache, "capacity") and cache.capacity != 10:
            raise ValueError("Capacity should be set to 10")
        # Additional initialization checks would go here

    def test_initialization_with_invalid_capacity_raises_error(self) -> None:
        """Test that LRU cache raises error for invalid capacity values."""
        with pytest.raises(
            ValueError,
            match=r"capacity must be positive|Capacity must be greater than 0",
        ):
            LRU[int, int](0)

        with pytest.raises(
            ValueError,
            match=r"capacity must be positive|Capacity must be greater than 0",
        ):
            LRU[int, int](-5)

    def test_get_returns_none_for_nonexistent_key(self) -> None:
        """Test that get method returns None for keys that don't exist in cache."""
        cache = LRU[int, int](2)
        result = cache.get(999)
        if result is not None:
            raise ValueError("Get should return None for non-existent key")

    def test_put_and_get_operations_work_correctly(self) -> None:
        """Test basic put and get functionality with existing keys."""
        cache = LRU[str, int](3)

        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)

        if cache.get("a") != 1:
            raise ValueError("Should return 1 for key 'a'")
        if cache.get("b") != 2:
            raise ValueError("Should return 2 for key 'b'")
        if cache.get("c") != 3:
            raise ValueError("Should return 3 for key 'c'")

    def test_put_updates_existing_key_value(self) -> None:
        """Test that put method updates value for existing keys."""
        cache = LRU[str, int](2)

        cache.put("key", 100)
        cache.put("key", 200)  # Update existing key

        result = cache.get("key")
        if result != 200:
            raise ValueError("Put should update existing key value to 200")

    def test_lru_eviction_removes_least_recently_used_item(self) -> None:
        """Test that LRU cache evicts least recently used items when capacity is exceeded."""
        cache = LRU[int, str](2)

        cache.put(1, "one")
        cache.put(2, "two")
        cache.put(3, "three")  # This should evict key 1

        if cache.get(1) is not None:
            raise ValueError("Key 1 should be evicted and return None")
        if cache.get(2) != "two":
            raise ValueError("Key 2 should remain with value 'two'")
        if cache.get(3) != "three":
            raise ValueError("Key 3 should be present with value 'three'")

    def test_get_operation_updates_recency_of_accessed_items(self) -> None:
        """Test that accessing items via get method updates their recency position."""
        cache = LRU[int, str](2)

        cache.put(1, "one")
        cache.put(2, "two")
        cache.get(1)  # Access key 1 to make it most recently used
        cache.put(3, "three")  # This should evict key 2, not key 1

        if cache.get(1) != "one":
            raise ValueError("Key 1 should remain after being accessed")
        if cache.get(2) is not None:
            raise ValueError("Key 2 should be evicted and return None")
        if cache.get(3) != "three":
            raise ValueError("Key 3 should be present")

    def test_put_operation_updates_recency_of_existing_items(self) -> None:
        """Test that updating existing items via put method updates their recency."""
        cache = LRU[int, str](2)

        cache.put(1, "one")
        cache.put(2, "two")
        cache.put(1, "updated")  # Update key 1, making it most recently used
        cache.put(3, "three")  # This should evict key 2, not key 1

        if cache.get(1) != "updated":
            raise ValueError("Key 1 should remain with updated value")
        if cache.get(2) is not None:
            raise ValueError("Key 2 should be evicted and return None")
        if cache.get(3) != "three":
            raise ValueError("Key 3 should be present")

    def test_complex_usage_sequence_maintains_lru_ordering(self) -> None:
        """Test complex sequence of operations maintains correct LRU ordering."""
        cache = LRU[int, int](3)

        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        cache.get(2)  # Access order: 2, 3, 1
        cache.put(4, 4)  # Should evict 1 (least recently used)

        if cache.get(1) is not None:
            raise ValueError("Key 1 should be evicted first and return None")
        if cache.get(2) != 2:
            raise ValueError("Key 2 should remain")
        if cache.get(3) != 3:
            raise ValueError("Key 3 should remain")
        if cache.get(4) != 4:
            raise ValueError("Key 4 should be present")

        cache.get(3)  # Access order: 3, 4, 2
        cache.put(5, 5)  # Should evict 2 (least recently used)

        if cache.get(2) is not None:
            raise ValueError("Key 2 should be evicted second and return None")
        if cache.get(3) != 3:
            raise ValueError("Key 3 should remain")
        if cache.get(4) != 4:
            raise ValueError("Key 4 should remain")
        if cache.get(5) != 5:
            raise ValueError("Key 5 should be present")

    def test_cache_works_with_different_key_value_types(self) -> None:
        """Test that cache works correctly with various key and value types."""
        # Test with string keys and integer values
        cache1 = LRU[str, int](2)
        cache1.put("test", 42)
        if cache1.get("test") != 42:
            raise ValueError("String key with integer value should work")

        # Test with integer keys and string values
        cache2 = LRU[int, str](2)
        cache2.put(123, "hello")
        if cache2.get(123) != "hello":
            raise ValueError("Integer key with string value should work")

        # Test with tuple keys
        cache3 = LRU[tuple[int, int], str](2)
        cache3.put((1, 2), "tuple_value")
        if cache3.get((1, 2)) != "tuple_value":
            raise ValueError("Tuple key should work")

    def test_cache_handles_multiple_evictions_correctly(self) -> None:
        """Test that cache can handle multiple consecutive evictions."""
        cache = LRU[int, int](2)

        # Fill cache
        cache.put(1, 1)
        cache.put(2, 2)

        # Force multiple evictions
        cache.put(3, 3)  # Evicts 1
        cache.put(4, 4)  # Evicts 2
        cache.put(5, 5)  # Evicts 3

        if cache.get(1) is not None:
            raise ValueError("Key 1 should be evicted and return None")
        if cache.get(2) is not None:
            raise ValueError("Key 2 should be evicted and return None")
        if cache.get(3) is not None:
            raise ValueError("Key 3 should be evicted and return None")
        if cache.get(4) != 4:
            raise ValueError("Key 4 should be present")
        if cache.get(5) != 5:
            raise ValueError("Key 5 should be present")

    def test_edge_case_single_item_cache(self) -> None:
        """Test cache behavior with capacity of 1."""
        cache = LRU[int, str](1)

        cache.put(1, "first")
        if cache.get(1) != "first":
            raise ValueError("Single item should be accessible")

        cache.put(2, "second")  # Should evict first item
        if cache.get(1) is not None:
            raise ValueError("First item should be evicted and return None")
        if cache.get(2) != "second":
            raise ValueError("Second item should be present")

        cache.put(2, "updated")  # Update existing item
        if cache.get(2) != "updated":
            raise ValueError("Item should be updated")

    def test_mixed_operations_with_none_results(self) -> None:
        """Test various operations that should return None."""
        cache = LRU[int, int](2)

        # Test get on empty cache
        if cache.get(1) is not None:
            raise ValueError("Get on empty cache should return None")

        # Test get after eviction
        cache.put(1, 100)
        cache.put(2, 200)
        cache.put(3, 300)  # Evicts 1
        if cache.get(1) is not None:
            raise ValueError("Get on evicted key should return None")

        # Test get on never-inserted key
        if cache.get(999) is not None:
            raise ValueError("Get on never-inserted key should return None")

    def test_cache_consistency_after_multiple_operations(self) -> None:
        """Test that cache remains consistent after various operations."""
        cache = LRU[str, int](2)

        # Add and remove items
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)  # Evicts "a"

        # Verify state
        if cache.get("a") is not None:
            raise ValueError("Key 'a' should be evicted and return None")
        if cache.get("b") != 2:
            raise ValueError("Key 'b' should remain")
        if cache.get("c") != 3:
            raise ValueError("Key 'c' should be present")

        # Update and test again
        cache.put("b", 22)  # Update existing
        if cache.get("b") != 22:
            raise ValueError("Key 'b' should be updated to 22")

        # Add another item, should evict "c"
        cache.put("d", 4)
        if cache.get("c") is not None:
            raise ValueError("Key 'c' should be evicted and return None")
        if cache.get("d") != 4:
            raise ValueError("Key 'd' should be present")
