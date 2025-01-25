import streamlit as st
from dotenv import load_dotenv
from resume_parser import parse_resume
from career_model import CareerPathRecommender

# Load environment variables
load_dotenv()

# Streamlit App
st.title("Career Path Recommender")
st.write("Upload your resume to get personalized career path recommendations!")

# File uploader for resume
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    try:
        # Parse the resume
        st.write("Parsing your resume...")
        resume_data = parse_resume(uploaded_file)

        # Initialize the recommender
        recommender = CareerPathRecommender()

        # Get recommendations
        career_paths = recommender.get_recommendations(resume_data)

        # Display the recommendations
        if isinstance(career_paths, str):
            st.success(f"Recommended Career Path: {career_paths}")
        else:
            st.error("No recommendations available. Please try again with a more detailed resume.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
