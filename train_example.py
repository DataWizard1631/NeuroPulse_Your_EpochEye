# examples/train_example.py
import time

from sdk.neuropulse import init


def train():
    client = init(api_key="dev-key", project="vision/exp1", ingest_url="http://localhost:3000/ingest")

    try:
        for step in range(1, 501):
            # pretend training
            loss = 1.0 / (step**0.5)
            grad_norm = 0.01 * step
            client.log("train/loss", loss, step)
            client.log("train/grad_norm", grad_norm, step)
            if step % 50 == 0:
                print(f"step {step} loss={loss:.4f}")
            time.sleep(0.02)
    finally:
        client.close()


if __name__ == "__main__":
    train()