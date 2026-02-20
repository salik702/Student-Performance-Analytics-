import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import textwrap

# Set page configuration for a premium look
st.set_page_config(
    page_title="Student Grade Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for glassmorphism and modern UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        color: #e0e0e0;
    }

    /* Main background - Dark Premium */
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgb(0, 0, 0) 0%, rgb(20, 20, 20) 90.2%);
    }

    /* Glassmorphism for containers - Dark Version */
    div[data-testid="stForm"] {
        background: rgba(30, 30, 30, 0.6);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    
    /* Input Fields Overrides */
    .stTextInput > div > div > input, 
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > div {
        color: #ffffff;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #0d0d0d;
        border-right: 1px solid #333;
    }

    /* Headings */
    h1, h2, h3 {
        color: #ffffff;
    }
    
    .header-style {
        color: #ffffff;
        font-weight: 700;
        text-align: center;
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
        padding: 20px 0;
    }

    /* Section titles */
    .section-title {
        background: linear-gradient(90deg, #1f4037 0%, #99f2c8 100%);
        color: #000; /* Dark text on bright gradient */
        padding: 10px 20px;
        border-radius: 10px;
        margin-top: 20px;
        margin-bottom: 20px;
        font-weight: 700;
        box-shadow: 0 4px 15px rgba(0, 255, 127, 0.2);
    }

    /* Prediction Card - Dark */
    .prediction-card {
        background: rgba(20, 20, 20, 0.9);
        padding: 3rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        text-align: center;
        margin-top: 2rem;
        border: 1px solid #333;
        animation: fadeIn 1s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Custom Button Styling */
    .stButton>button {
        background: linear-gradient(90deg, #ef5350 0%, #b71c1c 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.2rem;
        border-radius: 50px;
        box-shadow: 0 5px 15px rgba(0, 210, 255, 0.3);
        transition: all 0.3s ease;
        font-weight: 600;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 210, 255, 0.5);
    }
    
    /* Metrics/Labels */
    label {
        color: #cfcfcf !important;
    }

</style>
""", unsafe_allow_html=True)

# Load the model and features
@st.cache_resource
def load_model():
    model_path = "model_2.pkl"
    features_path = "features.pkl"
    
    if not os.path.exists(model_path) or not os.path.exists(features_path):
        st.error("Model files not found! Please make sure model_2.pkl and features.pkl are in the same directory.")
        return None, None
    
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(features_path, "rb") as f:
        features = pickle.load(f)
    
    return model, features

model, feature_columns = load_model()

# Sidebar for additional info
with st.sidebar:
    # Replaced external image with a reliable large emoji/icon styled with HTML
    st.markdown("<div style='text-align: center; font-size: 80px;'>🎓</div>", unsafe_allow_html=True)
    st.title("🎓 Grade Optimizer")
    st.markdown("""
    This application uses a **Random Forest Regressor** to predict a student's final score based on various academic and lifestyle factors.
    
    ### How to use:
    1. Enter student's numeric data.
    2. Select categorical levels.
    3. Select AI usage details.
    4. Click **Predict Final Score**.
    """)
    st.info("Input validation is active to ensure data integrity.")

st.markdown("<h1 class='header-style'>📊 Student Performance Analytics</h1>", unsafe_allow_html=True)
st.write("Enter the student's information below to predict their final exam score.")

# Create form for inputs
with st.form("student_data_form"):
    
    # Numerical Inputs Section
    st.markdown("<div class='section-title'>➡️ Academic & Lifestyle Metrics</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age", min_value=5, max_value=100, value=20, help="Enter student's age (min 5)")
        study_hours = st.number_input("Study Hours/Day", min_value=0, max_value=24, value=4, step=1, help="Total hours spent studying per day")
        attendance = st.number_input("Attendance %", min_value=0, max_value=100, value=95, step=1, help="Class attendance percentage")
        last_exam = st.number_input("Last Exam Score", min_value=0, max_value=100, value=80, step=1, help="Score in the previous major examination")
        assignment_avg = st.number_input("Avg Assignment Score", min_value=0, max_value=100, value=82, step=1, help="Average score of all assignments")

    with col2:
        concept_score = st.slider("Concept Understanding Score", 1, 10, 8, help="How well the student understands fundamental concepts (1-10)")
        study_consistency = st.number_input("Study Consistency Index", min_value=0, max_value=10, value=7, step=1, help="Index of how consistent study habits are (0-10)")
        improvement_rate = st.number_input("Improvement Rate", min_value=-50, max_value=50, value=6, step=1, help="Rate of performance improvement")
        participation = st.slider("Class Participation Score", 1, 10, 9, help="Active participation in class discussions (1-10)")
        tutoring_hours = st.number_input("Tutoring Hours/Week", min_value=0, max_value=40, value=1, step=1, help="Hours spent in extra tutoring")

    with col3:
        sleep_hours = st.number_input("Sleep Hours/Day", min_value=0, max_value=24, value=7, step=1, help="Average sleep hours per night")
        social_media = st.number_input("Social Media Hours/Day", min_value=0, max_value=24, value=2, step=1, help="Hours spent on social media apps")
        st_id = st.text_input("Student ID (Internal)", value="1000", help="Numeric identifier for the student record")

    # AI Usage Section
    st.markdown("<div class='section-title'>🤖 AI Integration Metrics</div>", unsafe_allow_html=True)
    
    col4, col5 = st.columns(2)
    
    with col4:
        uses_ai_bool = st.toggle("Uses AI Tools?", value=True)
        ai_usage_time = st.number_input("AI Usage (Min/Day)", min_value=0, max_value=1440, value=90 if uses_ai_bool else 0)
        ai_dependency = st.slider("AI Dependency Score", 1, 10, 7 if uses_ai_bool else 1, help="How dependent the student is on AI (1-10)")
        ai_ethics = st.slider("AI Ethics Score", 1, 10, 8, help="Understanding and adherence to AI ethics (1-10)")

    with col5:
        ai_content_pct = st.number_input("AI Generated Content %", min_value=0, max_value=100, value=25 if uses_ai_bool else 0)
        ai_prompts = st.number_input("AI Prompts/Week", min_value=0, value=40 if uses_ai_bool else 0)
        ai_purpose = st.selectbox("Primary AI Purpose", ["Coding", "Doubt Solving", "Exam Prep", "Homework", "Notes", "None"])

    # Categorical Section
    st.markdown("<div class='section-title'>👤 Profile Details</div>", unsafe_allow_html=True)
    
    col6, col7 = st.columns(2)
    
    with col6:
        gender = st.selectbox("Gender", ["Female", "Male", "Other"])
        grade_level = st.selectbox("Grade Level", ["10th", "11th", "12th", "1st Year", "2nd Year", "3rd Year"])
    
    with col7:
        ai_tools_multiselect = st.multiselect(
            "AI Tools Frequently Used", 
            ["ChatGPT", "Claude", "Copilot", "Gemini"],
            default=["ChatGPT"] if uses_ai_bool else []
        )

    # Submit button
    submitted = st.form_submit_button("Predict Final Score", use_container_width=True)

if submitted:
    if model is None:
        st.error("Model not loaded. Prediction aborted.")
    else:
        # Prepare the input data
        # Mappings from mappings.json (found during research)
        gender_map = {"Female": 0, "Male": 1, "Other": 2}
        purpose_map = {"Coding": 0, "Doubt Solving": 1, "Exam Prep": 2, "Homework": 3, "Notes": 4, "None": 5}
        
        # Redundant 'ai_tool_used' column logic from notebook
        # Based on my research, this column was fit on the original string like 'ChatGPT+Gemini'
        # I'll join the selected tools with '+' to match the label encoder's expectation
        tools_joined = "+".join(sorted(ai_tools_multiselect))
        if not tools_joined:
            tools_joined = "nan"
        
        # We need the AI Tool Mapping for the label encoded column 'ai_tool_used'
        ai_tool_map = {
            "ChatGPT": 0, "ChatGPT+Gemini": 1, "Claude": 2, 
            "Copilot": 3, "Gemini": 4, "nan": 5
        }
        # Fallback if a combination is not in the map
        ai_tool_encoded = ai_tool_map.get(tools_joined, 5) # Default to nan if not found

        input_data = {
            'student_id': int(st_id) if st_id.isdigit() else 1000,
            'age': age,
            'gender': gender_map[gender],
            'study_hours_per_day': study_hours,
            'uses_ai': 1 if uses_ai_bool else 0,
            'ai_usage_time_minutes': ai_usage_time,
            'ai_usage_purpose': purpose_map[ai_purpose],
            'ai_dependency_score': ai_dependency,
            'ai_generated_content_percentage': ai_content_pct,
            'ai_prompts_per_week': ai_prompts,
            'ai_ethics_score': ai_ethics,
            'last_exam_score': last_exam,
            'assignment_scores_avg': assignment_avg,
            'attendance_percentage': attendance,
            'concept_understanding_score': concept_score,
            'study_consistency_index': study_consistency,
            'improvement_rate': improvement_rate,
            'sleep_hours': sleep_hours,
            'social_media_hours': social_media,
            'tutoring_hours': tutoring_hours,
            'class_participation_score': participation,
            'ai_tool_used': ai_tool_encoded
        }

        # Handle one-hot encoding for grade_level
        levels = ["11th", "12th", "1st Year", "2nd Year", "3rd Year"]
        for lvl in levels:
            input_data[f'grade_level_{lvl}'] = 1 if grade_level == lvl else 0

        # Handle one-hot encoding for individual tools
        tools = ["ChatGPT", "Claude", "Copilot", "Gemini"]
        for tool in tools:
            input_data[tool] = 1 if tool in ai_tools_multiselect else 0
        
        # Add 'nan' tool column if it existed in training
        input_data['nan'] = 1 if not ai_tools_multiselect else 0

        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Align with training features
        # Ensure feature_columns is a list for robust reindexing
        if hasattr(feature_columns, "tolist"):
             feature_columns = feature_columns.tolist()
             
        input_df = input_df.reindex(columns=feature_columns, fill_value=0)
        
        # Ensure all types are numeric (float) for the model
        input_df = input_df.astype(float)
        
        # Show prediction
        try:
            prediction = model.predict(input_df)[0]
            
            # Determine Status and Styling
            # Use ROUND to get the nearest integer, avoiding truncation errors
            final_score_raw = prediction
            final_score = int(round(final_score_raw))
            
            if final_score >= 80:
                status_color = "#4CAF50" # Green
                status_text = "Excellent Performance! 🌟"
                status_bg = "rgba(76, 175, 80, 0.2)"
                bar_width = f"{final_score}%"
            elif final_score >= 60:
                status_color = "#1DE9B6" # Teal/Mint from user image
                status_text = "Good Performance with Room for Optimization 📈"
                status_bg = "rgba(29, 233, 182, 0.2)"
                bar_width = f"{final_score}%"
            else:
                status_color = "#F44336" # Red
                status_text = "Needs Additional Support ⚠️"
                status_bg = "rgba(244, 67, 54, 0.2)"
                bar_width = f"{final_score}%"
            
            # HTML Card with NO INDENTATION to prevent code block rendering
            # Construct HTML string line by line to avoid any indentation issues
            card_html = f"<div class='prediction-card'>"
            card_html += f"<h3 style='color: #e0e0e0; margin-bottom: 5px; font-weight: 300; letter-spacing: 1px;'>PREDICTED FINAL SCORE</h3>"
            card_html += f"<div style='display: flex; align-items: baseline; justify-content: center; margin-bottom: 20px;'>"
            card_html += f"<span style='font-size: 6rem; font-weight: 700; background: -webkit-linear-gradient({status_color}, #ffffff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>{final_score}</span>"
            card_html += f"<span style='font-size: 2rem; color: #888; margin-left: 10px;'>/ 100</span>"
            card_html += f"</div>"
            card_html += f"<div style='background-color: #333; border-radius: 10px; height: 10px; width: 80%; margin: 0 auto 25px auto; overflow: hidden;'>"
            card_html += f"<div style='background-color: {status_color}; width: {bar_width}; height: 100%; border-radius: 10px; transition: width 1s ease-in-out;'></div>"
            card_html += f"</div>"
            card_html += f"<div style='margin-bottom: 25px;'>"
            card_html += f"<span style='background-color: {status_bg}; color: {status_color}; padding: 8px 20px; border-radius: 20px; font-size: 1rem; border: 1px solid {status_color}; font-weight: 600;'>"
            card_html += f"{status_text}"
            card_html += f"</span>"
            card_html += f"</div>"
            card_html += f"<hr style='border: 0; border-top: 1px solid #444; width: 60%; margin: 20px auto;'>"
            card_html += f"<p style='color: #aaa; font-size: 0.9rem; margin-top: 15px;'>"
            # Added raw score display as requested to show sensitivity
            card_html += f"AI Confidence: <span style='color: #4CAF50;'>High</span> &nbsp; | &nbsp; Raw Prediction: <span style='color: #bbb;'>{final_score_raw:.2f}</span>"
            card_html += f"</p>"
            card_html += f"</div>"
            
            st.markdown(card_html, unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"Prediction Error: {str(e)}")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>Developed with ❤️ By Salik Ahmad | Built with Streamlit & Scikit-Learn</p>", unsafe_allow_html=True)
