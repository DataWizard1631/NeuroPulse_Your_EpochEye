# sdk/neuropulse/__init__.py
import threading
import time
import requests
import json
from typing import Any, Dict, List


class NeuroPulseClient:
    def __init__(self, api_key: str, project: str, ingest_url: str = "http://localhost:3000/ingest",
                 batch_size: int = 50, flush_interval: float = 1.0):
        self.api_key = api_key
        self.project = project
        self.ingest_url = ingest_url
        self.batch_size = batch_size
        self.flush_interval = flush_interval

        self._buffer: List[Dict[str, Any]] = []
        self._lock = threading.Lock()
        self._stop_event = threading.Event()
        self._thread = threading.Thread(target=self._background_flush, daemon=True)
        self._thread.start()

    def log(self, metric_name: str, value: float, step: int, tags: Dict[str, str] = None):
        event = {
            "project": self.project,
            "metric": metric_name,
            "value": float(value),
            "step": int(step),
            "timestamp": time.time(),
            "tags": tags or {}
        }
        with self._lock:
            self._buffer.append(event)
            if len(self._buffer) >= self.batch_size:
                self._flush_locked()

    def _background_flush(self):
        while not self._stop_event.is_set():
            time.sleep(self.flush_interval)
            with self._lock:
                if self._buffer:
                    self._flush_locked()

    def _flush_locked(self):
        if not self._buffer:
            return
        payload = self._buffer.copy()
        self._buffer.clear()
        try:
            headers = {"Content-Type": "application/json", "X-API-KEY": self.api_key}
            requests.post(self.ingest_url, json=payload, headers=headers, timeout=5)
        except Exception as e:
            # basic retry: put back to buffer for next try
            print("[NeuroPulse SDK] flush failed:", e)
            # naive: prepend payload back
            self._buffer = payload + self._buffer

    def close(self):
        self._stop_event.set()
        self._thread.join(timeout=2)
        with self._lock:
            self._flush_locked()


# convenience factory
def init(api_key: str, project: str, ingest_url: str = "http://localhost:3000/ingest") -> NeuroPulseClient:
    return NeuroPulseClient(api_key=api_key, project=project, ingest_url=ingest_url)