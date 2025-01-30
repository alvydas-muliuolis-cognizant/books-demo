from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    Table,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase):
    pass


book_author = Table(
    "book_author",
    Base.metadata,
    Column("book_id", ForeignKey("book.id"), primary_key=True),
    Column("author_id", ForeignKey("author.id"), primary_key=True),
)


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    isbn13: Mapped[str] = mapped_column(String(13), nullable=False)
    pages: Mapped[int]
    overview: Mapped[str] = mapped_column(String(1000), nullable=False)
    publisher_id: Mapped[int] = mapped_column(ForeignKey("publisher.id"))
    authors: Mapped[list["Author"]] = relationship(
        secondary=book_author,
        back_populates="books",
    )
    publisher: Mapped["Publisher"] = relationship(back_populates="books")


class Author(Base):
    __tablename__ = "author"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    books: Mapped[list["Book"]] = relationship(
        secondary=book_author,
        back_populates="authors",
    )


class Publisher(Base):
    __tablename__ = "publisher"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    books: Mapped[list["Book"]] = relationship(back_populates="publisher")
