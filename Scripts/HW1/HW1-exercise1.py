# Exercise1


def temp_tester(temp):
    def judge(normal_temp):
        if abs(normal_temp - temp) <= 1:
            return True
        else:
            return False

    return judge


# Test the above function


human_tester = temp_tester(37)
chicken_tester = temp_tester(41.1)

print(chicken_tester(42))
print(human_tester(42))
print(chicken_tester(43))
print(human_tester(35))
print(human_tester(98.6))







