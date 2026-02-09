from app.db import crud
from unicodedata import category
from app.db.db import SessionLocal


def main():
    db = SessionLocal()

    try:
        new_category = crud.create_category(db, title = "Роман")
        print(f"Новая категория: {new_category.title}, ID категории {new_category.id}")

        new_category1 = crud.create_category(db,title =  "Детектив")
        print(f"Новая категория: {new_category1.title}, ID категории {new_category1.id}")

        new_book = crud.create_book(
            db,
            title = "Мастер и Маргарита",
            description = "Культовое произведение Булгакова",
            price = 599.9,
            category_id = new_category.id
        )
        print(f"Новая книга: {new_book.title}, ID книги: {new_book.id}, ID категории: {new_book.category_id}")

        new_book1 = crud.create_book(
            db,
            title = "Оно",
            description = "Главное произведение Кинга",
            price = 1299.9,
            category_id = new_category1.id
        )
        print(f"Новая книга: {new_book1.title}, ID книги: {new_book1.id}, ID категории: {new_book1.category_id}")

        
        new_book2 = crud.create_book(
            db,
            title = "Почему не Эванс?",
            description = "История, которая манит и дразнит читателя, ни на минуту не давая перестать ворочать мозгами",
            price = 759.99,
            category_id = new_category1.id
        )
        print(f"Новая книга: {new_book2.title}, ID книги: {new_book2.id}, ID категории: {new_book2.category_id}")

        
        new_book3 = crud.create_book(
            db,
            title = "Униженные и оскорбленные",
            description = "Роман русского писателя Фёдора Михайловича Достоевского",
            price = 399.9,
            category_id = new_category.id
        )
        print(f"Новая книга: {new_book3.title}, ID книги: {new_book3.id}, ID категории: {new_book3.category_id}")

        categories = crud.get_all_categories(db)
        print(f"Все категории:")
        for c in categories:
            print(f"(ID: {c.id}) {c.title}")

        books = crud.get_all_books(db)
        print(f"Все книги:")
        for b in books:
            print(f"(ID: {b.id}) {b.title} - {b.price} руб")


        updated_book = crud.update_book(
            db,
            book_id = new_book1.id,
            title  = "Оно. Возвращение в Дерри",
            price = 1999.9

        )
        print(f"Обновленная книга: (ID: {updated_book.id}) {updated_book.title} - {updated_book.price}")


        deleted_book = crud.delete_book(db, book_id = new_book.id)
        if deleted_book:
            print(f"Удаленная книга: (ID: {new_book.id}) {new_book.title}")

        books1 = crud.get_all_books(db)
        print(f"Все книги:")
        for b in books1:
            print(f"(ID: {b.id}) {b.title} - {b.price} руб")



    finally:
        db.close()


if __name__ == "__main__":  
    main()