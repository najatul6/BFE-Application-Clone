from boot.service.registration_service import RegistrationService
from pweb import Blueprint

registration_url_prefix = "/registration"
registration_controller = Blueprint(
    "registration_controller",
    __name__,
    url_prefix=registration_url_prefix
)
registration_service = RegistrationService()


@registration_controller.route("/create", methods=['POST', 'GET'])
def create():
    return registration_service.create()


@registration_controller.route("/details/<int:id>", methods=['GET'])
def details(id: int):
    return registration_service.details(id)


@registration_controller.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id: int = None):
    return registration_service.update(id)


@registration_controller.route("/delete/<int:id>", methods=['GET'])
def delete(id: int):
    return registration_service.delete(id)


@registration_controller.route("/", methods=['GET'])
@registration_controller.route("/list", methods=['GET'])
def list():
    return registration_service.list()