def find_repeating_elements(arr):
    present = set()
    repeats = set()

    for num in arr:
        if num in present:
            repeats.add(num)
        else:
            present.add(num)

    return list(repeats)

array = [4, 3, 2, 5, 6, 6, 7, 8, 2, 3, 1]
repeating_elements = find_repeating_elements(array)
print("Repeating elements:", repeating_elements)