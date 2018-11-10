class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        positions = ([None] * len(flowers))[:]

        for i in range(len(flowers)):
            p = flowers[i] - 1
            positions[p] = i

            if p - k - 1 >= 0 and positions[p - k - 1] is not None:
                r = p - 1
                possible = True
                while r > p - k - 1:
                    if positions[r] is not None:
                        possible = False
                        break
                    r -= 1
                if possible:
                    return i + 1

            if p + k + 1 < len(flowers) and positions[p + k + 1] is not None:
                r = p + 1
                possible = True
                while r < p + k + 1:
                    if positions[r] is not None:
                        possible = False
                        break
                    r += 1
                if possible:
                    return i + 1
        return -1

def main():
    s = Solution()
    print(s.kEmptySlots([6,5,8,9,7,1,10,2,3,4],2))

if __name__ == '__main__':
    main()