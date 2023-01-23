import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

class Settings:
    SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')
    
    # SECRET_KEY = "19d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    SECRET_KEY = "8c640bfb56270cda1e03bb4aabb8d4b1ca25a054b3a41c1f"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    # PROJECT_TITLE = os.getenv{'PROJECT_TITLE'}
    # PROJECT_VERSION = os.getenv{'PROJECT_VERSION'}
    
    # ROOT_DIR = os.getenv{'ROOT_DIR'}
    # TEMP_DIR = os.getenv{'TEMP_DIR'}
    # WASTE_DIR = os.getenv{'WASTE_DIR'}
    # GIF = os.getenv{'GIF'}
    # WEBP = os.getenv{'WEBP'}

    # FRAME_MIN: int = 10
    # FRAME_MAX: int = 60
    # GIF_SIZE:int = 480              # gif 가로크기

    # PAGE: int = 10                  # pagination
    # _PAGESIZE: int = 18             # pagination 
    # RESOLUTION_HIGHT = 560000       # 864 * 648 = 559,872
    # RESOLUTION_LOW = 76000          # 360 * 240 = 86,400

    # CHUNK_SIZE = 1024 * 1024
    
    
    # ###############---<CHAT>---###############
    # REDIS_HOST = 'localhost'
    # REDIS_PORT = 6379
    # XREAD_TIMEOUT = 0
    
    # XREAD_COUNT = 100
    # NUM_PREVIOUS = 30
    # STREAM_MAX_LEN = 1000
    # ALLOWED_ROOMS = ['chat:1', 'chat:2', 'chat:3']

settings = Settings()