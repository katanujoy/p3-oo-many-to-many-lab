# lib/many_to_many.py

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        # Return all contracts where this author is involved
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # Return all unique books this author has contracts with
        return list({contract.book for contract in self.contracts()})

    def sign_contract(self, book, date, royalties):
        # Create and return a new contract with the given book, date, royalties
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Sum all royalties from this author's contracts
        return sum(contract.royalties for contract in self.contracts())

    def __repr__(self):
        return f"<Author: {self.name}>"


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        # Return all contracts where this book is involved
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # Return all unique authors who have contracts with this book
        return list({contract.author for contract in self.contracts()})

    def __repr__(self):
        return f"<Book: {self.title}>"


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # Validation for correct types
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        # Return all contracts that have the specified date
        return [contract for contract in cls.all if contract.date == date]

    def __repr__(self):
        return f"<Contract: {self.author.name} - {self.book.title} - {self.date} - ${self.royalties}>"
