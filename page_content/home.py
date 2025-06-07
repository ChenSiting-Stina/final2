import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Chen Siting</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="mailto:sarah.johnson@example.com">sarah.johnson@example.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "4：5.jpeg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I am a recent master's graduate in Master from the Chinese Universitu of Hong kong, eager to apply my knowledge and skills in a professional setting. During my academic journey, I developed a strong foundation in marketing and big data analysis.
        """
    )

    st.markdown(
        """
        ### Skills
        - **Programming Languages:** Python, R
        - **Machine Learning:** cursor
        - **Data Processing:** Pandas, NumPy, PySpark
        - **Visualization:** Matplotlib, Seaborn, Tableau, PowerBI
        - **Cloud Platforms:** Google Cloud
        - **Web Development:** Flask
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 