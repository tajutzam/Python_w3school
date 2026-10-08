from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

BLACK = RGBColor(0x00, 0x00, 0x00)

# ── Styling helpers ──────────────────────────────────────────────

def add_heading(doc, text, level=1):
    p = doc.add_heading(text, level=level)
    for run in p.runs:
        run.font.color.rgb = BLACK
    return p

def add_label(doc, text):
    """Label bold hitam (Kode Program:, Hasil Run:, Pembahasan:)."""
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.color.rgb = BLACK
    run.font.bold = True
    run.font.size = Pt(11)
    p.paragraph_format.space_after = Pt(2)
    return p

def add_body(doc, text):
    p = doc.add_paragraph(text)
    for run in p.runs:
        run.font.color.rgb = BLACK
        run.font.size = Pt(11)
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(6)
    return p

def add_placeholder_box(doc, height_cm=4):
    """Kotak kosong bertitik untuk ditempel screenshot."""
    from docx.shared import Cm
    tbl = doc.add_table(rows=1, cols=1)
    tbl.style = "Table Grid"
    cell = tbl.cell(0, 0)
    cell.width = Inches(6)
    # isi kosong dengan tinggi tertentu memakai baris newline
    lines = int(height_cm * 2.5)
    cell.paragraphs[0].add_run("\n" * lines)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    doc.add_paragraph()  # spasi setelah tabel

def spacer(doc, pt=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(pt)

# ── Cover ────────────────────────────────────────────────────────

doc.add_paragraph()
t = doc.add_paragraph()
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run("Zira Python")
r.font.name = "Calibri"
r.font.size = Pt(28)
r.font.bold = True
r.font.color.rgb = BLACK

t2 = doc.add_paragraph()
t2.alignment = WD_ALIGN_PARAGRAPH.CENTER
r2 = t2.add_run("Catatan Belajar Python — Pemrograman Dasar")
r2.font.size = Pt(13)
r2.font.color.rgb = BLACK

doc.add_paragraph()
doc.add_paragraph()

# ── Data setiap topik ────────────────────────────────────────────

topics = [
    {
        "num": 1,
        "title": "Pendahuluan (Intro)",
        "intro": (
            "Dalam pemrograman, program pertama yang lazim dibuat adalah program yang menampilkan "
            "teks \"Hello, World!\" ke layar. Program ini menjadi standar universal untuk memverifikasi "
            "bahwa lingkungan pemrograman telah terkonfigurasi dengan benar dan bahasa pemrograman "
            "dapat dieksekusi pada sistem yang bersangkutan."
        ),
        "pembahasan": (
            "Fungsi print() merupakan fungsi bawaan (built-in function) pada bahasa pemrograman Python "
            "yang berfungsi untuk menampilkan output berupa teks atau nilai ke layar terminal. "
            "Argumen yang diberikan berupa literal string, yaitu rangkaian karakter yang diapit oleh "
            "tanda kutip ganda (\"). Ketika program dieksekusi, interpreter Python akan memproses "
            "instruksi tersebut dan menampilkan hasilnya pada antarmuka baris perintah (command-line interface)."
        ),
    },
    {
        "num": 2,
        "title": "Memulai Python (Get Started)",
        "intro": (
            "Sebelum memulai penulisan program, lingkungan Python harus dipastikan telah terpasang "
            "dengan benar pada sistem operasi yang digunakan. Proses verifikasi dilakukan dengan "
            "menjalankan program sederhana sebagai konfirmasi bahwa interpreter Python berfungsi "
            "secara normal."
        ),
        "pembahasan": (
            "Program dijalankan melalui terminal dengan perintah python3 diikuti nama file. "
            "Pada sistem operasi macOS dan Linux digunakan perintah python3, sedangkan pada Windows "
            "umumnya cukup menggunakan perintah python. Keberhasilan eksekusi program ini menandakan "
            "bahwa Python telah terpasang dengan benar dan siap digunakan untuk pengembangan lebih lanjut."
        ),
    },
    {
        "num": 3,
        "title": "Output Program",
        "intro": (
            "Output merupakan mekanisme dasar dalam pemrograman yang memungkinkan program "
            "untuk menyampaikan informasi kepada pengguna. Pada Python, output dihasilkan "
            "menggunakan fungsi print() yang dapat menampilkan berbagai jenis data, baik berupa "
            "teks (string) maupun bilangan (numerik)."
        ),
        "pembahasan": (
            "Fungsi print() pada Python dapat menerima argumen berupa string maupun nilai numerik. "
            "String ditulis dengan menggunakan tanda kutip, sedangkan nilai numerik ditulis langsung "
            "tanpa tanda kutip. Setiap pemanggilan fungsi print() akan secara otomatis menambahkan "
            "karakter newline di akhir output, sehingga setiap pernyataan print() ditampilkan pada "
            "baris yang terpisah. Dalam pemrograman, teks dikenal sebagai tipe data string, "
            "sedangkan bilangan bulat dikenal sebagai tipe data integer."
        ),
    },
    {
        "num": 4,
        "title": "Sintaks Python (Python Syntax)",
        "intro": (
            "Sintaks merupakan seperangkat aturan yang mengatur cara penulisan kode dalam suatu "
            "bahasa pemrograman. Python memiliki sintaks yang bersih dan mudah dibaca, dengan "
            "beberapa aturan fundamental yang membedakannya dari bahasa pemrograman lain, "
            "terutama dalam hal penggunaan indentasi sebagai penanda blok kode."
        ),
        "pembahasan": (
            "Terdapat tiga aspek utama sintaks Python yang perlu dipahami:\n\n"
            "1. Indentasi — Python menggunakan indentasi (spasi di awal baris) sebagai penanda "
            "blok kode, menggantikan penggunaan kurung kurawal ({}) yang umum ditemukan pada bahasa "
            "lain seperti C atau Java. Jumlah spasi yang digunakan bersifat fleksibel, namun harus "
            "konsisten dalam satu blok yang sama. Ketidakkonsistenan indentasi akan menyebabkan "
            "IndentationError.\n\n"
            "2. Pernyataan (Statements) — Setiap baris kode merupakan satu pernyataan yang "
            "dieksekusi secara berurutan dari atas ke bawah.\n\n"
            "3. Titik Koma (Semicolon) — Python tidak mewajibkan penggunaan titik koma di akhir "
            "pernyataan. Meskipun memungkinkan penulisan beberapa pernyataan dalam satu baris "
            "menggunakan titik koma sebagai pemisah, praktik ini tidak direkomendasikan karena "
            "mengurangi keterbacaan kode."
        ),
    },
    {
        "num": 5,
        "title": "Komentar (Comments)",
        "intro": (
            "Komentar adalah bagian dari kode sumber yang tidak dieksekusi oleh interpreter. "
            "Komentar digunakan untuk memberikan penjelasan, dokumentasi, atau anotasi pada kode "
            "agar lebih mudah dipahami oleh pengembang lain maupun oleh penulis kode itu sendiri "
            "di kemudian hari."
        ),
        "pembahasan": (
            "Pada Python, komentar diawali dengan karakter tanda pagar (#). Seluruh teks yang "
            "berada setelah tanda # pada baris yang sama akan diabaikan oleh interpreter dan tidak "
            "dieksekusi. Komentar dapat ditulis pada baris tersendiri di awal kode, maupun "
            "ditambahkan di bagian akhir baris setelah pernyataan yang ada (inline comment). "
            "Selain sebagai dokumentasi, komentar juga sering dimanfaatkan untuk menonaktifkan "
            "sementara (disable) suatu baris kode selama proses pengembangan dan pengujian, "
            "tanpa perlu menghapus kode tersebut secara permanen."
        ),
    },
    {
        "num": 6,
        "title": "Variabel (Variables)",
        "intro": (
            "Variabel adalah nama simbolis yang digunakan untuk menyimpan nilai di dalam memori "
            "komputer. Dalam Python, variabel bersifat dinamis, artinya tipe data sebuah variabel "
            "dapat berubah sesuai dengan nilai yang ditetapkan padanya, tanpa perlu deklarasi tipe "
            "secara eksplisit seperti pada bahasa pemrograman bertipe statis."
        ),
        "pembahasan": (
            "Python mendukung beberapa cara penugasan nilai pada variabel:\n\n"
            "1. Penamaan Variabel — Nama variabel dapat menggunakan huruf, angka, dan karakter "
            "garis bawah (_), namun tidak boleh diawali dengan angka. Python bersifat case-sensitive, "
            "sehingga myVar dan myvar dianggap sebagai dua variabel yang berbeda.\n\n"
            "2. Penugasan Berganda (Multiple Assignment) — Python memungkinkan penugasan nilai "
            "kepada beberapa variabel sekaligus dalam satu baris: x, y, z = \"A\", \"B\", \"C\".\n\n"
            "3. Penugasan Satu Nilai ke Banyak Variabel — Satu nilai dapat ditugaskan ke beberapa "
            "variabel secara bersamaan: x = y = z = \"Orange\".\n\n"
            "4. Unpacking Koleksi — Elemen-elemen dari sebuah koleksi (seperti list) dapat "
            "langsung didistribusikan ke variabel-variabel yang terpisah.\n\n"
            "5. Variabel Global dan Kata Kunci global — Variabel yang dideklarasikan di luar "
            "fungsi dapat diakses dari dalam fungsi. Namun, untuk mengubah nilai variabel global "
            "dari dalam fungsi, diperlukan deklarasi eksplisit menggunakan kata kunci global."
        ),
    },
    {
        "num": 7,
        "title": "Tipe Data (Data Types)",
        "intro": (
            "Tipe data merupakan klasifikasi yang menentukan jenis nilai yang dapat disimpan "
            "oleh sebuah variabel serta operasi apa yang dapat dilakukan terhadap nilai tersebut. "
            "Python menyediakan berbagai tipe data bawaan yang mencakup hampir seluruh kebutuhan "
            "pemrograman umum."
        ),
        "pembahasan": (
            "Python memiliki kategori tipe data bawaan sebagai berikut: tipe teks (str), "
            "tipe numerik (int, float, complex), tipe sekuens (list, tuple, range), tipe pemetaan "
            "(dict), tipe himpunan (set, frozenset), tipe boolean (bool), tipe biner (bytes, "
            "bytearray, memoryview), dan tipe None (NoneType).\n\n"
            "Fungsi type() digunakan untuk memeriksa tipe data dari suatu variabel atau nilai "
            "pada saat program berjalan. Python merupakan bahasa pemrograman dengan pengetikan "
            "dinamis (dynamically typed), yang berarti tipe data sebuah variabel ditentukan secara "
            "otomatis oleh interpreter berdasarkan nilai yang ditetapkan, tanpa memerlukan "
            "deklarasi tipe secara eksplisit oleh programmer."
        ),
    },
    {
        "num": 8,
        "title": "Bilangan (Numbers)",
        "intro": (
            "Python menyediakan tiga tipe data numerik bawaan yang digunakan untuk merepresentasikan "
            "berbagai jenis bilangan dalam komputasi. Pemahaman terhadap ketiga tipe ini penting "
            "untuk memastikan presisi dan ketepatan dalam perhitungan matematis."
        ),
        "pembahasan": (
            "Tiga tipe data numerik pada Python adalah:\n\n"
            "1. Integer (int) — merepresentasikan bilangan bulat, baik positif maupun negatif, "
            "tanpa komponen desimal. Python mendukung integer dengan presisi tak terbatas, "
            "sehingga tidak ada batasan ukuran bilangan selain kapasitas memori sistem.\n\n"
            "2. Float (float) — merepresentasikan bilangan riil dengan komponen desimal. "
            "Tipe ini diimplementasikan menggunakan representasi floating-point presisi ganda "
            "(double-precision) sesuai standar IEEE 754.\n\n"
            "3. Complex (complex) — merepresentasikan bilangan kompleks yang terdiri dari "
            "bagian riil dan bagian imajiner. Bagian imajiner ditandai dengan sufiks j. "
            "Tipe ini umumnya digunakan dalam komputasi ilmiah dan matematis."
        ),
    },
    {
        "num": 9,
        "title": "String",
        "intro": (
            "String merupakan tipe data yang digunakan untuk merepresentasikan data teks. "
            "Dalam Python, string adalah urutan karakter yang bersifat immutable (tidak dapat "
            "diubah setelah dibuat). Python menyediakan beragam operasi dan metode bawaan untuk "
            "memanipulasi string secara efisien."
        ),
        "pembahasan": (
            "Beberapa operasi dasar string pada Python meliputi:\n\n"
            "1. Penulisan String — String dapat ditulis menggunakan tanda kutip ganda (\"..\") "
            "maupun kutip tunggal ('..'), dengan hasil yang identik.\n\n"
            "2. Slicing — Pengambilan sebagian karakter dari string menggunakan notasi [awal:akhir]. "
            "Indeks dimulai dari 0. Sebagai contoh, b[2:5] mengambil karakter dari indeks ke-2 "
            "hingga sebelum indeks ke-5.\n\n"
            "3. Metode Modifikasi — Python menyediakan metode bawaan seperti .upper() untuk "
            "mengonversi ke huruf kapital, .lower() untuk huruf kecil, dan .strip() untuk "
            "menghapus spasi di awal dan akhir string.\n\n"
            "4. Konkatenasi (Concatenation) — Penggabungan dua atau lebih string menggunakan "
            "operator +.\n\n"
            "5. f-String — Metode pemformatan string modern yang memungkinkan penyisipan nilai "
            "variabel secara langsung ke dalam string dengan sintaks f\"...{variabel}...\".\n\n"
            "6. Escape Character — Karakter khusus yang diawali dengan backslash (\\) untuk "
            "merepresentasikan karakter yang tidak dapat ditulis langsung, seperti \\\" untuk "
            "tanda kutip ganda di dalam string."
        ),
    },
    {
        "num": 10,
        "title": "Boolean",
        "intro": (
            "Tipe data boolean merupakan tipe data fundamental dalam logika pemrograman yang "
            "hanya memiliki dua kemungkinan nilai: True (benar) atau False (salah). Tipe data "
            "ini menjadi dasar dari seluruh struktur percabangan dan pengambilan keputusan "
            "dalam program."
        ),
        "pembahasan": (
            "Nilai boolean pada Python dihasilkan dari evaluasi ekspresi logika dan perbandingan. "
            "Operator perbandingan yang tersedia meliputi > (lebih besar), < (lebih kecil), "
            "== (sama dengan), != (tidak sama dengan), >= (lebih besar atau sama), dan "
            "<= (lebih kecil atau sama). Setiap ekspresi perbandingan akan menghasilkan nilai "
            "True atau False.\n\n"
            "Perlu diperhatikan perbedaan antara operator = (assignment, untuk menugaskan nilai "
            "ke variabel) dan operator == (comparison, untuk membandingkan dua nilai).\n\n"
            "Struktur if/else memanfaatkan nilai boolean untuk menentukan alur eksekusi program. "
            "Blok kode di bawah if akan dieksekusi apabila kondisi bernilai True, sedangkan "
            "blok else akan dieksekusi apabila kondisi bernilai False."
        ),
    },
    {
        "num": 11,
        "title": "Casting (Konversi Tipe Data)",
        "intro": (
            "Casting atau konversi tipe data adalah proses mengubah suatu nilai dari tipe data "
            "tertentu ke tipe data lain secara eksplisit. Operasi ini diperlukan ketika program "
            "perlu memproses data dalam tipe yang berbeda dari tipe aslinya, misalnya mengonversi "
            "input pengguna yang berupa string menjadi bilangan untuk keperluan perhitungan."
        ),
        "pembahasan": (
            "Python menyediakan fungsi bawaan untuk melakukan konversi tipe data, antara lain:\n\n"
            "1. int() — mengonversi nilai ke tipe integer. Apabila diberikan nilai float, "
            "bagian desimal akan dipotong (truncated), bukan dibulatkan. Apabila diberikan "
            "string yang merepresentasikan bilangan bulat, string tersebut akan dikonversi "
            "menjadi integer yang sesuai.\n\n"
            "2. float() — mengonversi nilai ke tipe float, menghasilkan bilangan dengan "
            "komponen desimal.\n\n"
            "3. str() — mengonversi nilai ke tipe string, menghasilkan representasi teks "
            "dari nilai yang diberikan.\n\n"
            "Casting sangat berguna dalam skenario di mana data diterima dari pengguna melalui "
            "fungsi input(), yang selalu mengembalikan nilai bertipe string, namun perlu "
            "diproses sebagai bilangan dalam perhitungan matematis."
        ),
    },
]

# ── Generate tiap topik ──────────────────────────────────────────

for t in topics:
    add_heading(doc, f"{t['num']}. {t['title']}", level=1)
    spacer(doc, 4)

    # intro / deskripsi
    add_body(doc, t["intro"])

    # kode program
    add_label(doc, "Kode Program:")
    add_placeholder_box(doc, height_cm=5)

    # hasil run
    add_label(doc, "Hasil Run:")
    add_placeholder_box(doc, height_cm=3.5)

    # pembahasan
    add_label(doc, "Pembahasan:")
    add_body(doc, t["pembahasan"])

    # pemisah antar topik
    doc.add_page_break()

# ── Simpan ───────────────────────────────────────────────────────

out = "/Users/zam/kerja/tajoki/pyth/zira-python/Zira_Python.docx"
doc.save(out)
print(f"Saved: {out}")
