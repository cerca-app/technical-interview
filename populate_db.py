from sqlalchemy.orm import Session
from models import User, Contact, Base
from sqlalchemy import create_engine

def populate_test_data():
    # Create SQLite database engine
    engine = create_engine('sqlite:///app.db')
    
    # Create all tables (if they don't exist)
    Base.metadata.create_all(engine)
    
    # Create a session
    session = Session(engine)
    
    try:
        # Create test users with explicit IDs
        users = [
            User(user_id=1, first_name="Alice", last_name="Smith", mobile_number="+1234567890"),
            User(user_id=2, first_name="Bob", last_name="Johnson", mobile_number="+1234567891"),
            User(user_id=3, first_name="Charlie", last_name="Brown", mobile_number="+1234567892"),
            User(user_id=4, first_name="David", last_name="Wilson", mobile_number="+1234567893"),
            User(user_id=5, first_name="Eve", last_name="Davis", mobile_number="+1234567894"),
            User(user_id=6, first_name="Frank", last_name="Miller", mobile_number="+1234567895"),
        ]
        
        session.add_all(users)
        session.flush()
        
        # Create contacts with various relationships
        contacts = [
            # Alice's contacts
            Contact(
                id=1,
                user_id=1,  # Alice -> Bob
                contact_name="Bob",
                contact_phone="+1234567891",
                is_registered=True,
                registered_user_id=2
            ),
            Contact(
                id=2,
                user_id=1,  # Alice -> Charlie
                contact_name="Charlie",
                contact_phone="+1234567892",
                is_registered=True,
                registered_user_id=3
            ),
            
            # Bob's contacts
            Contact(
                id=3,
                user_id=2,  # Bob -> David
                contact_name="David",
                contact_phone="+1234567893",
                is_registered=True,
                registered_user_id=4
            ),
            Contact(
                id=4,
                user_id=2,  # Bob -> Eve
                contact_name="Eve",
                contact_phone="+1234567894",
                is_registered=True,
                registered_user_id=5
            ),
            
            # Charlie's contacts
            Contact(
                id=5,
                user_id=3,  # Charlie -> Eve
                contact_name="Eve",
                contact_phone="+1234567894",
                is_registered=True,
                registered_user_id=5
            ),
            Contact(
                id=6,
                user_id=3,  # Charlie -> Frank
                contact_name="Frank",
                contact_phone="+1234567895",
                is_registered=True,
                registered_user_id=6
            ),
            
            # Add some non-registered contacts
            Contact(
                id=7,
                user_id=1,  # Alice -> Unknown
                contact_name="Unknown Person",
                contact_phone="+1234567896",
                is_registered=False
            ),
            
            # Add some blocked contacts
            Contact(
                id=8,
                user_id=2,  # Bob -> Blocked Person
                contact_name="Blocked Person",
                contact_phone="+1234567897",
                is_registered=False,
                blocked=True
            ),
        ]
        
        session.add_all(contacts)
        session.commit()
        
        print("Test data has been successfully populated!")
        print("\nTest scenarios created:")
        print("1. Alice (id=1) has Bob and Charlie as direct contacts")
        print("2. Bob (id=2) has David and Eve as contacts")
        print("3. Charlie (id=3) has Eve and Frank as contacts")
        print("4. Alice's second-degree contacts should include:")
        print("   - David (through Bob)")
        print("   - Eve (through both Bob and Charlie)")
        print("   - Frank (through Charlie)")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    populate_test_data() 