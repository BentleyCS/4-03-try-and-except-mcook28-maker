def sum(arr: list) -> int:
    total = 0
    i = 0

    while i < len(arr):
        try:
            if type(arr[i]) == int or type(arr[i]) == float:
                total = total + arr[i]
        except:
            pass
        i = i + 1

    return total


def cleanData(rawData: list) -> list:
    cleaned = []
    i = 0

    while i < len(rawData):
        try:
            cleaned.append(float(rawData[i]))
        except:
            pass
        i = i + 1

    return cleaned


def unreliableCalculator(divisors: list) -> list:
    results = []
    i = 0

    while i < len(divisors):
        try:
            results.append(100 / divisors[i])
        except Exception as e:
            results.append(type(e).__name__)
        i = i + 1

    return results


def upperAll(arr: list) -> None:
    i = 0

    while i < len(arr):
        try:
            arr[i] = arr[i].upper()
        except:
            pass
        i = i + 1


def firstItems(arr: list) -> list:
    result = []
    i = 0

    while i < len(arr):
        try:
            result.append(arr[i][0])
        except:
            try:
                result.append(arr[i])
            except:
                pass
        i = i + 1

    return result

def test_sum():
    assert sum([1,7,"hello", 8.5]) == 16.5
    assert sum(["Cat", "dog","7"]) ==0
    assert sum([1,2,3,4]) ==10


def test_clean_data():
    assert cleanData(["1", "7.5", "cat", "14.f"]) == [1.0,7.5]
    assert cleanData(["1", "7.5", "cat", "14.6"]) == [1.0,7.5,14.6]


def test_unreliable_calculator():
    assert  unreliableCalculator([100,700,3,0,12,"Cat"])==[1.0, 0.14285714285714285, 33.333333333333336, 'ZeroDivisionError', 8.333333333333334, 'TypeError']


def test_upper_all():
    words = ["hello", "Class", 1, "good", "job"]
    assert upperAll(words)==None
    assert words==['HELLO', 'CLASS', 1, 'GOOD', 'JOB']


def test_first_items():
    assert firstItems([1,[7,5],["hello"], ["food","Hello"],8]) == [1,7,"hello","food",8]
    assert firstItems([[1,2],[3,4],[5,6],[7,8]]) == [1,3,5,7]













