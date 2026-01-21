from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):

    bot_token: SecretStr

    ADMINS: str
    
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    





config = Settings()

ADMINS = {int(id_str) for id_str in config.ADMINS.split(",")}