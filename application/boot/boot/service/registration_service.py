from pweb import url_for
from boot.form.registration_form import RegistrationCreateForm, RegistrationUpdateForm, RegistrationDetailsForm
from boot.model.registration import Registration
from pweb_form_rest.crud.pweb_form_data_crud import FormDataCRUD


class RegistrationService:
    form_data_crud = FormDataCRUD(model=Registration)

    def create(self):
        params = {"button": "Create", "action": url_for("registration_controller.create")}
        form = RegistrationCreateForm()
        return self.form_data_crud.create(view_name="registration/form", form=form, redirect_url=url_for("registration_controller.list"), params=params)

    def update(self, model_id: int):
        params = {"button": "Update", "action": url_for("registration_controller.update", id=model_id)}
        form = RegistrationUpdateForm()
        return self.form_data_crud.update(view_name="registration/form", model_id=model_id, update_form=form, redirect_url=url_for("registration_controller.list"), params=params)

    def details(self, model_id: int):
        form = RegistrationDetailsForm()
        return self.form_data_crud.details("registration/details", model_id=model_id, redirect_url=url_for("registration_controller.list"), display_from=form)

    def delete(self, model_id: int):
        return self.form_data_crud.delete(model_id=model_id, redirect_url=url_for("registration_controller.list"))

    def list(self):
        search_fields = ["name", "email","shift","technology"]
        return self.form_data_crud.paginated_list(view_name="registration/list", search_fields=search_fields)