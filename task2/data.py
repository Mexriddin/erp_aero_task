from datetime import date

from pydantic import BaseModel, Field


class Label(BaseModel):
    company_name: str = Field(validation_alias='Company name')
    pn: str = Field(validation_alias='PN')
    sn: str = Field(validation_alias='SN')
    description: str = Field(validation_alias='DESCRIPTION')
    location: str = Field(validation_alias='LOCATION')
    condition: str = Field(validation_alias='CONDITION')
    receiver: int = Field(validation_alias='RECEIVER#')
    uom: str = Field(validation_alias='UOM')
    exp_date: date = Field(validation_alias='EXP DATE')
    po: str = Field(validation_alias='PO')
    cert_source: str = Field(validation_alias='CERT SOURCE')
    rec_date: date = Field(validation_alias='REC.DATE')
    mfg: str = Field(validation_alias='MFG')
    batch: int = Field(validation_alias='BATCH#')
    dom: date = Field(validation_alias='DOM')
    remark: str = Field(validation_alias='REMARK')
    lot: int = Field(validation_alias='LOT#')
    tagged_by: str = Field(validation_alias='TAGGED BY')
    qty: int = Field(validation_alias='Qty')
    notes: str = Field(validation_alias='NOTES')

