from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    codeqr = Column(String, default="")
    username = Column(String, default="")
    name = Column(String, default="")
    lastname = Column(String, default="")
    phone = Column(String, default="")
    password = Column(String)  # Assuming secure hashing is implemented
    instagram = Column(String, default="")
    puppy = Column(String, default="")
    is_active = Column(Boolean, default=True)
    
    def __repr__(self):
        return f"<User {self.id} - {self.email}>"
