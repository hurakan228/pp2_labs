import psycopg2
import pandas as pd

# Подключение к БД
conn = psycopg2.connect(
    dbname="lab11",
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


def search_by_pattern():
    pattern = input("Введите шаблон для поиска: ")
    cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def insert_or_update():
    name = input("Введите имя: ")
    phone = input("Введите номер: ")
    cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
    conn.commit()
    print("✅ Операция завершена.")

def insert_many():
    num = int(input("Сколько пользователей добавить? "))
    users = []

    for _ in range(num):
        name = input("Имя: ")
        phone = input("Телефон: ")
        users.append((name, phone))

    cur.execute("""
        CALL insert_many_users(%s::user_record[]);""", (users,))
    
    conn.commit()

def paginated_query():
    try:
        limit = int(input(" Введите лимит (сколько записей показать): "))
        offset = int(input(" Введите смещение (с какой записи начать): "))

        if limit <= 0 or offset < 0:
            print("❌ Неверные параметры: лимит должен быть больше 0, а смещение не может быть отрицательным.")
            return
        
        cur.execute("SELECT * FROM get_paginated_users(%s, %s);", (limit, offset))
        rows = cur.fetchall()
        
        if rows:
            print(" Результаты:")
            for row in rows:
                print(row)
        else:
            print("❗Нет данных для отображения.")
    except Exception as e:
        print("❌ Ошибка при выполнении пагинации:", e)


def delete_with_procedure():
    column = input("Удалить по (name/phone): ").strip().lower()
    value = input("Введите значение для удаления: ").strip()

    if column not in ['name', 'phone']:
        print("❌ Неверный параметр для удаления.")
        return

    try:
        cur.execute("CALL delete_user(%s, %s);", (value, column))
        conn.commit()
        print("🗑️ Данные успешно удалены.")
    except Exception as e:
        print("❌ Ошибка при удалении:", e)


def delete_by_id():
    try:
        target_id = int(input("Введите ID для удаления: "))
        cur.execute("CALL delete_user_by_id(%s);", (target_id,))
        conn.commit()
        print(f"🗑️ Запись с ID {target_id} удалена.")
    except Exception as e:
        print("❌ Ошибка при удалении:", e)


def menu():
    create_table()
    while True:
        print("\n📞 МЕНЮ ТЕЛЕФОННОЙ КНИГИ:")
        print("1. Загрузить данные из CSV")
        print("2. Вставить из консоли")
        print("3. Обновить данные")
        print("4. Поиск")
        print("5. Удалить")
        print("6. Вставить или обновить пользователя")
        print("7.Пагинация")
        print("8.Удалить по ID")
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
            search_by_pattern()
        elif choice == '5':
            delete_with_procedure()
        elif choice == '6':
            insert_or_update()
        elif choice == '7':
            paginated_query()  
        elif choice == '8':
            delete_by_id()
        elif choice == '0':
            break
        else:
            print("❌ Неверное значение.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    menu()
