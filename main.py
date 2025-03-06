from typing import List
from db import get_db
from models import Contact

def get_second_degree_contacts(user_id: int) -> List[Contact]:
    '''
    Write a function to get second-degree contacts for a user.
    A second degree contact is a "friend of friend".

    Make sure your function works and accounts for edge cases
    '''
    with get_db() as db:
        # code here
        return []

if __name__ == "__main__":
    get_second_degree_contacts(1) # modify arg for test
