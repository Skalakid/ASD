# Michał Skałka
# Mój algorytm do zadania offline 1 ma złośoność dla:
# k = 1: O(n)
# k < 12: O((n/(k+1))*(k+1)^2) = O(n(k+1))
# k >= 12   O(k+1) + O(nlog(k+1))
#
# Dla k = 1 używam pewnego radzaju modyfikacje sortowania bąbelkowego. Ponieważ każdy element może być oddalony o 1 miejsce, sprawdzam kolejne wartości elementów listy,
# odpowiednio je zamieniając.
#
# Dla k < 12 używam algorytmu selection sort. Jego działanie polega na tym, iż dziele listę na k+1 elementowe bloki. Następnie każdy taki blok sortuje przy pomocy selection sorta.
# Czyli dla mojego k+1 elem. bloku idę po każdym elemencie, i za każdym razem szukam najmniejszej wartości, oddalonej max o k elementów od elementu z którym porównuje ją. Zatem złożoność tego procecu
# wynosi O((k+1)^2).
#
# Dla pozostałych k używam sortowania przez kopcowanie. Tworzę tabliće k+1 elementową która przechowuje początkowe el. listy. Następnie buduję z niej kopiec.
# Przez to wiem że na pierwszym miejscu znajdzie się wartość najmniejsza. Wyciągam ją z tablicy a na jej miejsce wstawiam element z poza tablicy
# (czyli ten na którym zatrzymała się lista) i znowu buduje kopiec.
# Całość powtarzam aż przejdę całą listę a następnie aż wykorzystam wszystkie elementy z tablicy.
# Budowa tablicy ma złożoność ok O(k+1). Budowa kopca ma złożoność log(k+1), wykonuję to n razy.

from zad1testy import Node, runtests

def SortH(p,k):
    # tu prosze wpisac wlasna implementacje
    def left(i):
        return (2 * i) + 1

    def right(i):
        return (2 * i) + 2

    def parent(i):
        return (i - 1)//2

    def heapify(arr, n, i): # Fragment sortowania przez kopcowanie - O(log(k+1)) bo działa na tablicy k+1
        l = left(i)
        r = right(i)
        max_ind = i
        if l < n and arr[l].val < arr[max_ind].val:
            max_ind = l
        if r < n and arr[r].val < arr[max_ind].val:
            max_ind = r
        if max_ind != i:

            arr[i].val, arr[max_ind].val = arr[max_ind].val, arr[i].val
            heapify(arr, n, max_ind)

    def heapifyUp(tab, i): # funkcja taka jak heapify() tylko naprawia kopiec od dołu do góry - O(log(k+1))
        p = parent(i)
        if p >= 0 and tab[p].val > tab[i].val:
            tab[p].val, tab[i].val = tab[i].val, tab[p].val
            heapifyUp(tab, p)

    def heapPush(tab, el): # funkcja zamienia ostatnie miejsce tablicy na dany element
        tab[-1] = el
        heapifyUp(tab, len(tab)-1)

    def heapPop(tab, n): # funkcja usówa pierwszy el. w tablicy i zamienia go ostatnim. Zwraca usunięty element
        tmp = tab[0]
        tab[0] = tab[n]
        heapify(tab, n, 0)
        return tmp

    def buildHeap(arr): #funkcja odpowiedzialna za
        n = len(arr)
        for i in range(n - 1, -1, -1):
            heapify(arr, n, i)


    def selection_sort(p, k): # funkcja odpowiedzialna za sortowanie przez wybieranie
        curr1 = p
        while curr1 is not None: # funkjca dzieli listę na bloki conajwyżej k+1 elem.. Po każdym wykonaniu poleceń wewnątrz, zmiennej curr1 zostanie przypisany element o indeksie i+(k+1) - O(n/(k+1))
            curr2 = curr1
            i = 0
            while i < k and curr2 is not None: # O(k) - tu zaczna się zasadniczy selection sort, iteracja po kolejnych elementach listy
                min_el = curr2
                curr3 = curr2.next
                j = 0
                while j < k and curr3 is not None: # O(k) - funkcja przechodzi po elementach listy oddalonych o k od elementu i, szukany jest najmniejszy element z tego zbioru
                    if curr3.val < min_el.val:
                        min_el = curr3
                    curr3 = curr3.next
                    j += 1
                if min_el.val != curr2.val: # jeżeli owy element został znaleziony, zamiana
                    min_el.val, curr2.val = curr2.val, min_el.val
                curr2 = curr2.next
                i += 1
            curr1 = curr2
        return p

    if k == 1: # porownanie kolejnych elementów tablicy
        curr = p
        next = p.next
        while next is not None:
            if next.val < curr.val:
                next.val, curr.val = curr.val, next.val
            curr = curr.next
            next = curr.next
        return p
    if k < 20: # selection sort
        return selection_sort(p, k)
    # heap sort
    curr = p
    tab = []
    i = 0
    while i < k + 1 and curr is not None: # buduje tablice z conajwyżej k+1 elementami
        tab.append(curr)
        curr = curr.next
        i += 1

    buildHeap(tab) # (k+1)log(k+1)

    latest_smallest = 0
    while curr is not None: # (n-k-1)log(k+1)
        if latest_smallest != 0:
            latest_smallest.next = tab[0]
        latest_smallest = tab[0]
        heapPop(tab, len(tab)-1)
        heapPush(tab, curr)
        curr = curr.next

    for i in range(len(tab)): # (k+1)log(k+1)
        if latest_smallest != 0:
            latest_smallest.next = tab[0]
        latest_smallest = tab[0]
        heapPop(tab, len(tab)-1-i)
    latest_smallest.next = None
    return p
    pass


runtests( SortH )
