# examples/lightning_callback.py
from pytorch_lightning.callbacks import Callback
from sdk.neuropulse import init


class NeuroPulseCallback(Callback):
    def __init__(self, api_key: str, project: str, ingest_url: str = "http://localhost:3000/ingest"):
        super().__init__()
        self.client = init(api_key=api_key, project=project, ingest_url=ingest_url)

    def on_validation_end(self, trainer, pl_module):
        # example: log val_loss
        avg_loss = trainer.callback_metrics.get('val_loss')
        step = trainer.global_step
        if avg_loss is not None:
            self.client.log('val/loss', float(avg_loss), step)

    def on_train_end(self, trainer, pl_module):
        self.client.close()