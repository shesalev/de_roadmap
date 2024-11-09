# DE Roadmap

## md file
[Базовый синтаксис записи и форматирования](https://docs.github.com/ru/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

## Spark

- Знает назначение драйвера и экзекьюторов, объясняет shuffle по аналогии с MapReduce, знает, как уменьшить и увеличить число партиций. 
- Знает, что Spark оптимизирует запросы и как можно вывести итоговый план на экран. 
- Тюнит производительность за счет увеличения числа экзекьюторов и/или добавления памяти/ядер. 
- Сталкивался с кэшированием. 
- Знает, зачем нужны UDF

### Middle

- Может описать взаимодействие драйвера и экзекьюторов, понимает роль YARN при запуске в кластере. 
    - [Running Spark on YARN](https://spark.apache.org/docs/latest/running-on-yarn.html)
- Поверхностно знает отличия 2 и 3 версии. 
- Знает про deploy-modes и динамическую аллокацию ресурсов. 
- Понимает суть узких и широких трансформаций, понимает проблему shuffle и может привести примеры операций, вызывающих его, знает про skewness. 
- Верхнеуровнево понимает роль оптимизатора Catalyst.
    - [Как работает SparkSQL изнутри и причем здесь Catalyst](https://spark-school.ru/blog/how-catalyst-works/)
- Понимает, как справляться с OutOfMemory. 
- Знает базовые подходы к оптимизации, знает про broadcast. 
- Может объяснить как происходит кэширование. 
- Может перечислить алгоритмы join’ов в Spark. 
- Знает, почему UDF медленные. 
- Понимает разницу между RDD, Dataframe, Dataset
- Spark UI 
[Руководство для начинающих по Spark UI: Как отслеживать и анализировать задания Spark](https://habr.com/ru/companies/slurm/articles/771036/)

### Senior

- Может подробно описать рантайм архитектуру спарк-приложения при запуске в YARN кластере.
    - [Как Apache Spark планирует и запускает задания в кластере](https://bigdataschool.ru/blog/news/spark/spark-job-scheduling.html)
    - [Running Spark on YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) 
- Может перечислить отличия 2 и 3 версии. 
    - [Spark 3.0: новые возможности и примеры их использования – часть 1](https://habr.com/ru/companies/newprolab/articles/530568/)
        - Adaptive Query Execution
            - Coalescing Shuffle Partitions
            - Switching Join Strategies
            - Optimizing Skew Joins
            - Dynamic Partition Pruning
        - Spark Connect
        - ANSI SQL Compatibility
        - GPU
        - Hints
- Может объяснить разницу в deploy-modes и какой когда используется. 
- Хорошо понимает настройку динамической аллокации.
    - [Как Apache Spark планирует и запускает задания в кластере](https://bigdataschool.ru/blog/news/spark/spark-job-scheduling.html)
    - [Вспомнить все: 6 сегментов памяти Apache Spark и параметры их конфигурирования](https://bigdataschool.ru/blog/jvm-spark-memory-types-and-configurations.html) 
- Хорошо понимает, как происходит shuffle. 
    - [How to optimize shuffle spill in Apache Spark application](https://stackoverflow.com/questions/30797724/how-to-optimize-shuffle-spill-in-apache-spark-application)
    - [Оптимизируем Shuffle в Spark](https://habr.com/ru/companies/X5Tech/articles/837348/)
- Понимает разницу между repartition и coalesce. 
- Умеет бороться со skewness. 
- Может пошагово описать работу оптимизатора. 
- Знает продвинутые методики оптимизации. 
- Может объяснить разницу между кэшированием и чекпоинтами. 
    - [pyspark.sql.DataFrame.checkpoint](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.checkpoint.html)
- Может подробно рассказать про все типы join и алгоритм выбора между ними в Spark. 
- Может подробно описать особенности работы UDF. 
- Знает, как справляться с большинством ошибок, как дебажить и искать проблемные места

[Пять подходов к созданию ad-hoc-датафреймов в PySpark](https://habr.com/ru/companies/vk/articles/760796/)

https://www.youtube.com/watch?v=mA96gUESVZc&list=PLWAuYt0wgRcLCtWzUxNg4BjnYlCZNEVth&index=5

[Spark Performance Tuning](https://github.com/afaqueahmad7117/spark-experiments)

[Руководство для начинающих по Spark UI: Как отслеживать и анализировать задания Spark](https://habr.com/ru/companies/slurm/articles/771036/)

## Hadoop
- [Apache Hadoop YARN](https://hadoop.apache.org/docs/r3.1.1/hadoop-yarn/hadoop-yarn-site/YARN.html)

## Python

Базовый синстаксис
Переменные и типы данных
Ветвления и циклы
Работа с исключениями и ошибками
Преобразование типов
Встроенные стурктуры данных (List, Tuple, Set, Dict)
Журналирование

### Middle

Алгоритмы и стурктуры данных (Array, Linked List, Queue, Heap, Stask, Hash Table, B-Tree, Recursion, Sorting)
List Comprehensions
Pandas, NumPy, SciPy
RegEx
Decorators, Iterators, Generators
OOP (Абстракция, Наследование, Инкапсуляция, Полиморфизм, dunder методы)
Модули
Пакетные менеджеры

### Senior

Парадигмы программирования
Тесты (UnitTest, PyTest)
FastAPI, Flask, Tornado
ML Libraries (sklearn, xgboost, catboost, etc)


## Data
- Индексы
    - [Индексирование баз данных в PostgreSQL: погружение в тему](https://habr.com/ru/companies/ibs/articles/838492/)

- PostgeSql
    - [Топ полезных SQL-запросов для PostgreSQL](https://habr.com/ru/articles/696274/)
    - [Коллекция готовых SQL запросов для PostgreSQL](https://github.com/rin-nas/postgresql-patterns-library)

- Greenplum
    - [Читаем планы SQL-запросов Greenplum на практическом примере и разбираемся с операциями](https://bigdataschool.ru/blog/greenplum-explain-plans-operations-to-execute-sql-query.html)
- SQL train
    - [Practical skills of SQL language](https://sql-ex.ru/)

## Arch
[HP Vertica, проектирование хранилища данных, больших данных](https://habr.com/ru/articles/227111/)
[Архитектура хранилищ данных: традиционная и облачная](https://habr.com/ru/articles/441538/)
[Снежинка, Data Vault, Anchor Modeling. Какая методология проектирования DWH подойдет для вашего бизнеса?](https://habr.com/ru/articles/786822/)
[DataVault / Anchor Modeling / Николай Голов](https://www.youtube.com/watch?v=-ZgzpQXsxi0)
[Топ-5 архитектурных паттернов для распределённых систем](https://tproger.ru/translations/top-5-arhitekturnyh-patternov-dlja-raspredeljonnyh-sistem)
[System Integration Patterns](https://testengineer.ru/system-integration-patterns/)

## OOP
- [Solid](https://habr.com/ru/companies/itentika/articles/694730/)
- [Справочник-шпаргалка по методологиям и паттернам на Python](python)
- [ООП на простых примерах. Объектно-ориентированное программирование](https://www.youtube.com/watch?v=-6DWwR_R4Xk)

## SQL
- [Логотип sql academy(Тренажер)](https://sql-academy.org/ru/trainer/tasks/1)

## Common
- [Главное из книги Fundamentals of Data engineering — фундаментального труда о дата-инжиниринге](https://habr.com/ru/companies/vk/articles/766530/)

## Python
- [Декораторы в Python](https://habr.com/ru/articles/814217/)
- [Fluent Python (Code)](https://github.com/AllenDowney/fluent-python-notebooks/blob/master/03-dict-set/dialcodes.ipynb)