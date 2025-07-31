from sqlalchemy import UUID, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime
import uuid
from src.utils.db_utils import Base

# Author
class Author(Base):
    __tablename__ = 'authors'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), unique=True, nullable=False)

    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f"<Author(id='{self.id}', name='{self.name}')>"

# Books
class Book(Base):
    __tablename__ = "books"

    id: Column = Column(UUID(as_uuid=True), primary_key=True)
    title: Column = Column(String, nullable=False)
    publication_year: Column = Column(Integer, nullable=False)
    quantity: Column = Column(Integer, nullable=False)
    available_quantity = Column(Integer, nullable=False, default=1)
    author_id = Column(UUID(as_uuid=True), ForeignKey("authors.id"), nullable=False)
    author = relationship("Author", back_populates="books")
    state: Column = Column(Boolean, nullable=False)
    description: Column = Column(String, nullable=True)

    def __repr__(self):
        return f"<Book(id={self.id}, name={self.name}, publication_year={self.publication_year} description={self.description})>"

# Borrower
class Borrower(Base):
    __tablename__ = "borrowers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)
    gender = Column(String(10), nullable=False)
    dob = Column(DateTime, nullable=False)
    email = Column(String(150), nullable=True, unique=True)
    phone = Column(String(20), nullable=False, unique=True)

    loans = relationship("Management", back_populates="borrower")

    def __repr__(self):
        return (f"<Borrower(id='{self.id}', name='{self.name}', email='{self.email}', "
                f"phone='{self.phone}')>")


class Management(Base):
    __tablename__ = "management"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    book_id = Column(UUID(as_uuid=True), ForeignKey("books.id"), nullable=False)
    borrower_id = Column(UUID(as_uuid=True), ForeignKey("borrowers.id"), nullable=False)
    loan_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    due_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime, nullable=True)
    is_returned = Column(Boolean, nullable=False, default=False)
    book = relationship("Book", back_populates="management")

    borrower = relationship("Borrower", back_populates="management")

    def __repr__(self):
        return (f"<Management(id='{self.id}', book_id='{self.book_id}', borrower_id='{self.borrower_id}', "
                f"loan_date={self.loan_date.strftime('%Y-%m-%d')}, "
                f"due_date={self.due_date.strftime('%Y-%m-%d')}, "
                f"is_returned={self.is_returned})>")
