from pweb import PWebModuleRegister
from boot.boot_module import BootModule
from pweb_ssr.pweb_ssr_module import PWebSSRModule
from pweb_auth import PWebAuthModule
from pweb_ui.pweb_ui_module import PWebUIModul

class Register(PWebModuleRegister):

    def get_module_list(self) -> list:
        return [BootModule,PWebSSRModule,PWebUIModule,PWebAuthModule,]
