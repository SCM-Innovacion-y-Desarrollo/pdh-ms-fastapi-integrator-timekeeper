from src.models.declarative_base import Base
from sqlalchemy import BigInteger, Column, ForeignKey, DateTime, String, Integer, Boolean, Time, Float
from sqlalchemy.orm import relationship
class Paycodes(Base):
    __tablename__ = "paycodes"

    # Fields
    paycode_id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    abbreviated_name = Column(String, nullable=True)
    timetime_ip_aliases = Column(String, nullable=True)
    code_number = Column(String, nullable=True)
    type = Column(String, nullable=True)
    unit = Column(String, nullable=True)
    timesheet_resolved_exception = Column(Boolean, nullable=False)
    requires_approval = Column(Boolean, nullable=False)
    unjustified_exception = Column(Boolean, nullable=False)
    justified_exception = Column(Boolean, nullable=False)
    asscociate_paycode = Column(Boolean, nullable=False)
    paycode_asociate = Column(Integer, nullable=True)
    always_process_duration_separate_ = Column(Boolean, nullable=False)
    multiplier = Column(Float, nullable=True)
    add = Column(Float, nullable=True)
    enable = Column(Boolean, nullable=False)
    description = Column(String, nullable=True)
