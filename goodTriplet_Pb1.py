class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        count = 0
        triplet_pair = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <=b and abs(arr[i] - arr[k]) <= c:
                        count +=1
                        set = (arr[i], arr[j], arr[k]) #tuple - immutable collection of items
                        triplet_pair.append(set)
        return triplet_pair, count

arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3

triplet = Solution()
triplet_pair, result = triplet.countGoodTriplets(arr, a, b, c)
print("The number of triplets: ", result)
print("Triplet set: ", triplet_pair)