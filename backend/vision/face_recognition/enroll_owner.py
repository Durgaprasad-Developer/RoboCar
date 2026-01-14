# vision/face_recognition/enroll_owner.py

import os
import time
import numpy as np
from insightface.app import FaceAnalysis
from vision.camera import Camera

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
OWNER_PATH = os.path.join(
    BASE_DIR, "..", "models", "identities", "owner.npy"
)

SAMPLES = 20

def main():
    app = FaceAnalysis(name="buffalo_l")
    app.prepare(ctx_id=0, det_size=(640, 640))

    cam = Camera()
    embeddings = []

    print("Owner enrollment started")

    while len(embeddings) < SAMPLES:
        frame = cam.get_frame()
        if frame is None:
            continue

        faces = app.get(frame)
        if len(faces) == 1:
            emb = faces[0].embedding
            emb = emb / np.linalg.norm(emb)
            embeddings.append(emb)
            print(f"Captured {len(embeddings)}/{SAMPLES}")

        time.sleep(0.1)

    cam.release()

    owner_emb = np.mean(embeddings, axis=0)
    owner_emb = owner_emb / np.linalg.norm(owner_emb)

    os.makedirs(os.path.dirname(OWNER_PATH), exist_ok=True)
    np.save(OWNER_PATH, owner_emb)

    print("Owner enrolled successfully")

if __name__ == "__main__":
    main()
