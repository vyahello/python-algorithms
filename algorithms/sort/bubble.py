"""
Approach:
  - select the first element of the array
  - compare it with its next element
  - if it is larger than the next element then swap them
  - else do nothing
  - keep doing this for every index of the array
  - repeat the above process n times

-----------------------------------
For doctests run following command:
python -m xdoctest -v bubble.py
or
python3 -m xdoctest -v bubble.py
For manual testing run:
python bubble.py
"""
from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    """Implements bubble sort algorithm.

    Args:
        array: a given array

    Examples:
        >>> assert bubble_sort([]) == []
        >>> assert bubble_sort([0, 7, 5, 4]) == [0, 4, 5, 7]
        >>> assert bubble_sort([0, 7, 5, 4]) == bubble_sort([0, 7, 5, 4])
        >>> assert bubble_sort([0, 7, 5, 4]) == sorted([0, 7, 5, 4])
        >>> assert bubble_sort([0, 7, 5, 4]) != [0, 7, 5, 4]
    """
    if not len(array):
        return array
    for _ in range(len(array)):  # type: int
        for inner in range(len(array) - 1):  # type: int
            if array[inner] > array[inner + 1]:
                array[inner], array[inner + 1] = array[inner + 1], array[inner]
    return array


if __name__ == "__main__":
    print("Result is: ", bubble_sort([0, 7, 5, 4]))
