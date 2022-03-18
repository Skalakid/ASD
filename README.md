# ASD
ASD offline exercises

offline1: k-sorted linked-list

Węzły jednokierunkowej listy odsyłaczowej reprezentowane są w postaci:
class Node:
def __init__(self):
self.val = None # przechowywana liczba rzeczywista
self.next = None # odsyłacz do nastepnego elementu
Niech p będzie wskaźnikiem na niepustą listę odsyłaczową zawierającą parami różne liczby rzeczywiste a1, a2, . . . , an (lista nie ma wartownika). Mówimy, że lista jest k-chaotyczna jeśli dla każdego elementu zachodzi, że po posortowaniu listy znalazłby się na pozycji różniącej się od bieżącej
o najwyżej k. Tak więc 0-chaotyczna lista jest posortowana, przykładem 1-chaotycznej listy jest
1, 0, 3, 2, 4, 6, 5, a (n − 1)-chaotyczna lista długości n może zawierać liczby w dowolnej kolejności.
Proszę zaimplementować funkcję SortH(p,k), która sortuje k-chaotyczną listę wskazywaną przez p.
Funkcja powinna zwrócić wskazanie na posortowaną listę. Algorytm powinien być jak najszybszy
oraz używać jak najmniej pamięci (w sensie asymptotycznym, mierzonym względem długości n listy
oraz parametru k). Proszę skomentować jego złożoność czasową dla k = Θ(1), k = Θ(log n) oraz
k = Θ(n).


offline2:

Dany jest ciąg przedziałów domkniętych L = [[a1, b1], . . . ,[an, bn]]. Początki i końce przedziałów
są liczbami naturalnymi. Poziomem przedziału c ∈ L nazywamy liczbę przedziałów w L, które w
całości zawierają się w c (nie licząc samego c). Proszę zaproponować i zaimplementować algorytm,
który zwraca maksimum z poziomów przedziałów znajdujących się w L. Proszę uzasadnić poprawność algorytmu i oszacować jego złożoność obliczeniową.
Algorytm należy zaimplementować jako funkcję postaci:
def depth( L ):
...
która przyjmuje listę przedziałów L i zwraca maksimum z poziomów przedziałów w L.
Przykład. Dla listy przedziałów:
L = [ [1, 6],
[5, 6],
[2, 5],
[8, 9],
[1, 6]]
wynikiem jest liczba 3.
