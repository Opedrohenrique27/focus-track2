from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Focus Track"
    app_version: str = "1.0.0"
    database_url: str = "sqlite:///./focus_track.db"
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = True
    quotes_api_url: str = "https://zenquotes.io/api/random"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
