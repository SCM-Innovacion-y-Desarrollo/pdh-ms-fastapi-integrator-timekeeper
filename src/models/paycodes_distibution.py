from typing import List, Optional
from sqlalchemy import Column,Integer, String, ForeignKey, Boolean

from sqlalchemy.orm import Mapped, relationship

from ..models.declarative_base import Base


class PaycodesDistribution(Base):
    __tablename__ = "paycodes_distribution"

    paycodes_distribution_id:                           Mapped[int] =    Column(Integer, primary_key=True, index=True)
    name:                                               Mapped[str] =    Column(String)
    description:                                        Mapped[str] =    Column(String)
    combination_rule_id:                                Mapped[int] =    Column(Integer, ForeignKey('combination_rule.combination_rule_id'))
    enable:                                             Mapped[bool] =   Column(Boolean, default=True)

    distributions_overtime_rule:                        Mapped[Optional[List["PaycodesDistributionROvertimeRule"]]] = relationship("PaycodesDistributionROvertimeRule", lazy="joined", viewonly=True, overlaps="paycodes")
    distributions_paycodes:                             Mapped[Optional[List["PaycodesDistributionRPaycode"]]] = relationship("PaycodesDistributionRPaycode", lazy="joined", overlaps="paycodes", viewonly=True)
    distribution_r_zone_schedule_desviation:            Mapped[Optional[List["PaycodesDistributionRZoneScheduleDesviation"]]] = relationship("PaycodesDistributionRZoneScheduleDesviation", lazy="joined", viewonly=True, overlaps="paycodes")
    combination_rule:                                   Mapped[Optional["CombinationRule"]] = relationship("CombinationRule", uselist=False, lazy="joined", viewonly=True, overlaps="paycodes")

class PaycodesDistributionROvertimeRule (Base):
    __tablename__ = "paycodes_distribution_r_overtime_rule"

    paycodes_distribution_r_overtime_rule_id:   Mapped[int] =    Column(Integer, primary_key=True, index=True)
    paycodes_distribution_id:                   Mapped[Optional[int]] =    Column(Integer, ForeignKey('paycodes_distribution.paycodes_distribution_id'), nullable=True, index=True)
    overtime_rule_id:                           Mapped[Optional[int]] =    Column(Integer, ForeignKey('overtime_rule.overtime_rule_id'), nullable=True, index=True)
    column:                                     Mapped[Optional[int]] =    Column(Integer)

    paycode_distribution:        Mapped[Optional["PaycodesDistribution"]] = relationship("PaycodesDistribution")
    overtime_rule:               Mapped[Optional["OvertimeRule"]] = relationship("OvertimeRule")


class PaycodesDistributionRPaycode(Base):
    __tablename__ = "paycodes_distribution_r_paycode"

    paycodes_distribution_r_paycode_id:     Mapped[int] =              Column(Integer, primary_key=True, index=True)
    paycodes_distribution_id:               Mapped[Optional[int]] =    Column(Integer, ForeignKey('paycodes_distribution.paycodes_distribution_id'), index=True)
    paycode_id:                             Mapped[Optional[int]] =    Column(Integer, ForeignKey('paycode.paycode_id'), index=True)
    row:                                    Mapped[Optional[int]] =    Column(Integer)
    column:                                 Mapped[Optional[int]] =    Column(Integer)

    paycode_distribution:                   Mapped[Optional["PaycodesDistribution"]] = relationship("PaycodesDistribution")
    paycode:                                Mapped[Optional["Paycode"]] = relationship("Paycode")

class PaycodesDistributionRZoneScheduleDesviation(Base):
    __tablename__ = "paycodes_distribution_r_zone_schedule_desviation"

    paycodes_distribution_r_zone_schedule_desviation_id:    Mapped[Optional[int]] =    Column(Integer, primary_key=True, index=True)
    paycodes_distribution_id:                               Mapped[Optional[int]] =    Column(Integer, ForeignKey('paycodes_distribution.paycodes_distribution_id'), nullable=True, index=True)
    zone_id:                                                Mapped[Optional[int]] =    Column(Integer, ForeignKey('zone.zone_id'), nullable=True, index=True)
    schedule_desviation_rule_id:                            Mapped[Optional[int]] =    Column(Integer, ForeignKey('schedule_desviation_rule.schedule_desviation_rule_id'), nullable=True, index=True)
    row:                                                    Mapped[Optional[int]] =    Column(Integer)

    zone:                        Mapped[Optional["Zone"]] = relationship("Zone")
    schedule_desviation_rule:    Mapped[Optional["ScheduleDesviationRule"]] = relationship("ScheduleDesviationRule")