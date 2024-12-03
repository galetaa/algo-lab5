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
