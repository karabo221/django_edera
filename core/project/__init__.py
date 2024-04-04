import os
from pathlib import Path
from decouple import Csv, config
from dotmap import DotMap
#init env
ENV = DotMap({'config': config,'Csv': Csv})

BASE_DIR = Path(__file__).resolve().parent.parent
ADMIN_PATH = ENV.config('ADMIN_PATH')
