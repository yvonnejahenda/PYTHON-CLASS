from models.user import User
from models.invoice import Invoice
from peewee import SqliteDatabase, IntegrityError

DATABASE = SqliteDatabase("invoice.db")
invoices = [
    {'id': 1, 'user_email': 'john@doe.com', 'design_fee': 20, 'hosting_fee': 100, 'developer_fee': 20,'domain_fee': 100, },
    {'id': 2, 'user_email': 'fatma15@doe.com', 'design_fee': 20, 'hosting_fee': 100, 'developer_fee': 20,'domain_fee': 100, }
    
    
]


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Invoice], safe=True)
    try:
        User.create(
            first_name="yvonne",
            last_name="jahenda",
            email="john@doe.com",
            company="Acme Corp."
        )
    except IntegrityError:
        pass
    for invoice in invoices:
      try:
        Invoice.create(
                user_email=invoice.get('user_email'),
                design_fee=invoice.get('design_fee'),
                hosting_fee=invoice.get('hosting_fee'),
                developer_fee=invoice.get('developer_fee'),
                domain_fee=invoice.get('domain_fee')
        )
      except IntegrityError:
        pass
    DATABASE.close()