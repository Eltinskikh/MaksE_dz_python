import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Подключение к БД
DATABASE_URL = "postgresql://postgres:2104@localhost:5432/DZ"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()

# Модель студента


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

# Создание таблиц


Base.metadata.create_all(bind=engine)

# Фикстура для сессии БД


@pytest.fixture(scope="function")
def db_session():
    session = SessionLocal()
    yield session
    session.close()

# Тест на добавление студента


def test_create_student(db_session):
    new_student = Student(name="Иван Иванов", email="ivan@example.com")
    db_session.add(new_student)
    db_session.commit()
    assert new_student.id is not None

# Тест на изменение студента


def test_update_student(db_session):
    # Создаем студента
    new_student = Student(name="Петр Петров", email="petr@example.com")
    db_session.add(new_student)
    db_session.commit()

    # Меняем имя
    new_student.name = "Петр Сидоров"
    db_session.commit()

    # Проверяем изменение
    updated_student = (db_session.query(Student).filter_by
                       (id=new_student.id).first())
    assert updated_student.name == "Петр Сидоров"

# Тест на удаление студента


def test_delete_student(db_session):
    # Создаем студента
    new_student = Student(name="Анна Аннова", email="anna@example.com")
    db_session.add(new_student)
    db_session.commit()

    # Удаляем студента
    db_session.delete(new_student)
    db_session.commit()

    # Проверяем, что студент удален
    deleted_student = (db_session.query(Student).filter_by
                       (id=new_student.id).first())
    assert deleted_student is None

# Очистка данных после тестов


@pytest.fixture(autouse=True)
def cleanup(db_session):
    yield
    db_session.query(Student).delete()
    db_session.commit()
