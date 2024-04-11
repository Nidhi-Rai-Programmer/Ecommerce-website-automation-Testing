import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_directory = ".\\Logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
        log_file_path = os.path.join(log_directory, "automation.log")
        logging.basicConfig(filename=log_file_path,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger