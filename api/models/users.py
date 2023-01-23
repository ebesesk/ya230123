from email.policy import default
from sqlalchemy import Column, Integer, String, Boolean, Date, null, DateTime
from sqlalchemy.orm import relationship

from ..db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(10, 'utf8mb4_unicode_ci'), unique=True, nullable=False)
    hashed_password = Column(String(256, 'utf8mb4_unicode_ci'), nullable=False)
    # email = Column(String(30, 'utf8mb4_unicode_ci'), unique=True, index=True)
    # is_active = Column(Boolean, nullable=True)
    # is_superuser = Column(Boolean, nullable=True)

    # blogs = relationship('Blog', back_populates='creator')