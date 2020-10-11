import json
import logging
from datetime import datetime
from typing import Any, Dict


class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = self.make_structured_dict(record)
        if hasattr(record, "exc_info") and record.exc_info:
            payload["stack_trace"] = self.formatException(record.exc_info)
        return json.dumps(payload)

    @staticmethod
    def make_structured_dict(record: logging.LogRecord) -> Dict[str, Any]:
        message_string = record.getMessage()
        if isinstance(record.args, dict):
            user_payload = record.args
        else:
            user_payload = {"value": repr(record.args)}
        return {
            "payload": user_payload,
            "message": message_string,
            "metadata": {
                "timestamp": f"{datetime.utcnow().isoformat()}Z",
                "level": record.levelname,
                "name": record.name,
                "pid": record.process,
                "code": {
                    "filename": record.filename,
                    "file_path": record.pathname,
                    "function_name": record.funcName,
                    "lineno": record.lineno,
                },
            },
        }
