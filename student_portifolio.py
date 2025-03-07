import streamlit as st
import json
import os
import time

# Set the page title
st.set_page_config(page_title="WELCOME TO STUDENT PORTFOLIO", page_icon="🎓", layout="wide")

# File to store user data
DATA_FILE = "user_data.json"

# Function to load user data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to save user data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Load user data
user_data = load_data()

# Initialize session state with user data
def get_user_value(key, default):
    if key not in st.session_state:
        st.session_state[key] = user_data.get(key, default)
    return st.session_state[key]

# Initialize session state variables
get_user_value("name", "Your Name")
get_user_value("location", "Your Location")
get_user_value("bio", "I am passionate about AI and Web Development.")
get_user_value("skills", "Python, JavaScript, SQL, React, Flask")
get_user_value("university", "Your University")
get_user_value("field_of_study", "Your Field of Study")

# Custom Styling
st.markdown("""
    <style>
    html { scroll-behavior: smooth; }
    body {
        background-color: #f4f4f4;
        color: #333;
    }
    .stButton > button, .stDownloadButton > button {
        background-color: #008CBA;
        color: white;
        border-radius: 10px;
        transition: all 0.3s ease-in-out;
        font-weight: bold;
    }
    .stButton > button:hover, .stDownloadButton > button:hover {
        transform: scale(1.05);
        background-color: #005f73;
    }
    a {
        color: #FF5733;
        font-weight: bold;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
        color: #C70039;
    }
    </style>
    """, unsafe_allow_html=True)

# Side navigation 
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Customize Profile", "Contact", "Testimonials"])

# Home Section 
if page == "Home":
    st.title("🎓 WELCOME TO STUDENT PORTIFOLIO")
    st.write("The Student Portfolio Web App is a personalized online profile designed for students to showcase their skills, projects, and achievements in a visually appealing way.")
    st.title(" 🧑Student Profile")
    # Display Profile Picture
    st.image("assets/profile.jpeg", caption='Profile Picture', width=150)
    
    # Display Student Details
    st.subheader("📌 Personal Details")
    st.write(f"**Full Name:** 😎 {st.session_state.name}")
    st.write(f"**Location:** 📍 {st.session_state.location}")
    st.write(f"**Field of Study:** 📚 {st.session_state.field_of_study}")
    st.write(f"**University:** 🏫 {st.session_state.university}")
    
    # Resume Download
    with open("assets/my_resume.pdf", "rb") as file:
        st.download_button(label="📄 Download My Resume", data=file, file_name="My_Resume.pdf")
    
    # Customize Profile Button
    if st.button("🛠 Customize Profile"):
        st.session_state.editing_profile = True
    
    # "Deep Me" Button for More Information
    if st.button("🔍 Deep Me"):
        st.subheader("📌 Additional Information")
        st.write("- **Date of Birth:** 03/08/2001")
        st.write("- **Nationality:** Rwandan")
        st.write("- **Gender:** Male")
        st.write("- **Marital Status:** Single")
        st.write("- **Email:** masongashemap@gmail.com")
        st.write("- **Phone:** 0786781268")
        st.write("- **Residence:** Kigali, Gasabo, Kimihurura")

# Projects Page
elif page == "Projects":
    st.title("💻 Projects")
    
    with st.expander("📊 AI-Based Loan Evaluation System (Final Year Project)"):
        st.write("**Project Type:** Individual Dissertation")
        st.write("**Description:** Developed an AI-powered system to evaluate loan eligibility using OCR and data analysis.")
        st.write("**Technologies:** Python, TensorFlow, Django, PostgreSQL")
        st.write("[GitHub Repository](https://github.com/Songatech02/loan-evaluation)")
    
    with st.expander("📡 Hospital Management System (Year 3 Project)"):
        st.write("**Project Type:** Group Assignment")
        st.write("**Description:** A web-based platform for managing hospital operations including patient records, doctor appointments, and ambulance services.")
        st.write("**Technologies:** HTML, CSS, JavaScript, PHP, MariaDB")
    
    with st.expander("🛍️ E-Commerce Platform (Year 2 Project)"):
        st.write("**Project Type:** Individual Project")
        st.write("**Description:** Built an e-commerce website where users can buy and sell products online.")
        st.write("**Technologies:** React, Firebase, Node.js")

# Skills Page
elif page == "Skills":
    st.title("📊 Skills & Achievements")
    
    st.subheader("📌 Technical Skills")
    st.write("✔ Python")
    st.write("✔ JavaScript")
    st.write("✔ SQL")
    st.write("✔ HTML, CSS, React, Flask")
    
    st.subheader("📌 Certifications & Achievements")
    st.write("✔ Completed Google Data Analytics Certification")
    st.write("✔ Coding Finalist at XYZ University")

# Customize Profile Page
elif page == "Customize Profile":
    st.title("🛠 Customize Your Profile")
    name = st.text_input("Full Name", st.session_state.name)
    location = st.text_input("Location", st.session_state.location)
    university = st.text_input("University", st.session_state.university)
    field_of_study = st.text_input("Field of Study", st.session_state.field_of_study)
    bio = st.text_area("Write your bio", st.session_state.bio)
    skills = st.text_area("Skills", st.session_state.skills)
    
    if st.button("Save Changes"):
        st.session_state.name = name
        st.session_state.location = location
        st.session_state.university = university
        st.session_state.field_of_study = field_of_study
        st.session_state.bio = bio
        st.session_state.skills = skills
        
        user_data.update({
            "name": name,
            "location": location,
            "university": university,
            "field_of_study": field_of_study,
            "bio": bio,
            "skills": skills
        })
        save_data(user_data)
        st.success("Profile updated successfully!")

# #Contact Page
elif page == "Contact":
    st.title("📩 Contact Me")
    st.write("📌 Feel free to reach out to me for any inquiries or collaborations. I am passionate about technology, AI, and web development.")
    
    st.write("📧 **Email:** masongashemap@gmail.com")
    st.write("🔗 [GitHub](https://github.com/Songatech02) 💻")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/masonga-shema-prince-aba095271/) 🌐")
    st.write("🔗 [X](https://x.com/MasongaShema) 🐦")
    
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    if st.button("Send Message"):
        st.success("Message sent successfully!")
        
        # Testimonials Page
elif page == "Testimonials":
    st.title("🗣 Testimonials")
    testimonials = user_data.get("testimonials", [])
    
    if testimonials:
        st.subheader("📌 What others say about me:")
        for testimonial in testimonials:
            st.write(f"- {testimonial}")
    else:
        st.info("No testimonials yet. Be the first to add one!")
    
    new_testimonial = st.text_area("Write a testimonial about me")
    if st.button("Submit Testimonial"):
        if new_testimonial.strip():
            testimonials.append(new_testimonial.strip())
            user_data["testimonials"] = testimonials
            save_data(user_data)
            st.success("Thank you for your feedback!")