# 🐦 Flappy Bird Gesture Controller using OpenCV & CVZone

## 📌 Project Summary
This project uses your hand gestures to control the **Flappy Bird** game.  
When you open your palm (5 fingers), the bird **jumps** by pressing the spacebar automatically.  
When you close your fist (0 fingers), the bird **falls** as usual.

Built using:
- OpenCV (for webcam)
- CVZone (for hand tracking)
- Python's `keyboard` module (for key press simulation)

---

## 🎮 Controls
| Gesture          | Action             |
|------------------|--------------------|
| ✋ 5 fingers       | Bird jumps (space) |
| ✊ 0 fingers       | No input, bird falls |

---

## 🛠️ Requirements

Install the following Python packages:

```bash
pip install opencv-python cvzone keyboard
