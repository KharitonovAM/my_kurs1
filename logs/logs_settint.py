import logging
from src.setting import Project_Log

mylogconfig = logging.basicConfig(level=logging.DEBUG,
                                  format="%(asctime)s - %(levelname)s- %(name)s - %(message)s",
                                  filename=Project_Log,
                                  filemode="w",
                                  )
