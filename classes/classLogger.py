import logging

from typing import Dict, Any, List

class Logger(logging.Logger):
    def __init__(self, loggerName: str, config: Dict[str, Any]) -> None:
        ## initialise class
        super().__init__(loggerName)
        self.config: Dict[str, Any] = config

        ## formatter
        self.f: logging.Formatter = logging.Formatter(self.config["format"])
        
        ## handlers
        self.sh: logging.Handler = logging.StreamHandler()
        self.fh: logging.Handler = logging.FileHandler(self.config["filename"])
        
        for h in [self.sh, self.fh]:
            h.setLevel(self.config["level"])
            h.setFormatter(self.f)
            self.addHandler(h)

        self.setLevel(self.config["level"])