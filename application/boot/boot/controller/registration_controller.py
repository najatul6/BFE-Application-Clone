from pweb import Blueprint
from pweb_form_rest import ssr_ui_render

url_prefix = "/"
registration_controller = Blueprint(
    "registration_controller",
    __name__,
    url_prefix=url_prefix
)


@registration_controller.route("/registration", methods=['GET'])
def index():
    return ssr_ui_render(view_name="registration/index")
