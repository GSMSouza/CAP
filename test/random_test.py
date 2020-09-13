import unittest
import random as Random


class RandomTestCase(unittest.TestCase):
    def test_randint(self):
        rand_a = Random
        rand_a.seed(101)
        list_a = []
        for i in range(1000):
            list_a.append(rand_a.randint(0, 1001))
        rand_b = Random
        rand_b.seed(101)
        list_b = []
        for i in range(1000):
            list_b.append(rand_b.randint(0, 1001))

        self.assertEquals(list_a, list_b)

    def test_random(self):
        rand_a = Random
        rand_a.seed(101)
        list_a = []
        for i in range(1000):
            list_a.append(rand_a.random())
        rand_b = Random
        rand_b.seed(101)
        list_b = []
        for i in range(1000):
            list_b.append(rand_b.random())

        self.assertEquals(list_a, list_b)

    def test_choices(self):
        rand_a = Random
        rand_a.seed(101)
        list_a = []
        for i in range(1000):
            list_a.append(rand_a.choices(range(10), k=2))

        rand_b = Random
        rand_b.seed(101)
        list_b = []
        for i in range(1000):
            list_b.append(rand_b.choices(range(10), k=2))

        self.assertEquals(list_a, list_b)


if __name__ == '__main__':
    unittest.main()
