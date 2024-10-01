from boot.model.member import Member
from pweb_form_rest import fields, PWebRestDTO


class MemberDetailsDTO(PWebRestDTO):
    class Meta:
        model = Member
        load_instance = True

    name = fields.String(required=True, error_messages={"required": "Please enter name"})
    mobile = fields.String(required=True, error_messages={"required": "Please enter mobile number"})
    emergencyContact = fields.String(required=True, error_messages={"required": "Please enter emergency Contact number"})
    homeDistrict = fields.String(required=True, error_messages={"required": "Please enter home District name"})
    studyIn = fields.String(required=True, error_messages={"required": "Please enter studyIn"})
    instituteName = fields.String(required=True, error_messages={"required": "Please enter institute Name"})
    technology = fields.String(required=True, error_messages={"required": "Please enter technology"})
    semester = fields.String(required=True, error_messages={"required": "Please enter semester"})
    shift = fields.String(required=True, error_messages={"required": "Please enter shift(8th)"})
    email = fields.Email(required=True, error_messages={"required": "Please enter email"})
    address = fields.String(allow_none=True)


class MemberCreateDTO(MemberDetailsDTO):
    class Meta:
        model = Member
        load_instance = True

    password = fields.String(required=True, error_messages={"required": "Please enter password"})


class MemberUpdateDTO(MemberDetailsDTO):
    class Meta:
        model = Member
        load_instance = True

    id = fields.Integer(required=True, error_messages={"required": "Please enter id"})