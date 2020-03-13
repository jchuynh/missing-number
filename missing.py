"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8
    
    """

    # RUNTIME: O(n^2)?: Two for loops
    # take in the list of numbers
    # sort them
    srt_nums = sorted(nums)

    # find the max_num and slice only the section we are intereested in
    for val in srt_nums:
        if val == max_num:
            new_lst = srt_nums[:max_num]
    # create sequential numbers up to the range
    for item in range(1, max_num + 1):
        # item to the numbers in the new_lst (with missing number)
        # if the number is not in the missing nums list
        # return that number
        if item not in new_lst:
            return item




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. NICELY DONE!\n")
