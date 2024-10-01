from pweb import PWebAppConfig


class Config(PWebAppConfig):
    APP_NAME = "BFE-Application-Clone"
    PORT: int = 1212
    
    CONNECT_MESSAGE: str = "PWeb is an Open Source Python based Web Framework for Rapid Development."
    DEVELOPED_BY: str = "Najatul islam"
    DEVELOPED_BY_LINK: str = "https://najatul-islam.vercel.app"
    APP_VERSION: str = "v1.0.0"
    ENABLE_REGISTRATION: bool = True

    