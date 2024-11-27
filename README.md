# India States Guessing Game

## 📋 Overview  
The **India States Guessing Game** is an interactive Python application that uses the Turtle graphics and Pandas library to create a fun and educational way for students to learn the states of India. The goal is to guess as many Indian states as possible. At the end of the game, any missed states are saved to a separate CSV file (`missing-state.csv`), which students can use to learn and improve.

---

## 🚀 Features  
- Interactive map of India using Turtle graphics.  
- Allows users to guess Indian states with real-time feedback.  
- Keeps track of guessed and missed states.  
- Generates a CSV file of missed states for further learning.  

---

## 📂 Files Required  
1. **Python Script**: The provided game script.  
2. **India Map Image (statesimg.gif)**: A map image file for the game.  
3. **States Data CSV (state.csv)**: A CSV file containing Indian states and their respective `x` and `y` coordinates.  
    - Example format:
      ```
      State,x,y
      Maharashtra,100,200
      Tamil Nadu,-150,-250
      ```

---

## 🖥️ How to Run  

### Prerequisites  
1. **Python Installed**: Ensure Python 3.7+ is installed on your system.  
2. **Required Libraries**: Install the necessary libraries using pip:  
   ```bash
   pip install pandas
   ```

### Steps to Run  
1. Place all required files (**Python script**, **statesimg.gif**, **state.csv**) in the same folder.  
2. Open a terminal/command prompt in the folder and run the script:  
   ```bash
   python <script_name>.py
   ```
3. Follow the on-screen prompts to guess Indian states. Type the names of states to play.  
4. Type **exit** to end the game. A CSV file named `missing-state.csv` will be generated with the states you missed.  

---

## 🎓 Benefits for Students  
- **Geography Learning**: Encourages users to learn and memorize the states of India.  
- **Immediate Feedback**: Visual representation of guessed states on the map.  
- **Mistake Learning**: Highlights missed states for further practice and learning.  
- **Interactive & Fun**: Combines education with gameplay, making it engaging.  
- **CSV Handling Practice**: Demonstrates how Python can manipulate CSV files for storing data.  

---

## 🔎 How It Works  
1. **Interactive Gameplay**:  
   - The map is displayed using the Turtle module, and users are prompted to guess a state.  
   - If the guess is correct, the state name is displayed on the map.  

2. **Tracking Progress**:  
   - Keeps track of correctly guessed states and scores.  
   - Stops when all states are guessed or the user chooses to exit.  

3. **Saving Missed States**:  
   - States not guessed by the user are saved to a `missing-state.csv` file for further study.  

---

## 📈 Example Output  
### Console:  
```text
Guess the State(5/33): Maharashtra
Guess the State(6/33): Tamil Nadu
```

### Map:  
State names appear on the map when guessed correctly.  

### `missing-state.csv`:  
```csv
State
Kerala
Assam
Goa
```

---

## 💡 Educational Use  
- **Classroom Activity**: Teachers can use it to test and improve students' knowledge of Indian geography.  
- **Self-Improvement**: Students can practice and track their progress.  
- **Data Analysis**: A great way for beginners to explore Python's CSV and Turtle modules.  

---

## 📜 License  
This project is free to use for educational purposes. Feel free to modify and share!  

**Enjoy Learning! 🌍**
