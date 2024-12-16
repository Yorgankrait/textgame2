class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"{self.title}: {self.content}"


class NoteApp:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)
        print("Заметка добавлена.")

    def edit_note(self, title, new_content):
        for note in self.notes:
            if note.title == title:
                note.content = new_content
                print("Заметка отредактирована.")
                return
        print("Заметка не найдена.")

    def delete_note(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                print("Заметка удалена.")
                return
        print("Заметка не найдена.")

    def list_notes(self):
        if not self.notes:
            print("Нет заметок.")
            return
        print("Список заметок:")
        for note in self.notes:
            print(note)

    def search_notes(self, keyword):
        results = [note for note in self.notes if keyword.lower() in note.title.lower() or keyword.lower() in note.content.lower()]
        if results:
            print("Результаты поиска:")
            for note in results:
                print(note)
        else:
            print("Заметки не найдены.")


def main():
    app = NoteApp()
    while True:
        print("\nВыберите действие:")
        print("1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Просмотреть все заметки")
        print("5. Поиск заметок")
        print("6. Выход")
        
        choice = input("Ваш выбор: ")
        
        if choice == '1':
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержание заметки: ")
            app.add_note(title, content)
        elif choice == '2':
            title = input("Введите заголовок заметки для редактирования: ")
            new_content = input("Введите новое содержание заметки: ")
            app.edit_note(title, new_content)
        elif choice == '3':
            title = input("Введите заголовок заметки для удаления: ")
            app.delete_note(title)
        elif choice == '4':
            app.list_notes()
        elif choice == '5':
            keyword = input("Введите ключевое слово для поиска: ")
            app.search_notes(keyword)
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()