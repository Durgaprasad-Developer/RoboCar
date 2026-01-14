# vision/face_recognition/recognizer.py

import os
import numpy as np
from .config import OWNER_THRESHOLD

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
OWNER_PATH = os.path.join(
    BASE_DIR, "..", "models", "identities", "owner.npy"
)

class OwnerRecognizer:
    def __init__(self):
        if not os.path.exists(OWNER_PATH):
            raise FileNotFoundError(
                f"Owner identity not found at {OWNER_PATH}"
            )

        self.owner_emb = np.load(OWNER_PATH)

        # 🔒 HARD CHECK
        if self.owner_emb.shape != (512,):
            raise ValueError(
                f"Invalid owner embedding shape: {self.owner_emb.shape}"
            )

        # Normalize once
        self.owner_emb = self.owner_emb / np.linalg.norm(self.owner_emb)

    def recognize(self, emb):
        emb = emb / np.linalg.norm(emb)

        score = float(np.dot(self.owner_emb, emb))  # cosine similarity

        if score >= OWNER_THRESHOLD:
            return "OWNER", score
        else:
            return "UNKNOWN", score
