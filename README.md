# 🎓 STUDENT GRADE PREDICTOR & OPTIMIZER 🚀

The **Student Grade Predictor** is a next-generation, interactive Streamlit application powered by machine learning. It predicts a student's final exam score with exceptional precision by analyzing academic habits, lifestyle choices, and—uniquely—**AI tool usage patterns**. 

Designed for educators, students, and analysts, this tool provides actionable insights into how factors like sleep, study consistency, and ethical AI integration influence academic performance.

## 🌐 Live Demo

[🚀 Launch the App](https://student-performance-salik.streamlit.app/)

## 🖼️ Preview

<div align="center">
  <img width="872" height="361" alt="image" src="https://github.com/user-attachments/assets/6799a35d-be75-40f5-a374-cde45164f80a" />

</div>

> *A stunning, glassmorphism-inspired dark UI that makes data analysis a visual delight.*

---

## 🚀 Key Features

### 🔮 **Precision Grade Forecasting**
- Leverages a **Random Forest Regressor🌳** to predict final scores with high accuracy.
- Analyzes complex non-linear relationships between 20+ variables.

### 🤖 **AI Usage Analytics (Unique!)**
- Tracks the impact of AI tools (**ChatGPT, Gemini, Claude**) on learning.
- Evaluates metrics like **AI Dependency**, **Ethics Score**, and **Prompting Frequency**.
- Distinguishes between healthy assistance and over-reliance.

### 📊 **Holistic Student Profiling**
- **Academic Metrics**: Study Hours, Attendance, Past Performance.
- **Lifestyle Factors**: Sleep Quality, Social Media Consumption.
- **Interactive Inputs**: Real-time sliders and toggles for dynamic "what-if" analysis.

### 🎨 **Premium User Experience**
- **Glassmorphism Design**: Modern, translucent containers with blur effects.
- **Responsive Layout**: Seamlessly adapts to desktop and tablet screens.
- **Dynamic Visuals**: Animated progress bars and color-coded performance cards.

---

## 🛠️ Tech Stack

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
</div>

---

## 📦 Installation (Local Setup)

Get the application running on your local machine in minutes.

**1. Clone the repository**

```bash
git clone <your-repo-url>
cd student-grade-predictor
```

**2. Set up virtual environment (Recommended)**

*Windows:*
```bash
python -m venv venv
.\venv\Scripts\activate
```

*macOS/Linux:*
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Launch the App**

```bash
streamlit run app.py
```

---

## 📈 Model Performance

- **Algorithm:** Random Forest Regressor🌳
- **Random Forest Regressor Performance:**
  - **Mean Absolute Error:** `4.1064`
  - **Mean Squared Error:** `26.7775`
  - **R² Score:** `0.8560`
- **Key Predictors:** Past Grades, Study Consistency, AI Ethics Score.

---

## 💡 How It Works

1.  **Input Data**: User provides academic history and lifestyle details via the sidebar and main form.
2.  **AI Analysis**: The system evaluates the student's relationship with AI tools (Dependency vs. Productivity).
3.  **Processing**: Inputs are encoded and scaled to match the training distribution.
4.  **Prediction**: The Random Forest model generates a predicted final score out of 100.
5.  **Insight**: The app categorizes the student as "Excellent", "Good", or "Needs Support" with visual feedback.

---

## 🤝 Contribution

We welcome contributions! Whether it's adding new features, improving the UI, or optimizing the model:

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📝 License

This project is open-source and available for free.

---

<div align="center">

<h3>Made with ❤️ by <b>Salik Ahmad</b></h3>

<p>
  <a href="https://salikahmad.vercel.app/" target="_blank">
    <img src="https://img.shields.io/badge/Website-🌐-blue?style=for-the-badge&logo=about.me&logoColor=white" alt="Website Badge"/>
  </a>
  <a href="https://www.linkedin.com/in/salik-ahmad-programmer/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-🔗-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="https://www.kaggle.com/salikahmad702" target="_blank">
    <img src="https://img.shields.io/badge/Kaggle-📊-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" alt="Kaggle Badge"/>
  </a>
</p>

<p style="font-size:14px; color:gray;">
  <em>© 2026 <b>Salik Ahmad</b>. All rights reserved. ☕ AI/ML Engineer</em>
</p>

</div>
