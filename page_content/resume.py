import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="CSTRESUME.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("CHEN Siting")

    st.header("Contact Information")
    st.markdown("""
    - **Email**: [chenst2023@outlook.com](mailto:chenst2023@outlook.com)
    - **Phone**: +86 (0757) 13590539472
    """)

    st.header("Professional Summary")
    st.markdown("""
    **Master in Marketing**: Chinese University of Hong Kong, August 2024 - July 2025* (Expected)
    **Bachelor of Finanance**: Lanzhou University, September 2019 - June 2023
    """)

    st.header("Work Experience")
    st.markdown("""
    **Data Analyst in Marketing Analysis Dept, Guangzhou Taiqi Food Co., LTD**
    - *June 2023- April 2024*
    - Spearheaded the collection and management of critical marketing data, ensuring accuracy and integrity in customer, sales, and 
market trend datasets. 
    -  Performed in-depth analysis using statistical tools, translating complex data sets into understandable reports, aiding in strategic 
decision-making processes. 
    -  Assisted in shaping marketing strategies through data-driven insights, influencing product positioning, pricing, and promotional 
activities.
    - Conducted comprehensive market research to identify industry trends and customer preferences, utilizing both qualitative and 
quantitative methodologies. 

    **Corporate Business Intern, China Guangfa Bank Foshan Branch**
    - *July 2022 - August 2022*
    - Became familiar with banking products, daily operation process, and related business policies and regulations
    - Assisted the corporate business department in collecting relevant industry finance-related materials; sorted out and summarized competitive industries and market conditions
    - Made product strategy recommendations with data visualizations and insights  
    - Analyzed business requirements and business cases for products with a data- and hypothesis-driven approach. 
    """)

    st.header("Education")
    st.markdown("""
    ** Master of Marketing
    - Chinese University of Hong Kong | August 2024 - July 2025 (Expected)
    ** Bachelor of Finanance
    - Lanzhou University** | September 2019 - June 2023
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, JavaScript, Java, C++
    - **Web Technologies:** HTML, CSS, React, Node.js, Django
    - **Databases:** MySQL, PostgreSQL, MongoDB
    - **Tools:** Git, Docker, Jenkins, AWS
    - **Soft Skills:** Team Leadership, Project Management, Problem-Solving, Communication
    """)

    st.header("Certifications")
    st.markdown("""
    - IELTS 6.5
    """)

    st.header("Projects")
    st.markdown("""
    ** Research on the Mechanism of Large-scale Poverty Return in Northwest Backward Areas
    - Conducted a comprehensive literature review on the mechanism of large-scale poverty return in Northwest backward areas
    - Developed a model to analyze the impact of poverty alleviation on economic development
    - Maily responsible for data collection and analysis, and wrote a paper on the mechanism of large-scale poverty return in Northwest backward areas
    
    ** Lanzhou University to Zhangye Sunan Yugur Autonomous County Public Welfare Service
    - Interviewed local residents and learned about local culture
    - mainly responsible for organizing members to write project declaration forms and partial closing reports.
    """)

    st.header("Languages")
    st.markdown("""
    - **English:** Native
    - **Chinese:** NativeNative
    """)

    st.header("Interests")
    st.markdown("""
    - Handwork
    - Hiking and outdoor activities
    """)

    st.markdown("---") 