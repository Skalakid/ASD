# zad1test_spec.py

ALLOWED_TIME = 1


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# k, len(list), maxint
  (1, 25, 100),
  (26, 25, 100),
  (5, 100, 1000),
  (25, 100, 1000),
  (25, 1000, 10000),
  (5, 10000, 2**24),
  (15, 10000, 2**24),
  (5, 100000, 2**24),
  (10, 100000, 2**24),
  (25, 1000000, 2**24),
]

