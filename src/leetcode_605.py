class Solution:
    def can_place_flowers(self, flowerbed: list[int], n: int) -> bool:
        flowers_remaining = n

        for p in range(len(flowerbed)):
            if flowers_remaining <= 0:
                break

            if flowerbed[p] == 1:
                continue

            if self.can_plant(flowerbed, p):
                flowerbed[p] = 1
                flowers_remaining -= 1

        return flowers_remaining == 0

    def can_plant(self, flowerbed: list[int], p: int) -> bool:
        return (p + 1 >= len(flowerbed) or flowerbed[p + 1] == 0) and (
            p - 1 < 0 or flowerbed[p - 1] == 0
        )
