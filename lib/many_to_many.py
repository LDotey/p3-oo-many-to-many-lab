class ContractHolder:
    def __init__(self):
        self._contracts = []

    def contracts(self):
        return self._contracts
    
    def add_contract(self, contract):
        if not isinstance(contract, Contract):
            raise Exception("contract must be an instance of Contract")
        self._contracts.append(contract)


class Author(ContractHolder):
    def __init__(self, name = ""):
        super().__init__()
        self.name = name
        # self._contracts = []
    
    # def contracts(self):
    #     return self._contracts
    
    # def add_contract(self, contract):
    #     if not isinstance(contract, Contract):
    #         raise Exception("contract must be an instance of Contract")
    #     self._contracts.append(contract)

    def books(self):
        return list({contract.book for contract in self._contracts})

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.add_contract(contract)
        return contract
    
    def total_royalties(self):
        return sum({contract.royalties for contract in self._contracts})



class Book(ContractHolder):
    def __init__(self, title = ""):
        super().__init__()
        self.title = title
    #     self._contracts = []
    # pass

    # def contracts(self):
    #     return self._contracts
    # def add_contract(self, contract):
    #     if not isinstance(contract, Contract):
    #         raise Exception("contract must be an instance of Contract")
    #     self._contracts.append(contract)

    def authors(self):
        return list({contract.author for contract in self._contracts})


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be a number")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all.append(self)

        author.add_contract(self)
        book.add_contract(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    pass


