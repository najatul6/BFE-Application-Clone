from pweb_orm import PwebModel, pweb_orm


class Member(PwebModel):
    name = pweb_orm.Column("name", pweb_orm.String(150), nullable=False)
    mobile = pweb_orm.Column("mobile", pweb_orm.Integer(150), nullable=False)
    emergencyContact = pweb_orm.Column("emergencyContact", pweb_orm.Integer(150), nullable=False)
    homeDistrict = pweb_orm.Column("homeDistrict", pweb_orm.String(150), nullable=False)
    studyIn = pweb_orm.Column("studyIn", pweb_orm.String(150), nullable=False)
    instituteName = pweb_orm.Column("instituteName", pweb_orm.String(150), nullable=False)
    technology = pweb_orm.Column("technology", pweb_orm.String(150), nullable=False)
    semester = pweb_orm.Column("semester", pweb_orm.String(150), nullable=False)
    shift = pweb_orm.Column("shift", pweb_orm.String(150), nullable=False)
    email = pweb_orm.Column("email", pweb_orm.String(150), nullable=False)
    password = pweb_orm.Column("password", pweb_orm.String(250), nullable=False)
    address = pweb_orm.Column("address", pweb_orm.Text())