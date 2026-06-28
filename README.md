# KPPL-CI

Contoh proyek **CI sederhana** menggunakan Python, GitHub Actions, `uv`, `pytest`, dan `flake8`. Dibuat untuk mata kuliah KPPL sebagai contoh penerapan Continuous Integration pada repository Git.

## Struktur Proyek

```
.
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline CI GitHub Actions
├── app/
│   ├── __init__.py
│   └── main.py             # Kalkulator sederhana (add, subtract, multiply, divide)
├── tests/
│   └── test_main.py        # Unit test untuk fungsi di app/main.py
├── pyproject.toml          # Konfigurasi proyek & tools (uv, pytest, flake8)
├── uv.lock                 # Lockfile dependensi uv
└── .gitignore
```

## Prasyarat

- Python `>= 3.11`
- [`uv`](https://docs.astral.sh/uv/) — package manager & runner

## Cara Menjalankan Secara Lokal

### 1. Install dependencies

```bash
uv sync
```

Perintah ini akan membuat virtual environment dan memasang seluruh dependency termasuk group `dev` (`pytest` dan `flake8`).

### 2. Jalankan aplikasi

```bash
uv run python app/main.py
```

Contoh output:
```
Kalkulator Sederhana
2 + 3 = 5
10 - 4 = 6
5 * 6 = 30
20 / 4 = 5.0
```

### 3. Jalankan unit test

```bash
uv run pytest tests/ -v
```

### 4. Cek format kode dengan Flake8

```bash
uv run flake8 app tests
```

## Pipeline CI

Workflow GitHub Actions didefinisikan di [`.github/workflows/ci.yml`](.github/workflows/ci.yml) dan akan otomatis berjalan pada:

- `push` ke branch `main` atau `master`
- `pull_request` ke branch `main` atau `master`

Langkah-langkah pipeline:

1. Checkout kode sumber
2. Install `uv` (dengan cache aktif)
3. Setup Python 3.12
4. Sync dependencies dengan `uv sync`
5. Cek format kode menggunakan `flake8 app tests`
6. Jalankan unit test menggunakan `pytest tests/ -v`

Jika salah satu langkah (lint atau test) gagal, pipeline akan berhenti dengan status `failed`, sehingga kode yang error tidak dapat masuk ke branch utama.

## Fungsi yang Diuji

Modul `app/main.py` berisi kalkulator sederhana:

| Fungsi        | Deskripsi                              |
|---------------|----------------------------------------|
| `add(a, b)`   | Menambahkan dua bilangan               |
| `subtract(a, b)` | Mengurangkan `b` dari `a`           |
| `multiply(a, b)` | Mengalikan dua bilangan             |
| `divide(a, b)` | Membagi `a` dengan `b`; melempar `ValueError` jika `b == 0` |

Semua fungsi ini diuji pada [`tests/test_main.py`](tests/test_main.py), termasuk kasus pembagian dengan nol.
