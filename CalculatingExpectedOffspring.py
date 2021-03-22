def expected_offspring(ints):
    return 2 * (ints[0] + ints[1] + ints[2] + ints[3] * (3/4) + ints[4] * (2/4))

print(expected_offspring([17562, 16816, 17784, 17776, 18354, 19870]))