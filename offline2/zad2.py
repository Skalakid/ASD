from zad2testy import runtests


def depth(L):
    class Node():
        def __init__(self, val, index):
            self.next = None
            self.val = val
            self.index = index
            self.count = 0

    def printSet(p):
        curr = p
        while curr is not None:
            print(curr.val, "-> ", end="")
            curr = curr.next
        print()

    # tu prosze wpisac wlasna implementacje
    def left(i):
        return (2 * i) + 1

    def right(i):
        return (2 * i) + 2

    def heapify(A, n, i):
        l = left(i)
        r = right(i)
        max_ind = i

        if l < n and A[l][1] - A[l][0] > A[max_ind][1] - A[max_ind][0]:
            max_ind = l
        if r < n and A[r][1] - A[r][0] > A[max_ind][1] - A[max_ind][0]:
            max_ind = r
        if max_ind != i:
            A[max_ind], A[i] = A[i], A[max_ind]
            heapify(A, n, max_ind)

    def buid_heap(A):
        n = len(A)
        for i in range(n - 1, -1, -1):
            heapify(A, n, i)

    buid_heap(L)  # logn
    # print(L)
    max_count = 0
    p = Node(None, None)
    curr = p
    for i in range(1, len(L)):  # n
        if L[0][0] <= L[i][0] and L[0][1] >= L[i][1]:
            p.count += 1
        else:
            curr.next = Node(L[i], i)
            curr = curr.next

    curr = p.next
    while curr is not None:
        curr2 = p.next
        prev2 = p
        while curr2 is not None:
            if curr.index != curr2.index and (
                    curr.val == curr2.val or (curr.val[0] <= curr2.val[0] and curr.val[1] > curr2.val[1]) or (
                    curr.val[0] < curr2.val[0] and curr.val[1] >= curr2.val[1])):
                prev2.next = curr2.next
            else:
                prev2 = curr2
            curr2 = curr2.next
        curr = curr.next

    # printSet(p)
    curr = p.next
    while curr is not None:
        for i in range(len(L)):
            if curr.index != i and curr.val[0] <= L[i][0] and curr.val[1] >= L[i][1]:
                curr.count += 1
                if p.count < curr.count:
                    p.count = curr.count
        curr = curr.next
    return p.count
    pass


runtests( depth ) 
