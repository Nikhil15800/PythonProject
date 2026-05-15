import os
from datetime import datetime


class Config:
    RUN_ID = datetime.now().strftime("%H%M%S")

    BASE_URL = os.getenv(
        "BASE_URL",
        "https://automationexercise.com/",
    )
    USERNAME = f"testuser_{RUN_ID}"
    EMAIL = f"testuser_{RUN_ID}@yopmail.com"
    PASSWORD = f"Test@{RUN_ID}"
