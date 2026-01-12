import os
import time
import threading
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("❌ GEMINI_API_KEY not set")

CONF_THRESHOLD = 0.55
COOLDOWN_SECONDS = 60
AMBIGUOUS_LABELS = {"dog", "cat", "unknown"}

class GeminiValidator:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

        self.last_call_time = 0
        self.running = False
        self.result_text = None

        print("🧠 Gemini validator ready")

    def should_validate(self, detections):
        if not detections:
            return False

        now = time.time()
        if now - self.last_call_time < COOLDOWN_SECONDS:
            return False

        for d in detections:
            if d["confidence"] < CONF_THRESHOLD:
                return True
            if d["label"] in AMBIGUOUS_LABELS:
                return True

        return False

    def validate_async(self, frame, yolo_label):
        if self.running:
            return

        self.running = True
        self.last_call_time = time.time()
        self.result_text = None

        def task():
            try:
                image = Image.fromarray(frame[:, :, ::-1])
                prompt = (
                    f"YOLO detected this object as '{yolo_label}'. "
                    "What is the object actually? Give a short answer."
                )
                response = self.model.generate_content([image, prompt])
                self.result_text = response.text.strip()
            except Exception as e:
                print("⚠️ Gemini error:", e)
            finally:
                self.running = False

        threading.Thread(target=task, daemon=True).start()
