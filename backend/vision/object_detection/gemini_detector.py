import os
import json
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
from google.generativeai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("❌ GEMINI_API_KEY not set")

class GeminiVisionDetector:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-2.5-flash")
        print("🧠 Gemini Vision fallback ready")

    def detect(self, frame):
        try:
            h, w, _ = frame.shape
            image = Image.fromarray(frame[:, :, ::-1])

            prompt = (
                "Detect prominent objects. "
                "Return JSON list with label and box_2d "
                "[ymin, xmin, ymax, xmax] normalized to 0-1000."
            )

            response = self.model.generate_content(
                contents=[image, prompt],
                generation_config=types.GenerationConfig(
                    response_mime_type="application/json"
                )
            )

            raw = json.loads(response.text)
            detections = []

            for d in raw:
                y1, x1, y2, x2 = d["box_2d"]
                detections.append({
                    "label": d["label"],
                    "confidence": 0.9,
                    "bbox": (
                        int(x1/1000*w),
                        int(y1/1000*h),
                        int(x2/1000*w),
                        int(y2/1000*h)
                    )
                })
            return detections

        except Exception as e:
            print("⚠️ Gemini failed:", e)
            return []
