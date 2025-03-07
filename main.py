from typing import List
from db import get_db
from models import Contact

def get_contacts(user_id: int) -> List[Contact]:

    db = next(get_db())
    contacts = db.query(Contact).filter(Contact.user_id == user_id).all()
    return contacts

def get_second_degree_contacts(user_id: int) -> List[Contact]:
    '''
    Write a function to retrieve second-degree contacts for a user.
    A second degree contact is a "friend of friend". It's basically your contact's contacts.

    Make sure your function works and accounts for edge cases
    '''
    # code here
    second_degree_contacts = set()
    contacts = get_contacts(user_id)
    ids = []
    for contact in contacts:
        ids.append(contact.registered_user_id)
    for contact in contacts:
        contact_id = contact.registered_user_id
        secondary_contacts = get_contacts(contact_id)
        
        for secondary_contact in secondary_contacts:
            if not secondary_contact.blocked and secondary_contact.id not in ids:
                second_degree_contacts.add(secondary_contact.contact_name)
    if len(second_degree_contacts) > 0:
        print(second_degree_contacts)
    else:
        print("No second-degree contacts found.")

      
    return []

if __name__ == "__main__":
    get_second_degree_contacts(2) # modify arg for test


# A -> B
# A -> D
# B -> C +1212

# 