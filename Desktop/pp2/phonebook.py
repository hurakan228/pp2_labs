import psycopg2
import pandas as pd

# Подключение к БД
conn = psycopg2.connect(
    dbname="lab10",
    user="postgres",
    password="Zz159632",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def create_table():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );
    ''')
    conn.commit()
    print("✅ Создана таблица «Телефонная книга».")

def load_from_csv(file_path):
    df = pd.read_csv(file_path)

    print("🔎 Колонки в файле:", df.columns.tolist())
    print(df.head())

    for _, row in df.iterrows():
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s);", (row['name'], row['phone']))
    conn.commit()
    print("Data loaded from CSV.")


def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите номер: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s);", (name, phone))
    conn.commit()
    print("✅ Данные вставлены.")

def update_data(old_value, new_value, column='name'):
    if column not in ['name', 'phone']:
        print("❌ Неверный раздел.")
        return
    cur.execute(f"UPDATE phonebook SET {column} = %s WHERE {column} = %s;", (new_value, old_value))
    conn.commit()
    print("Данные обновлены.")

def search_data(filter_by=None, value=None):
    if filter_by in ['name', 'phone']:
        cur.execute(f"SELECT * FROM phonebook WHERE {filter_by} ILIKE %s;", (f"%{value}%",))
    else:
        cur.execute("SELECT * FROM phonebook;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_data(by_value, column='name'):
    if column not in ['name', 'phone']:
        print("❌ Неверный раздел.")
        return
    cur.execute(f"DELETE FROM phonebook WHERE {column} = %s;", (by_value,))
    conn.commit()
    print("🗑️ Данные удалены.")

def menu():
    create_table()
    while True:
        print("\n📞 МЕНЮ ТЕЛЕФОННОЙ КНИГИ:")
        print("1. Загрузить данные из CSV")
        print("2. Вставить из консоли")
        print("3. Обновить данные")
        print("4. Поиск")
        print("5. Удалить")
        print("0. Выйти")
        choice = input("Выберите вариант: ")

        if choice == '1':
            path = input("Путь к CSV-файлу: ")
            load_from_csv(path)
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            col = input("Что обновить? (имя/телефон): ")
            old = input("Старое значение: ")
            new = input("Новое значение: ")
            update_data(old, new, col)
        elif choice == '4':
            col = input("Фильтр по (имя/телефон или пусто для всех): ")
            val = input("Значение фильтра (или оставьте пустым): ")
            search_data(col if col else None, val if val else None)
        elif choice == '5':
            col = input("Удалить по (имя/телефон): ")
            val = input("Значение для удаления: ")
            delete_data(val, col)
        elif choice == '0':
            break
        else:
            print("❌ Неверное значение.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    menu()
