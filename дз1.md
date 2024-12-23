# Практическое занятие №1. Введение, основы работы в командной строке

Тимофеев Никита. ИКБО-68-23

Научиться выполнять простые действия с файлами и каталогами в Linux из командной строки. Сравнить работу в командной строке Windows и Linux.

## Задача 1

Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="1_1.png">
  <source media="(prefers-color-scheme: light)" srcset="1_1.png">
  <img alt="YOUR-ALT-TEXT" src="1_1.png">
</picture>

## Задача 2

Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов, как показано в примере ниже:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="1_2.png">
  <source media="(prefers-color-scheme: light)" srcset="1_2.png">
  <img alt="YOUR-ALT-TEXT" src="1_2.png">
</picture>

## Задача 3

Написать программу banner средствами bash для вывода текстов, как в следующем примере (размер баннера должен меняться!):

<p>Код скрипта banner:</p>

```bash
#!/bin/bash
echo -n "+-"
for ((i=0; i<${#1}; i++))
do
        echo -n "-"
done
echo "-+"
echo "| $1 |"
echo -n "+-"
for ((i=0; i<${#1}; i++))
do
        echo -n "-"
done
echo "-+"
```

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="1_3.png">
  <source media="(prefers-color-scheme: light)" srcset="1_3.png">
  <img alt="YOUR-ALT-TEXT" src="1_3.png">
</picture>

## Задача 4

Написать программу для вывода всех идентификаторов (по правилам C/C++ или Java) в файле (без повторений).

<p>Код скрипта ident.sh:</p>

```bash
#!/bin/sh
grep -o "[a-zA-Z]*" hello.c | sort -u
```
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="1_4.png">
  <source media="(prefers-color-scheme: light)" srcset="1_4.png">
  <img alt="YOUR-ALT-TEXT" src="1_4.png">
</picture>

## Задача 5

<p>Код скрипта reg.sh:</p>

```bash
#!/bin/sh
chmod u+rwx $1
cp $1 /usr/local/bin
```
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="1_5.png">
  <source media="(prefers-color-scheme: light)" srcset="1_5.png">
  <img alt="YOUR-ALT-TEXT" src="1_5.png">
</picture>

## Задача 6

Написать программу для проверки наличия комментария в первой строке файлов с расширением c, js и py.

## Задача 7

Написать программу для нахождения файлов-дубликатов (имеющих 1 или более копий содержимого) по заданному пути (и подкаталогам).

## Задача 8

<p>Код скрипта archive.sh:</p>

```bash
#!/bin/sh
find -name "*.$1" | tar -cf archive.tar -T -
```
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="1_8.png">
  <source media="(prefers-color-scheme: light)" srcset="1_8.png">
  <img alt="YOUR-ALT-TEXT" src="1_8.png">
</picture>

## Задача 9

Написать программу, которая заменяет в файле последовательности из 4 пробелов на символ табуляции. Входной и выходной файлы задаются аргументами.

## Задача 10

Написать программу, которая выводит названия всех пустых текстовых файлов в указанной директории. Директория передается в программу параметром. 

## Полезные ссылки

Линукс в браузере: https://bellard.org/jslinux/

ShellCheck: https://www.shellcheck.net/

Разработка CLI-приложений

Общие сведения

https://ru.wikipedia.org/wiki/Интерфейс_командной_строки
https://nullprogram.com/blog/2020/08/01/
https://habr.com/ru/post/150950/

Стандарты

https://www.gnu.org/prep/standards/standards.html#Command_002dLine-Interfaces
https://www.gnu.org/software/libc/manual/html_node/Argument-Syntax.html
https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html

Реализация разбора опций

Питон

https://docs.python.org/3/library/argparse.html#module-argparse
https://click.palletsprojects.com/en/7.x/
