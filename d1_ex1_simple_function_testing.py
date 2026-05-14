# Scrieți o funcție 
def maximum(lst):
    pass # un placeholder cu valoare sintactică. un statement no-op.

# ce primind un singur argument o listă de numere întregi,
# returnează numărul maxim.

def maximum(lst):
    # early data validation
    if not lst:
        # this is an exception
        raise ValueError("Empty list not allowed")

    max = lst[0]

    for n in lst:
        if n > max:
            max = n

    return max


# ... și apoi scriem teste
# we test for...


# !! number of elements in list

# zero elements in list:

#assert maximum([]) == None  # this is a test that conveys behavioral specifications!
#                            # it is also wrong. see below for correct expectations.

try:
    value = maximum([])
    has_exception = False
except ValueError as exc:
    has_exception = True


# other important variations in the number of elements:
# one and two

assert maximum([55]) == 55
assert maximum([77, 55]) == 77


# !! regular cases, with varied values

# very regular case
assert maximum([1, 2, 3]) == 3

# still regular case, dar ne jucăm cu ordinea datelor
# max --> first, in the middle, last
assert maximum([1, 2, 7, 9, 12]) == 12
assert maximum([12, 1, 2, 7, 9]) == 12
assert maximum([1, 2, 12, 7, 9]) == 12

# varied dataset
# let's use smaller / larger values
# let's use negative values!

# only negatives
assert maximum([-55, -22, -80]) == -22
# a mix
assert maximum([-55, 0, 1, 1800, -22, -80]) == 1800

# maybe mix floats, ints, decimals
# (if the function is supposed to deal with them)




def is_valid_age(age):
    "accepts ages bewtween 18 and 60"
    return age >= 18 and age < 60

# we want to test for boundary values:
# 17, 18, 19
# 42
# 59, 60, 61
