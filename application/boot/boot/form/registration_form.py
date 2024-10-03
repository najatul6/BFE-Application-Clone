from boot.model.registration import Registration
from pweb_form_rest import fields, PWebForm


class RegistrationDetailsForm(PWebForm):

    class Meta:
        model = Registration
        load_instance = True

    name = fields.String(required=True, error_messages={"required": "Please enter name"})
    mobile = fields.Integer(required=True, error_messages={"required": "Please enter mobile number"})
    emergencyContact = fields.Integer(required=True, error_messages={"required": "Please enter emergency contact number"})
    homeDistrict = fields.String(required=True, error_messages={"required": "Please enter home district name"})
    studyIn = fields.String(required=True, error_messages={"required": "Please enter study in(8th)"})
    instituteName = fields.String(required=True, error_messages={"required": "Please enter institute name"})
    technology = fields.String(required=True, error_messages={"required": "Please enter technology"})
    semester = fields.String(required=True, error_messages={"required": "Please enter semester"})
    shift = fields.String(required=True, error_messages={"required": "Please enter shift"})
    email = fields.Email(required=True, error_messages={"required": "Please enter email"})
    address = fields.String(allow_none=True, type="textarea")


class RegistrationCreateForm(RegistrationDetailsForm):
    class Meta:
        model = Registration
        load_instance = True

    password = fields.String(required=True, error_messages={"required": "Please enter password"}, type="password")


class RegistrationUpdateForm(RegistrationDetailsForm):
    class Meta:
        model = Registration
        load_instance = True

    id = fields.Integer(required=True, error_messages={"required": "Please enter id"}, type="hidden", isLabel=False)