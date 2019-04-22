


"""
compute the next permutation:

write a program that takes in a input permutation and returns the next permutation
under dictionary ordering

example:
input: [ 1, 0, 3, 2 ]
output: [ 1, 2, 0 , 3]
"""

def next_permutation(perm):

    #find the first entry from the right that is smaller than the entry
    # immediately after it
    inversion_point = len(perm) - 2
    while (inversion_point >= 0 and
            perm[inversion_point] >= perm[inversion_point + 1]):
        inversion_point -= 1
    if inversion_point == -1:
        return []


    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm

print(next_permutation([1, 0, 3, 2]))