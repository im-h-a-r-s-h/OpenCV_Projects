# CricSimulation

## 🏏 About
**CricSimulation** is a real-time AI-powered **cricket batting simulation** using **OpenCV** and **MediaPipe**. You can play cricket **anywhere using any rectangular object** (like a book, phone, or hand) as a bat while your **laptop camera tracks your shots**. The ball is bowled from a fixed **center-right** position, and you can score **sixes, fours, or defend**.

## 🚀 Features
- 🏏 **Hand Tracking** using **MediaPipe**
- 🎯 **Real-time Ball-Bat Collision Detection**
- 🎥 **Webcam-based Game Play**
- 🔢 **Dynamic Score Calculation**
- 🛑 **Game Ends after 10 Balls with Total Score Display**
- 🏆 **Different Shot Types (Six, Four, Defense, Missed Shot)**

## 🖥️ Installation
### 🔹 Prerequisites
Make sure you have **Python 3.7+** installed.

### 🔹 Install Dependencies
Run the following command:
```bash
pip install opencv-python numpy mediapipe
```

## 🎮 How to Play
1️⃣ **Run the script:**
```bash
python main.py
```
2️⃣ **Position your webcam** so it can see your hand or bat.
3️⃣ **Hit the ball** by moving your hand quickly:
   - **Swing fast → SIX 🏏🎯**
   - **Medium speed → FOUR 🔥**
   - **Slow touch → Defensive Shot**
   - **No touch → Missed Shot ❌**
4️⃣ **Game ends after 10 balls**, displaying your **Total Score**.

## 📷 Demo
![Gameplay Demo](https://github.com/im-h-a-r-s-h/OpenCV_Projects/blob/main/Cricket_Simulation%20Game/ss.jpg)

## 📜 Scoring System
| Shot Type       | Points |
|---------------|--------|
| **Six** 🎯   | +6     |
| **Four** 🔥  | +4     |
| **Defensive Shot** | +1     |
| **Missed Shot** ❌ | 0     |

## 🔥 Roadmap
- [ ] **Variable Bowling Speeds**
- [ ] **Boundary Animation for 4s and 6s**
- [ ] **Player Name Input Before the Game**
- [ ] **Multiple Game Modes**

## 🛠️ Contributing
1️⃣ Fork the repository.  
2️⃣ Create a new branch: `git checkout -b feature-branch`  
3️⃣ Commit changes: `git commit -m "Your message"`  
4️⃣ Push to the branch: `git push origin feature-branch`  
5️⃣ Open a **Pull Request** 🚀

## 📄 License
This project is **open-source** and available under the **MIT License**.

---
Made with ❤️ by **Harsh** 🚀

