# Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher,
# write a function to compute the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have
# at least h citations each, and the other N − h papers have no more than h citations each."
#
# Example:
#
# Input: citations = [0,1,3,5,6]
# Output: 3
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had
#              received 0, 1, 3, 5, 6 citations respectively.
#              Since the researcher has 3 papers with at least 3 citations each and the remaining
#              two with no more than 3 citations each, her h-index is 3.
# Note:
#
# If there are several possible values for h, the maximum one is taken as the h-index.
#
# Follow up:
#
# This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
# Could you solve it in logarithmic time complexity?

def h_index(citations):
    def binarySearch(citations, low, high):
        print("low: ", low, " high: ", high)
        if citations:
            if low == high:
                small = citations.index(citations[low])
                great = len(citations) - small
                if small < citations[low] <= great:
                    return citations[low]
                else:
                    if citations[low] > 0:
                        return 1
                    else:
                        return 0
            elif high - low == 1:
                small = citations.index(citations[high])
                great = len(citations) - small
                if small < citations[high] <= great:
                    return citations[high]
                else:
                    small = citations.index(citations[low])
                    great = len(citations) - small
                    if small < citations[low] <= great:
                        return citations[low]

            mid = int((low + high) / 2)
            # print("mid: ", mid)
            small = citations.index(citations[mid])
            great = len(citations) - small
            if small < citations[mid] <= great:
                # print("upper")
                return binarySearch(citations, mid, high)
            else:
                # print("lower")
                return binarySearch(citations, low, mid)
        else:
            return 0

    return binarySearch(citations, 0, len(citations) - 1)


citations = [11, 15]
citations = [0, 1, 3, 5, 6]
# citations = [0, 1]
print(h_index(citations))
