from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import relationship, Mapped, mapped_column
from base import Base

class Address(Base):
    __tablename__ = "address"
    __table_args__ = {"schema":"orm"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("orm.user.id"), unique=True)

    user = relationship("User", back_populates="address")

    @classmethod
    def filter_address_by(cls, session, value):
        stmt = select(cls).where(cls.address.ilike(f"%{value}%"))
        addresses = session.scalars(stmt).all()

        if not addresses:
            return print(f"No addresses with '{value}' found.")

        for position, address in enumerate(addresses):
            print(F"Address {position}: {address.address}")