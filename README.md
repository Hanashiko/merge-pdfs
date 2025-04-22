# 📄 Merge PDFs

Це простий Python-скрипт для об'єднання декількох PDF-файлів в один. Корисний для злиття документів, сторінок або звітів в один файл.

## 🛠️ Функціональність

- Інтерактивний інтерфейс командного рядка.
- Автоматичне додавання розширення `.pdf`, якщо його не вказано.
- Об’єднання файлів у порядку введення.
- Збереження результату у файл `result.pdf`.

## 📂 Структура проєкту

```
merge-pdfs/
│
├── main.py             # Основний скрипт для запуску
├── requirements.txt    # Залежності проєкту
└── README.md           # Документація проєкту
```

## ▶️ Як запустити

### 1. Клонувати репозиторій:

```bash
git clone https://github.com/hanashiko/merge-pdfs.git
cd merge-pdfs
```

### 2. Створити віртуальне середовище (опціонально):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Встановити залежності:

```bash
pip install -r requirements.txt
```

### 4. Запустити скрипт:

```bash
python main.py
```

Після запуску програма запитає ввести назви PDF-файлів по черзі. Щоб завершити — просто натисни Enter без вводу.

## 💾 Результат

Фінальний злитий файл зберігається як `result.pdf` в кореневій директорії проєкту.

## 🧾 Приклад роботи

```
Write name of pdf file (leave empty, if you want to end adding pdf's): document1
Write name of pdf file (leave empty, if you want to end adding pdf's): notes.pdf
Write name of pdf file (leave empty, if you want to end adding pdf's):
```

> Згенерується файл: `result.pdf`, який містить вміст `document1.pdf` та `notes.pdf`.
