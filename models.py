from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    String,
    BigInteger,
    UniqueConstraint,
    Index,
    event,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_id = Column(BigInteger, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    mobile_number = Column(String, nullable=True, unique=True)
    contacts = relationship("Contact", back_populates="owner", foreign_keys="Contact.user_id")


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(
        BigInteger, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False
    )
    contact_name = Column(String(255), nullable=False)
    contact_email = Column(String(255), nullable=True)
    contact_phone = Column(String(20), nullable=True)
    is_registered = Column(Boolean, default=False)
    registered_user_id = Column(
        BigInteger, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=True
    )
    blocked = Column(Boolean, default=False)

    owner = relationship("User", foreign_keys=[user_id], back_populates="contacts")
    registered_user = relationship(
        "User", foreign_keys=[registered_user_id], backref="registered_in_contacts"
    )

    __table_args__ = (
        UniqueConstraint("user_id", "contact_phone", name="uq_user_contact_phone"),
        Index("idx_contact_phone", "contact_phone"),  # Add index for phone lookups
        Index(
            "idx_registered_user", "registered_user_id"
        ),  # Add index for registered user lookups
    )
