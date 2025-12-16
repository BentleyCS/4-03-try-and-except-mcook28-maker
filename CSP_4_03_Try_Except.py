#No using the built in type check function
#https://www.w3schools.com/python/python_try_except.asp
def sum(arr: list) -> int:
    total = 0
    i = 0                  # start

    while i < len(arr):    # stop condition
        total = total + arr[i]
        i = i + 1          # increment

    return total
def cleanData(rawData: list) -> list:
    cleaned = []
    i = 0                  # start

    while i < len(rawData):  # stop condition
        try:
            cleaned.append(float(rawData[i]))
        except:
            pass
        i = i + 1            # increment

    return cleaned
def unreliableCalculator(divisors: list) -> list:
    results = []
    i = 0                   # start

    while i < len(divisors):  # stop condition
        try:
            results.append(100 / divisors[i])
        except Exception as e:
            results.append(type(e).__name__)
        i = i + 1            # increment

    return results
def upperAll(arr: list) -> None:
    i = 0                   # start

    while i < len(arr):     # stop condition
        if type(arr[i]) == str:
            arr[i] = arr[i].upper()
        i = i + 1           # increment
def firstItems(arr: list) -> list:
    """
    Returns a new list containing the first item of each inner list,
    or the value itself if it is not a list. Skips empty lists safely.
    """
    result = []
    i = 0  # start

    while i < len(arr):  # stop condition
        if type(arr[i]) == list:
            try:
                result.append(arr[i][0])
            except IndexError:
                pass  # skip empty lists
        else:
            result.append(arr[i])
        i = i + 1  # increment

    return result
# ======== sum ========
print("Testing sum()")
print(sum([1, 2, 3, 4, 5]))          # Expected: 15
print(sum([10, -5, 3]))               # Expected: 8
print(sum([]))                         # Expected: 0
print()

# ======== cleanData ========
print("Testing cleanData()")
print(cleanData([1, "2", "hello", 3.5, None]))  # Expected: [1.0, 2.0, 3.5]
print(cleanData(["5.5", "NaN", "100"]))          # Expected: [5.5, 100.0]
print(cleanData([True, False, "3"]))             # Expected: [1.0, 0.0, 3.0]
print()

# ======== unreliableCalculator ========
print("Testing unreliableCalculator()")
print(unreliableCalculator([100, 50, 0, "5"]))  # Expected: [1.0, 2.0, 'ZeroDivisionError', 'TypeError']
print(unreliableCalculator([25, 20, 4]))         # Expected: [4.0, 5.0, 25.0]
print(unreliableCalculator([0]))                # Expected: ['ZeroDivisionError']
print()
# ======== upperAll ========
print("Testing upperAll()")
test_list = ["hello", "world", 123, True]
upperAll(test_list)
print(test_list)                                # Expected: ['HELLO', 'WORLD', 123, True]

test_list2 = ["pizza", "burger", "food"]
upperAll(test_list2)
print(test_list2)                              
print()

# ======== firstItems ========
print("Testing firstItems()")
print(firstItems([[1,2],[3,4],[5,6],[7,8],9]))      # Expected: [1, 3, 5, 7, 9]
print(firstItems([["a","b"], ["c"], "d", ["e","f"]])) # Expected: ['a', 'c', 'd', 'e']
print(firstItems([[], [1,2], 10]))












