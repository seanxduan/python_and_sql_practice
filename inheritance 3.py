class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


# don't touch above this line


class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows
        pass

    def shoot(self, target):
        if self.__num_arrows <= 0:
            raise Exception ("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10)
        pass



run_cases = [
    (("Hercules", 200), ("Pericles", 100, 2), 190),
    (("Aquiles", 150), ("Aneas", 80, 1), 140),
]

submit_cases = run_cases + [
    (("Zeus", 1000), ("Hades", 900, 1), None, "not enough arrows", True),
    (("Icarus", 60), ("Daedalus", 40, 2), 40, None, True),
]


def test(hero_args, archer_args, expected_result, expected_err=None, twice=False):
    hero = Hero(*hero_args)
    archer = Archer(*archer_args)

    print("---------------------------------")
    print(f"Hero:   {hero.get_name()}, Health: {hero.get_health()}")
    print(f"Archer: {archer.get_name()}, Arrows: {archer_args[2]}")
    print("")
    try:
        print(f"{archer.get_name()} tries to shoot {hero.get_name()}")
        archer.shoot(hero)
        if twice:
            print(f"{archer.get_name()} tries to shoot {hero.get_name()} again")
            archer.shoot(hero)
        result = hero.get_health()

        if expected_err:
            print(f"Expected exception: {expected_err}")
            print("Actual exception:   None")
            return False

        print(f"Expected {hero.get_name()} health: {expected_result}")
        print(f"Actual   {hero.get_name()} health: {result}")
        if result == expected_result:
            return True
        return False
    except Exception as e:
        print(f"Expected Exception: {expected_err}")
        print(f"Actual Exception:   {e}")
        if str(e) == expected_err:
            return True
        else:
            return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            print("Pass")
            passed += 1
        else:
            print("Fail")
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
