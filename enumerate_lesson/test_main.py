from complete_main import format_leaderboard

def test(players, expected):
    print(r"----------------------------------------")
    print(f"Inputs: {players}")
    print(f"Expected: {expected}")
    result = format_leaderboard(players)
    print(f"Actual: {result}")
    if result == expected:
        print("Pass")
        return True
    print("Fail")
    return False

def main():
    passed = 0
    tests = [
        (["Merlin", "Gandalf", "Elrond"], ["1. Merlin", "2. Gandalf", "3. Elrond"]),
        (["SoloPlayer"], ["1. SoloPlayer"]),
        ([], []),
    ]
    for t in tests:
        if test(t[0], t[1]):
            passed += 1
            
    print(r"----------------------------------------")
    print(f"{passed}/{len(tests)} tests passed")
    if passed != len(tests):
        raise Exception("Test suite failed")

main()
