print('Hello from repository!')


from dotenv import load_dotenv
import os

def print_author():
    load_dotenv()  # Загружаем переменные из .env
    author = os.getenv('AUTHOR')  # Читаем переменную AUTHOR
    print(f"Автор проекта: {author}")

# Проверка работы
if __name__ == "__main__":
    print_author()
