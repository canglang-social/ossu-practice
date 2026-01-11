# 251129 SelfReview
# Felix Orion


def all_true(n, Lf):
    """n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called
    with n as a parameter. Otherwise returns False.
    """
    # Your code here
    for function in Lf:
        if not function(n):
            return False
    return True


# Examples:
all_true()  # prints 6
