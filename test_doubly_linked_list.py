import unittest
import time
from doubly_linked_list import Car, DoublyLinkedList
from sys import setrecursionlimit

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.cars = [
            Car("Toyota", "VIN1", 2.0, 20000, 180),
            Car("BMW", "VIN2", 3.0, 50000, 240),
            Car("Audi", "VIN3", 2.5, 40000, 220),
            Car("Ford", "VIN4", 1.8, 18000, 160),
            Car("Honda", "VIN5", 2.2, 22000, 200),
            Car("Kia", "VIN6", 1.6, 15000, 150),
            Car("Hyundai", "VIN7", 1.6, 16000, 155),
            Car("Mercedes", "VIN8", 3.5, 70000, 250),
            Car("Volkswagen", "VIN9", 2.0, 25000, 190),
            Car("Nissan", "VIN10", 2.4, 23000, 195),
        ]
        self.dll = DoublyLinkedList()
        for car in self.cars:
            self.dll.append(car)

    # Тесты для метода сортировки
    def test_sorting_unsorted_list(self):
        self.dll.sort()
        self.assertTrue(self.dll.is_sorted())

    def test_sorting_already_sorted_list(self):
        self.dll.sort()
        self.dll.sort()
        self.assertTrue(self.dll.is_sorted())

    def test_sorting_reverse_sorted_list(self):
        self.dll = DoublyLinkedList()
        for car in sorted(self.cars, key=lambda x: -x.price):
            self.dll.append(car)
        self.dll.sort()
        self.assertTrue(self.dll.is_sorted())

    def test_sorting_single_element(self):
        self.dll = DoublyLinkedList()
        self.dll.append(Car("Test", "VIN_TEST", 1.0, 1000, 100))
        self.dll.sort()
        self.assertTrue(self.dll.is_sorted())

    def test_sorting_empty_list(self):
        self.dll = DoublyLinkedList()
        self.dll.sort()
        self.assertIsNone(self.dll.head)

    # Тесты для быстрого выбора
    def test_quick_select_valid(self):
        self.dll.sort()
        car = self.dll.quick_select(40000)
        self.assertEqual(car.price, 40000)

    def test_quick_select_invalid(self):
        self.dll.sort()
        with self.assertRaises(Exception):
            self.dll.quick_select(99999)

    def test_quick_select_edge_case(self):
        self.dll.sort()
        car = self.dll.quick_select(15000)
        self.assertEqual(car.price, 15000)

    def test_quick_select_unsorted_list(self):
        with self.assertRaises(Exception):
            self.dll.quick_select(40000)

    # Тесты для Фибоначчи-поиска
    def test_fibonacci_search_valid(self):
        self.dll.sort()
        car = self.dll.fibonacci_search(25000)
        self.assertEqual(car.price, 25000)

    def test_fibonacci_search_edge_case(self):
        self.dll.sort()
        car = self.dll.fibonacci_search(15000)
        self.assertEqual(car.price, 15000)

    def test_fibonacci_search_unsorted_list(self):
        with self.assertRaises(Exception):
            self.dll.fibonacci_search(25000)

    def test_fibonacci_search_first_element(self):
        self.dll.sort()
        car = self.dll.fibonacci_search(15000)
        self.assertEqual(car.price, 15000)


class BenchmarkDoublyLinkedList:
    def __init__(self):
        self.cars = [Car(f"Car{i}", f"VIN{i}", 2.0, i * 1000, 180) for i in range(1, 100001)]
        self.dll = DoublyLinkedList()
        for car in self.cars:
            self.dll.append(car)

    def benchmark_sort(self):
        start_time = time.time()
        self.dll.sort()
        end_time = time.time()
        print(f"Sorting 100000 elements: {end_time - start_time:.4f} seconds")

    def benchmark_fibonacci_search(self):
        self.dll.sort()
        start_time = time.time()
        self.dll.fibonacci_search(500000)
        end_time = time.time()
        print(f"Fibonacci search (non-existent element) on 1000 elements: {end_time - start_time:.4f} seconds")

    def benchmark_quick_select(self):
        self.dll.sort()
        start_time = time.time()
        self.dll.quick_select(500000)
        end_time = time.time()
        print(f"Quick select (non-existent element) on 1000 elements: {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    setrecursionlimit(1000000)
    # Запуск тестов
    #unittest.main()

    # Бенчмарки
    print("\nRunning benchmarks...")
    benchmark = BenchmarkDoublyLinkedList()
    benchmark.benchmark_sort()
    benchmark.benchmark_fibonacci_search()
    benchmark.benchmark_quick_select()
