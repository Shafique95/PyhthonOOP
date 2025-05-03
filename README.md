## Python-এর Object-Oriented Programming (OOP)

---

## 🐍 Python OOP (Object-Oriented Programming) — বাংলা টিউটোরিয়াল

### 🔰 অধ্যায় ১: OOP কী?

OOP বা **Object-Oriented Programming** হলো একটি প্রোগ্রামিং স্টাইল, যেখানে সবকিছুকে **অবজেক্ট** বা বস্তু হিসেবে ভাবা হয়। প্রতিটি অবজেক্টের থাকে **Attribute (Data)** এবং **Method (Functionality)**।

---

## 📦 অধ্যায় ২: ক্লাস (Class) ও অবজেক্ট (Object)

### ✅ Class:

ক্লাস হলো অবজেক্ট তৈরির জন্য একটি ব্লুপ্রিন্ট বা নকশা।

```python
class Student:
    name = "Shafiqul"
    age = 23
```

### ✅ Object:

ক্লাস থেকে বানানো বাস্তব উদাহরণ।

```python
s1 = Student()
print(s1.name)  # Output: Shafiqul
```

---

## 🧱 অধ্যায় ৩: Constructor (`__init__`) ও Instance Variables

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Shafiqul", 23)
print(s1.name, s1.age)  # Output: Shafiqul 23
```

---

## 🧰 অধ্যায় ৪: Method (Function inside class)

```python
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

s1 = Student("Shafiqul")
print(s1.greet())  # Output: Hello, Shafiqul!
```

---

## 🔄 অধ্যায় ৫: Inheritance (উত্তরাধিকার)

একটি ক্লাস থেকে অন্য ক্লাসের বৈশিষ্ট্য গ্রহণ করা।

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        return f"{self.name} is studying"

s = Student("Shafiqul")
print(s.study())  # Output: Shafiqul is studying
```

---

## 🧱 অধ্যায় ৬: Encapsulation (তথ্য গোপন)

প্রাইভেট ভ্যারিয়েবল: `_name` বা `__name` দিয়ে বুঝায়।

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500
```

---

## 🌀 অধ্যায় ৭: Polymorphism (বহুরূপিতা)

একই মেথড বিভিন্ন ক্লাসে বিভিন্নভাবে কাজ করে।

```python
class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Woof"

animals = [Cat(), Dog()]
for animal in animals:
    print(animal.sound())
```

**Output:**

```
Meow
Woof
```

---

## 🧠 অধ্যায় ৮: Abstraction (নিরবিচারে ব্যবহার)

Interface-এর মতো কাজ করে। Python-এ আমরা `abc` module ব্যবহার করি।

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())  # Output: 78.5
```

---

## 📌 অধ্যায় ৯: `@classmethod`, `@staticmethod` ও `self`, `cls`

```python
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def greet():
        return "Hello from static method"

print(MyClass.greet())         # Static Method Call
print(MyClass.get_count())     # Class Method Call
```

---

## 🧪 অধ্যায় ১০: Practice করো নিচের আইডিয়া দিয়ে

* `Student` ম্যানেজমেন্ট সিস্টেম
* `Library` ক্লাস (Book add/remove/search)
* `Bank` অ্যাকাউন্ট (deposit/withdraw/loan)
* `E-commerce` (Product, Cart, Order)

---

## 🎯 শেষ কথা

Python-এর OOP শেখার সবচেয়ে ভালো উপায় হলো **ছোট ছোট প্রজেক্ট বানানো** এবং **problem solving করা**।

