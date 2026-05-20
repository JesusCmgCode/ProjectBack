from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

SLURM_HOST = os.getenv("SLURM_HOST", "http://localhost:6820")
SLURM_TOKEN = os.getenv("SLURM_TOKEN", "")

USE_MOCK = os.getenv("USE_MOCK", "True") == "True"