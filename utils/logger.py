# utils/logger.py
import logging
from datetime import datetime

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to log request success and time taken
def log_request_success(start_time, endpoint):
    end_time = datetime.now()
    time_taken = end_time - start_time
    logger.info(f"Request to {endpoint} successful. Time taken: {time_taken}")
