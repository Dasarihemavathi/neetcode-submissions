class Solution:
    def topKFrequent(self, nums, k):

        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        ans = []

        for i in range(k):

            maxi = 0
            value = 0

            for key in d:

                if d[key] > maxi:
                    maxi = d[key]
                    value = key

            ans.append(value)

            d[value] = 0

        return ans