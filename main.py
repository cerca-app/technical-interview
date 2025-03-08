from typing import List
from db import get_db
from models import Contact

def get_second_degree_contacts(user_id: int) -> List[Contact]:
    '''
    Write a function to retrieve second-degree contacts for a user.
    A second degree contact is a "friend of friend". It's basically your contact's contacts.

    Make sure your function works and accounts for edge cases
    '''
    db = next(get_db())
    # Initialize a list
    # code here
    # check if that is valid user
    # get all first degree contacts using contacts table
    # iterate through them
    # on each level inside the loop, I will fetch contacts, see if they are already in the list, if not, I will add them

    allContacts = db.query(Contact).filter(Contact.user_id == user_id).all()
    secondDegreeContacts = []
    for contact in allContacts:
        firstDegreeforContact = db.query(Contact).filter(Contact.user_id == contact.id).all()
        for mutual in firstDegreeforContact:
            secondDegreeContacts.append(mutual)

    for people in secondDegreeContacts:
        print(people.contact_name)


    # put all the connections in a queue
    # make a queue and use BFS to traverse all the connections and get 2nd degree connections
    # while (!queue.isEmpty()){
    # pop the first userId
    # get all the contacts of the first userId/User
    # push these contacts in the List
    # }

    return []

if __name__ == "__main__":
    get_second_degree_contacts(1) # modify arg for test
