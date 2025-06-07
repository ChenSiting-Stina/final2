import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Data Analyst in Marketing Analysis Dept.
    **Guangzhou Taiqi Food Co., LTD** | *June 2023- April 2024*
    
    - Spearheaded the collection and management of critical marketing data, ensuring accuracy and integrity in customer, sales, and 
market trend datasets. 
    -  Performed in-depth analysis using statistical tools, translating complex data sets into understandable reports, aiding in strategic 
decision-making processes. 
    -  Assisted in shaping marketing strategies through data-driven insights, influencing product positioning, pricing, and promotional 
activities.
    - Conducted comprehensive market research to identify industry trends and customer preferences, utilizing both qualitative and 
quantitative methodologies. 
    """)
    
    st.markdown("""
    ### Corporate Business Intern
    **China Guangfa Bank   Foshan Branch** | *July 2022 - August 2022*
    
    - Became familiar with banking products, daily operation process, and related business policies and regulations
    - Assisted the corporate business department in collecting relevant industry finance-related materials; sorted out and summarized competitive industries and market conditions
    - Made product strategy recommendations with data visualizations and insights  
    - Analyzed business requirements and business cases for products with a data- and hypothesis-driven approach.  
    """)
    
    st.markdown("""
    ### Software Development Intern
    **InnovateTech Solutions** | *May 2020 - August 2020*
    
    - Developed and maintained web applications using Django and React
    - Collaborated with a team of developers using Agile methodologies
    - Implemented new features based on user feedback and requirements
    - Participated in code reviews and testing procedures
    """)
    
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R
        - **Machine Learning:** cursor
        - **Data Processing:** Pandas, NumPy, PySpark
        - **Visualization:** Matplotlib, Seaborn, Tableau, PowerBI
        - **Cloud Platforms:** Google Cloud
        - **Web Development:** Flask
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)
    
    st.markdown("---") 