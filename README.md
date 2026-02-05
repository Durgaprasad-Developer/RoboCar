# 🤖 RoboCar

A **modular autonomous robot system** with vision + brain + web dashboard.

Supports:

* Manual & autonomous control
* Ball tracking
* Face recognition (owner detection)
* Object detection (labels only)
* Single shared camera pipeline

Built with a **clean brain architecture** so features don’t block or freeze each other.

---

## ✨ Features

* 🧠 Central brain loop (decision → motion → safety)
* 👁️ Vision modules (ball, face, objects)
* 🎮 Multiple control modes
* 🖥️ Real-time dashboard
* 🔒 Safety overrides always active

---

## 🎮 Modes

```
IDLE
MANUAL
AUTO
TRACK_BALL
FOLLOW_OWNER
DETECT_OBJECT
```

Only the **active mode’s vision pipeline runs**.

---

## 🗂️ Project Structure

```
robo_car/
├── backend/
│   ├── main.py
│   ├── core/            # brain, decision, motion, safety
│   ├── vision/          # camera + vision modules
│   ├── api/             # REST APIs
│   └── control/         # motor control
│
├── dashboard/           # React frontend
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements

### System

* Python **3.10**
* Node.js **18+**
* USB / Webcam

### Important Python Notes

* Use **NumPy 1.24.4**
* NumPy 2.x breaks Torch / YOLO

---

## 🧪 Setup

### 1️⃣ Clone

```bash
git clone <repo-url>
cd robo_car
```

### 2️⃣ Backend Environment

```bash
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

If NumPy breaks:

```bash
pip uninstall -y numpy
pip install numpy==1.24.4
```

---

## 🚀 Run the System

### ▶️ Backend (Brain + Vision + API)

```bash
cd backend
source ../venv/bin/activate
python main.py
```

Backend:

```
http://localhost:8000
```

---

### ▶️ Dashboard

```bash
cd dashboard
npm install
npm run dev
```

Dashboard:

```
http://localhost:5173
```

---

## 🧪 Test Vision Modules Individually

### 🟠 Ball Tracking

```bash
source venv/bin/activate
cd backend
python vision/ball_tracking/test_ball_tracking.py
```

---

### 🔵 Object Detection

```bash
source venv/bin/activate
python -m backend.vision.object_detection.test_object_detection
```

---

### 🟢 Face Recognition

> Uses a **separate environment** (`venv_face`)

```bash
source venv_face/bin/activate
cd backend
python -m vision.face_recognition.main
```

OR

```bash
source venv_face/bin/activate
cd backend
python -m vision.face_recognition.test_engine
```

Returns:

```
OWNER | UNKNOWN | NONE
```

---

## 👁️ Vision Behavior

### Face Recognition

* InsightFace embeddings
* Compares with stored owner face
* No drawing, logic-only output

### Object Detection

* YOLOv8 Nano
* Labels only (no tracking, no boxes)
* Dashboard + brain safe

---

## 🛡️ Safety Logic

* Obstacle sensor always active
* Motion priority:

```
STOP > SAFETY > MODE > MANUAL
```

States:

```
CLEAR | WARNING | BLOCKED
```

---

## 🧠 Design Rules

* Vision returns **facts only**
* Brain makes **decisions**
* Motion handles **actuation**
* One camera, one loop
* Mode-gated vision

Result: stable, debuggable, hardware-ready.

---

## 🔮 Planned

* Follow-owner motion logic
* Keyboard / joystick driving
* Mobile dashboard
* ROS support
* Multi-camera

---

## 📜 License

Open for learning and experimentation.
Fork it. Break it. Build on it.

---

## 🙌 Author

Built with discipline.
**Win with discipline.**


