# Zira Python — Catatan Belajar Python

Kumpulan contoh kode Python dasar yang dipelajari satu per satu. Setiap bagian berisi kode, hasil run, dan penjelasannya.

---

## Daftar Isi

1. [Intro](#1-intro)
2. [Get Started](#2-get-started)
3. [Output](#3-output)
4. [Syntax](#4-syntax)
5. [Comments](#5-comments)
6. [Variables](#6-variables)
7. [Data Type](#7-data-type)
8. [Numbers](#8-numbers)
9. [String](#9-string)
10. [Boolean](#10-boolean)
11. [Casting](#11-casting)

---

## 1. Intro

**File:** `zira_intro.py`

Kode pertama yang paling klasik di dunia programming — mencetak teks ke layar.

```python
print("Hello, World!")
```

**Run:**

```
Hello, World!
```

**Penjelasan:**

`print()` adalah fungsi bawaan Python untuk menampilkan teks atau nilai ke layar (terminal). String ditulis di dalam tanda kutip `" "`. Ini adalah program paling sederhana dan biasanya jadi titik awal belajar bahasa apapun.

---

## 2. Get Started

**File:** `zira_get_started.py`

Sama seperti intro, ini konfirmasi bahwa Python sudah bisa dijalankan di komputer.

```python
print("Hello, World!")
```

**Run:**

```
Hello, World!
```

**Penjelasan:**

Kalau kode ini berhasil dijalankan dengan perintah `python3 zira_get_started.py`, artinya Python sudah terinstall dengan benar dan siap digunakan.

---

## 3. Output

**File:** `zira_output.py`

Menampilkan berbagai jenis nilai menggunakan `print()`.

```python
# print text
print("Hello World!")
print("I am learning Python.")
print("It is awesome!")

# print number
print(3)
print(358)
print(50000)
```

**Run:**

```
Hello World!
I am learning Python.
It is awesome!
3
358
50000
```

**Penjelasan:**

- `print()` bisa mencetak **teks** (ditulis dalam tanda kutip) maupun **angka** (tanpa tanda kutip).
- Setiap pemanggilan `print()` otomatis pindah ke baris baru.
- Teks dalam programming disebut **string**, sedangkan angka bulat disebut **integer**.

---

## 4. Syntax

**File:** `zira_syntax.py`

Aturan penulisan dasar Python: indentasi, pernyataan (statements), dan titik koma.

```python
# indentation
if 5 > 2:
  print("Five is greater than two!")

if 5 > 2:
 print("Five is greater than two!")
if 5 > 2:
        print("Five is greater than two!")

# Statements
print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!")

# semicolon
print("Hello"); print("How are you?"); print("Bye bye!")
```

**Run:**

```
Five is greater than two!
Five is greater than two!
Five is greater than two!
Hello World!
Have a good day.
Learning Python is fun!
Hello
How are you?
Bye bye!
```

**Penjelasan:**

- **Indentasi** — Python menggunakan spasi (bukan kurung kurawal `{}`) untuk menandai blok kode. Jumlah spasi boleh beda (1 spasi, 4 spasi, 8 spasi), yang penting **konsisten dalam satu blok**. Kalau tidak konsisten, Python akan error.
- **Statements** — Setiap baris perintah adalah satu statement. Python mengeksekusinya dari atas ke bawah.
- **Semicolon** — Python tidak wajib pakai titik koma `;` di akhir baris. Tapi bisa dipakai untuk menulis beberapa statement dalam satu baris (tidak dianjurkan karena susah dibaca).

---

## 5. Comments

**File:** `zira_comments.py`

Cara menulis komentar di Python — kode yang tidak ikut dieksekusi.

```python
#This is a comment
print("Hello, World!")

print("Hello, World!") #This is a comment

#print("Hello, World!")
print("Cheers, Mate!")
```

**Run:**

```
Hello, World!
Hello, World!
Cheers, Mate!
```

**Penjelasan:**

- Komentar dimulai dengan tanda `#`. Semua teks setelah `#` di baris yang sama diabaikan oleh Python.
- Komentar bisa ditulis di awal baris maupun di belakang kode.
- Baris `#print("Hello, World!")` tidak dieksekusi, makanya tidak muncul di output. Teknik ini berguna untuk **menonaktifkan sementara** suatu kode tanpa menghapusnya.

---

## 6. Variables

**File:** `zira_variables.py`

Cara membuat dan menggunakan variabel di Python.

```python
# variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# assign multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# output variables
x = "Python is awesome"
print(x)

# global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# The global Keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```

**Run:**

```
Orange
Banana
Cherry
Orange
Orange
Orange
apple
banana
cherry
Python is awesome
Python is awesome
Python is fantastic
```

**Penjelasan:**

- **Nama variabel** bisa menggunakan huruf, angka, dan underscore `_`. Tidak boleh diawali angka. Python bersifat case-sensitive (`myVar` dan `myvar` adalah variabel berbeda).
- **Assign multiple values** — satu baris bisa mengisi beberapa variabel sekaligus dengan memisahkan pakai koma: `x, y, z = "A", "B", "C"`.
- **One value to multiple variables** — satu nilai bisa diisi ke banyak variabel sekaligus: `x = y = z = "Orange"`.
- **Unpack a collection** — isi dari sebuah list bisa langsung dipisah ke variabel-variabel terpisah.
- **Global variable** — variabel yang dibuat di luar fungsi bisa diakses dari dalam fungsi.
- **Keyword `global`** — jika ingin **mengubah** nilai variabel global dari dalam fungsi, harus deklarasikan dulu dengan `global x`. Tanpa itu, Python akan membuat variabel lokal baru dan tidak mengubah yang global.

---

## 7. Data Type

**File:** `zira_datatype.py`

Mengenal tipe data yang ada di Python dan cara mengeceknya.

```python
# Text Type:       str
# Numeric Types:   int, float, complex
# Sequence Types:  list, tuple, range
# Mapping Type:    dict
# Set Types:       set, frozenset
# Boolean Type:    bool
# Binary Types:    bytes, bytearray, memoryview
# None Type:       NoneType

x = 5
print(type(x))
```

**Run:**

```
<class 'int'>
```

**Penjelasan:**

- Python punya banyak tipe data bawaan. Yang paling sering dipakai di awal: `str` (teks), `int` (bilangan bulat), `float` (bilangan desimal), `list`, `bool`.
- Fungsi `type()` digunakan untuk mengecek tipe data dari sebuah variabel atau nilai.
- Python adalah bahasa **dynamically typed** — tipe data variabel ditentukan otomatis saat kita assign nilai, tidak perlu ditulis manual seperti di Java atau C.

---

## 8. Numbers

**File:** `zira_numbers.py`

Tiga jenis tipe data angka di Python.

```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))
```

**Run:**

```
<class 'int'>
<class 'float'>
<class 'complex'>
```

**Penjelasan:**

- **`int`** (integer) — bilangan bulat, positif atau negatif, tanpa desimal. Contoh: `1`, `-5`, `1000`.
- **`float`** — bilangan dengan titik desimal. Contoh: `2.8`, `-3.14`, `0.0`.
- **`complex`** — bilangan kompleks yang punya bagian real dan imajiner. Ditulis dengan huruf `j` untuk bagian imajiner. Contoh: `1j`, `3+5j`. Jarang dipakai di pemrograman umum, tapi sering dipakai di matematika dan sains.

---

## 9. String

**File:** `zira_string.py`

Berbagai operasi yang bisa dilakukan pada teks (string).

```python
print("Hello")
print('Hello')

# slicing strings
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

# modify string
# upper case
a = "Hello, World!"
print(a.upper())

# lower case
a = "Hello, World!"
print(a.lower())

# remove whitespace
a = " Hello, World! "
print(a.strip())

# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format - f strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# place holders
price = 59
txt = f"The price is {price} dollars"
print(txt)

# escape characters
txt = "We are the so-called \"Vikings\" from the north."
```

**Run:**

```
Hello
Hello
llo
Hello
HELLO, WORLD!
hello, world!
Hello, World!
Hello World
My name is John, I am 36
The price is 59 dollars
```

**Penjelasan:**

- String bisa ditulis pakai tanda kutip ganda `"..."` atau tunggal `'...'`, hasilnya sama.
- **Slicing** — mengambil sebagian karakter dari string. `b[2:5]` artinya ambil dari index ke-2 sampai sebelum index ke-5. Index dimulai dari `0`. `b[:5]` artinya dari awal sampai sebelum index ke-5.
- **`.upper()`** — mengubah semua huruf jadi kapital.
- **`.lower()`** — mengubah semua huruf jadi kecil.
- **`.strip()`** — menghapus spasi di awal dan akhir string.
- **Concatenation** — menggabungkan string dengan operator `+`.
- **f-string** — cara modern untuk menyisipkan variabel ke dalam string. Tulis `f` sebelum tanda kutip, lalu variabel ditulis dalam `{variabel}`.
- **Escape character** `\"` — digunakan untuk menulis tanda kutip di dalam string yang sudah dibungkus tanda kutip yang sama, agar tidak dianggap sebagai penutup string.

---

## 10. Boolean

**File:** `zira_boolean.py`

Tipe data yang hanya punya dua nilai: `True` atau `False`.

```python
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
```

**Run:**

```
True
False
False
b is not greater than a
```

**Penjelasan:**

- **Boolean** adalah tipe data yang nilainya hanya bisa `True` atau `False`.
- Hasil dari perbandingan (operator `>`, `<`, `==`, dll) selalu menghasilkan Boolean.
  - `10 > 9` → `True` karena 10 memang lebih besar dari 9.
  - `10 == 9` → `False` karena 10 tidak sama dengan 9. (Ingat: `==` untuk perbandingan, `=` untuk assignment.)
  - `10 < 9` → `False` karena 10 tidak lebih kecil dari 9.
- **`if/else`** — percabangan. Kode di blok `if` dijalankan kalau kondisinya `True`, kalau `False` maka yang di blok `else` yang jalan. Karena `b (33) > a (200)` adalah `False`, maka yang dicetak adalah blok `else`.

---

## 11. Casting

**File:** `zira_casting.py`

Mengubah tipe data dari satu jenis ke jenis lain.

```python
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

print(type(x), type(y), type(z))
```

**Run:**

```
<class 'int'> <class 'int'> <class 'int'>
```

**Penjelasan:**

- **Casting** adalah proses mengubah tipe data secara eksplisit (sengaja).
- `int()` mengubah nilai menjadi integer:
  - `int(1)` → angka `1` tetap jadi `1`.
  - `int(2.8)` → float `2.8` dibulatkan ke bawah jadi `2` (bukan dibulatkan ke atas, tapi dipotong desimalnya).
  - `int("3")` → string `"3"` diubah jadi angka `3`.
- Selain `int()`, ada juga `float()` untuk mengubah ke desimal dan `str()` untuk mengubah ke teks.
- Casting berguna saat kita dapat input dari user (yang selalu berupa string) tapi butuh diolah sebagai angka.

---

> Dibuat untuk membantu memahami dasar-dasar Python secara bertahap.
