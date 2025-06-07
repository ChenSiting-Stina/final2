import streamlit as st

def education_page():
    st.markdown("## Education")
    
    st.markdown("""
    ### Master of Marketing
    **Chinese University of Hong Kong | *August 2024 - July 2025 (Expected)*
    
    - GPA: 3.9/4.0
    - Relevant Coursework: machine learning in marketing, social media anatics, customer analysis
    
    ### Bachelor of Finanance
    **Lanzhou University** | *September 2019 - June 2023*

    
    - GPA: 3.5/4.0
    - Relevant Coursework: financial analysis, quantitative analysis, macroeconomics， microeconomics, International Trade
    """)
    
    st.markdown("---")
    
    st.markdown("## Certifications")
    
    cert1, cert2, cert3 = st.columns(3)
    
    with cert1:
        st.markdown("""
        ### IELTS 6.5
        **Issued by**: Cambridge University
        **Date**: 2023

        """)
        

        
    
    st.markdown("---")
    
    st.markdown("## Academic Projects")
    
    st.markdown("""
    ### Research on the Mechanism of Large-scale Poverty Return in Northwest Backward Areas
    - Conducted a comprehensive literature review on the mechanism of large-scale poverty return in Northwest backward areas
    - Developed a model to analyze the impact of poverty alleviation on economic development
    - Maily responsible for data collection and analysis, and wrote a paper on the mechanism of large-scale poverty return in Northwest backward areas
    
    ### Lanzhou University to Zhangye Sunan Yugur Autonomous County Public Welfare Service
    - Interviewed local residents and learned about local culture
    - mainly responsible for organizing members to write project declaration forms and partial closing reports.
    """)
    
    st.markdown("---") 