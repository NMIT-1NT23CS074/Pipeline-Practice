import streamlit as st

# ------------------ Page Config ------------------
st.set_page_config(page_title="Course Recommender", layout="wide")

# ------------------ Custom CSS ------------------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    .card {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ Title ------------------
st.title("🚀 LearnHub - Course Recommendation App")

# ------------------ Registration Form ------------------
st.header("📋 Register Here")

with st.form("registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    interest = st.selectbox(
        "Select Your Interest",
        ["Web Development", "Data Science", "AI/ML", "Cloud Computing"]
    )

    submit = st.form_submit_button("Register")

# ------------------ After Submission ------------------
if submit:
    st.success(f"Welcome {name}! 🎉 Here are recommended courses for you:")

    st.markdown("---")

    # ------------------ Course Recommendations ------------------
    if interest == "Web Development":
        st.subheader("🌐 Web Development Courses")
        st.markdown('<div class="card">HTML, CSS & JavaScript Basics</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">React JS Full Course</div>', unsafe_allow_html=True)

        st.video("https://www.youtube.com/watch?v=UB1O30fR-EE")

    elif interest == "Data Science":
        st.subheader("📊 Data Science Courses")
        st.markdown('<div class="card">Python for Data Science</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">Pandas & NumPy Tutorial</div>', unsafe_allow_html=True)

        st.video("https://www.youtube.com/watch?v=ua-CiDNNj30")

    elif interest == "AI/ML":
        st.subheader("🤖 AI & Machine Learning Courses")
        st.markdown('<div class="card">Machine Learning Basics</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">Deep Learning Introduction</div>', unsafe_allow_html=True)

        st.video("https://www.youtube.com/watch?v=GwIo3gDZCVQ")

    elif interest == "Cloud Computing":
        st.subheader("☁️ Cloud Computing Courses")
        st.markdown('<div class="card">AWS Basics</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">Google Cloud Fundamentals</div>', unsafe_allow_html=True)

        st.video("https://www.youtube.com/watch?v=3hLmDS179YE")