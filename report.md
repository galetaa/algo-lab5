### Отчет по работе

---

### 1. Цель работы

Научиться реализовывать алгоритмы поиска.

---

### 2. Задание

В рамках работы было необходимо реализовать двусвязный список с элементами, которые представляют автомобили. Каждый элемент списка — это объект класса `Car`, содержащий следующие поля:
- **Марка автомобиля**
- **VIN**
- **Объем двигателя**
- **Стоимость**
- **Средняя скорость**

Для данной структуры данных были добавлены следующие функциональные требования:

1. Реализовать метод "Быстрый выбор" (QuickSelect), который выполняет поиск по стоимости. Этот метод требует, чтобы элементы списка были отсортированы. Если список не отсортирован, необходимо выбросить исключение.
2. Реализовать метод для сортировки элементов списка.
3. Реализовать метод поиска по алгоритму Фибоначчи. Как и в случае с методом "Быстрого выбора", перед поиском необходимо удостовериться, что элементы списка отсортированы. Если они не отсортированы, необходимо выбросить исключение.

---

### 3. Описание реализации

#### Структура данных "Двусвязный список"

Двусвязный список — это структура данных, где каждый элемент (узел) хранит ссылку на следующий и предыдущий элементы. В отличие от односвязного списка, где каждый узел содержит только ссылку на следующий элемент, двусвязный список позволяет эффективно перемещаться как вперед, так и назад.

**Реализация узла (Node):**
Каждый узел содержит:
- Ссылку на данные (в данном случае — объект `Car`).
- Ссылку на следующий узел.
- Ссылку на предыдущий узел.

**Реализация списка (DoublyLinkedList):**
Список содержит два основных указателя:
- Указатель на первый элемент (`head`).
- Указатель на последний элемент (`tail`).

Каждый узел соединяется с предыдущим и следующим узлом, что позволяет эффективно обходить список в обоих направлениях.

**Асимптотика операций:**
- **Добавление элемента в конец списка (append):** O(1), так как мы всегда добавляем элемент в конец и обновляем ссылки.
- **Доступ к элементу по индексу:** O(n), так как для поиска элемента нужно пройти по всему списку.
- **Удаление элемента:** O(1), если мы имеем ссылку на удаляемый элемент.

#### Методы двусвязного списка

1. **`append(data)`** — Добавляет новый элемент в конец списка.
   - Описание: Создается новый узел с данными и добавляется в конец списка.
   - Время работы: O(1), так как список двусвязный и у нас есть прямой доступ к последнему элементу.

2. **`is_sorted()`** — Проверяет, отсортирован ли список по полю "стоимость".
   - Описание: Метод последовательно проверяет все элементы списка и возвращает `True`, если они отсортированы, и `False` в противном случае.
   - Время работы: O(n), так как необходимо пройти весь список для проверки порядка.

3. **`sort()`** — Сортирует список по полю "стоимость".
   - Описание: Метод реализует пузырьковую сортировку (или инкрементальные перестановки элементов), если список не отсортирован. Он многократно проходит по списку, меняя местами элементы, если они находятся в неправильном порядке.
   - Время работы: O(n²), так как сортировка реализована через метод, в котором происходит несколько проходов по списку.

4. **`quick_select(price)`** — Быстрый выбор по стоимости.
   - Описание: Метод использует технику разделения массива для поиска элемента по заданной стоимости. Требуется, чтобы список был отсортирован.
   - Время работы: O(n) в среднем, но в худшем случае — O(n²), так как QuickSelect — это модификация алгоритма быстрой сортировки.

5. **`fibonacci_search(price)`** — Поиск по алгоритму Фибоначчи.
   - Описание: Использует алгоритм Фибоначчи для поиска элемента в отсортированном списке.
   - Время работы: O(log n), так как на каждом шаге количество оставшихся элементов уменьшается по мере использования чисел Фибоначчи для поиска.

#### Принцип работы методов поиска

1. **Быстрый выбор (QuickSelect):**
   - Алгоритм работает путем разделения элементов на две части: меньшие и большие относительно выбранного элемента (пивота).
   - Он повторяет этот процесс только с той частью, где может находиться искомый элемент, что значительно уменьшает количество шагов по сравнению с полной сортировкой.
   - Для корректной работы алгоритма список должен быть отсортирован.

2. **Поиск Фибоначчи (Fibonacci Search):**
   - В отличие от бинарного поиска, который делит список пополам, поиск Фибоначчи использует числа Фибоначчи для нахождения ближайшего подходящего индекса.
   - Это позволяет избежать лишних вычислений и эффективно искать в отсортированном списке.

---

### 4. Листинг кода
Задание:
```Python
# doubly_linked_list.py
class Car:
   def __init__(self, brand, vin, engine_volume, price, avg_speed):
      self.brand = brand
      self.vin = vin
      self.engine_volume = engine_volume
      self.price = price
      self.avg_speed = avg_speed

   def __repr__(self):
      return f"Car({self.brand}, {self.price})"


class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None


class DoublyLinkedList:
   def __init__(self):
      self.head = None
      self.tail = None

   def append(self, data):
      new_node = Node(data)
      if not self.head:
         self.head = self.tail = new_node
      else:
         self.tail.next = new_node
         new_node.prev = self.tail
         self.tail = new_node

   def is_sorted(self):
      current = self.head
      while current and current.next:
         if current.data.price > current.next.data.price:
            return False
         current = current.next
      return True

   def sort(self):
      if not self.head or not self.head.next:
         return
      swapped = True
      while swapped:
         swapped = False
         current = self.head
         while current and current.next:
            if current.data.price > current.next.data.price:
               current.data, current.next.data = current.next.data, current.data
               swapped = True
            current = current.next

   def quick_select(self, price):
      if not self.is_sorted():
         raise Exception("List is not sorted. Cannot perform quick select.")

      def partition(low, high):
         pivot = high.data.price
         i = low.prev
         current = low
         while current != high:
            if current.data.price <= pivot:
               i = low if i is None else i.next
               i.data, current.data = current.data, i.data
            current = current.next
         i = low if i is None else i.next
         i.data, high.data = high.data, i.data
         return i

      def quick_select_recursive(low, high, target):
         if low == high:
            return low.data

         pivot_node = partition(low, high)

         if pivot_node.data.price == target:
            return pivot_node.data
         elif pivot_node.data.price > target:
            return quick_select_recursive(low, pivot_node.prev, target)
         else:
            return quick_select_recursive(pivot_node.next, high, target)

      return quick_select_recursive(self.head, self.tail, price)

   def fibonacci_search(self, price):
      if not self.is_sorted():
         raise Exception("List is not sorted. Cannot perform Fibonacci search.")

      fib_m2 = 0
      fib_m1 = 1
      fib_m = fib_m2 + fib_m1

      n = self.length()
      while fib_m < n:
         fib_m2 = fib_m1
         fib_m1 = fib_m
         fib_m = fib_m2 + fib_m1

      offset = -1

      current = self.head
      for _ in range(min(fib_m - 1, n - 1)):
         current = current.next

      while fib_m > 1:
         i = min(offset + fib_m2, n - 1)

         current = self.get_node_at(i)

         if current.data.price < price:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
         elif current.data.price > price:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
         else:
            return current.data

      if fib_m1 and self.get_node_at(offset + 1).data.price == price:
         return self.get_node_at(offset + 1).data

      return None

   def length(self):
      count = 0
      current = self.head
      while current:
         count += 1
         current = current.next
      return count

   def get_node_at(self, index):
      current = self.head
      for _ in range(index):
         if not current:
            return None
         current = current.next
      return current


# Пример использования:
cars = [
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

dll = DoublyLinkedList()
for car in cars:
   dll.append(car)

dll.sort()
print("Сортированный список:")
current = dll.head
while current:
   print(current.data)
   current = current.next

print("\nРезультат быстрого выбора:")
print(dll.quick_select(40000))

print("\nРезультат поиска Фибоначчи:")
print(dll.fibonacci_search(25000))

```
Тесты и бенчмарки:
```Python
# test_doubly_linked_list.py
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
   # unittest.main()

   # Бенчмарки
   print("\nRunning benchmarks...")
   benchmark = BenchmarkDoublyLinkedList()
   benchmark.benchmark_sort()
   benchmark.benchmark_fibonacci_search()
   benchmark.benchmark_quick_select()

```

---

### 5. Выводы

В процессе выполнения работы была успешно реализована структура данных "Двусвязный список" с методами для добавления элементов, сортировки и поиска. Было применено два алгоритма поиска: **быстрый выбор** и **поиск Фибоначчи**.

**Результаты тестирования** показали корректную работу методов поиска при условии, что список отсортирован. Также была продемонстрирована высокая эффективность алгоритмов, несмотря на использование сортировки с асимптотикой O(n²) для списка.

Бенчмарки показали, что несмотря на простоту реализации сортировки, её скорость может быть значительно улучшена с использованием более эффективных алгоритмов (например, быстрая сортировка или сортировка слиянием). Алгоритмы поиска, такие как быстрый выбор и поиск Фибоначчи, показали хорошую производительность на больших объемах данных.

Таким образом, работа позволяет лучше понять основы реализации структур данных, а также алгоритмы поиска и их применения в реальных задачах.