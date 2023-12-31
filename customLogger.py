import logging

class LogGeneration:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s:', datefmt="%m%d%y %I:%m:%s %p")
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
