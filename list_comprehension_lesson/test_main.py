from complete_main import double_xp

def test(base_xp, expected):
    print(r"----------------------------------------")
    print(f"Inputs: {base_xp}")
    print(f"Expected: {expected}")
    result = double_xp(base_xp)
    print(f"Actual: {result}")
    if result == expected:
        print("Pass")
        return True
    print("Fail")
    return False

def main():
    passed = 0
    tests = [
        ([10, 25, 50, 100], [20, 50, 100, 200]),
        ([0, 1, 5], [0, 2, 10]),
        ([], []),
    ]
    for t in tests:
        if test(t[0], t[1]):
            passed += 1
            
    print(r"----------------------------------------")
    print(f"{passed}/{len(tests)} tests passed")
    if passed != len(tests):
        raise Exception("Test suite failed")

if __name__ == "__main__":
    main()
