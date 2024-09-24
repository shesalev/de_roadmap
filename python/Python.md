# Python

## unittest
- [Юнит-тестирование. Использование unittest и coverage в PyCharm](https://www.youtube.com/watch?v=YD7aYJh3k-w)

## Типы и структуры данных
- [Словарь и множество (dict, set)](https://www.youtube.com/watch?v=B2pikdX1tz4)
- [Список и кортеж](https://www.youtube.com/watch?v=V3qZ6gJwBzk&t=1488s)
    -
    ```python
    lst = list(range(10))
    print(lst)
    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```
    - Add element to list
    ```python
    from timeit import timeit
    a_list = list(range(100))
    b_list = list(range(1000_000))

    x = timeit("a_list.append(100)", "from __main__ import a_list", number=1)
    y = timeit("b_list.append(100)", "from __main__ import b_list", number=1)
    print(f'{x:.6f}')
    print(f'{y:.6f}')
    ```


## Полезные функции
- dis — Disassembler for Python bytecode
```python
import dis

def myfunc(alist):
    return len(alist)

dis.dis(myfunc)
```

- Идентификатор объекта
```python
print(id(myfunc))
```

- Идентификатор объекта
```python
print(hash(myfunc))
# for objects hash(myfunc) = id(myfunc)//16
print(id(myfunc)//16)
```

- Сравнение эффективности функций в Python с timeit
```python
import timeit
execution_time = timeit.timeit('sum(range(100))', number=1000)
print(execution_time)

timeit.timeit("list()")
timeit.timeit("[]")
```

- Размер измеряемого объекта
```python
from pympler import asizeof

asizeof.asizeof(list())
asizeof.asizeof(tuple())
```

- Tables
```python
# pip install ansitable
from ansitable import ANSITable, Column

table = ANSITable("col1", "column 2 has a big header", "column 3")
table.row("aaaaaaaaa", 2.2, 3)
table.row("bbbbbbbbbbbbb", 5.5, 6)
table.row("ccccccc", 8.8, 9)
table.print()
```

```python
# pip install terminaltables
from terminaltables import AsciiTable

table_data = [
    ['Heading1', 'Heading2'],
    ['row1 column1', 'row1 column2'],
    ['row2 column1', 'row2 column2'],
    ['row3 column1', 'row3 column2']
]
table = AsciiTable(table_data)
print(table.table)
```

- Required function arguments count
```python
def myfunc(arg, *args, **kwargs):
    pass

print(myfunc.__code__.co_argcount)
```
