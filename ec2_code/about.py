import streamlit as st

def about():
    st.title("About HoopsIQ")
    
    st.markdown(
		"""
		<style>
		.big-divider {
			height: 5px;
			background-color: #333;
			margin: 20px 0;
		}
		</style>
		<div class="big-divider"></div>
		""",
		unsafe_allow_html=True
	)

    st.markdown("""
    # HoopsIQ - WNBA Data Analysis
    Welcome to HoopsIQ! Our project is focused on analyzing WNBA data to provide insights and predictions.

    ## Project Overview
    This project leverages advanced data science techniques and machine learning models to analyze WNBA data. We aim to provide detailed insights into player performance, team statistics, and game outcomes.

    ## Key Features
    - **Data Visualization**: Interactive charts and graphs to visualize player and team statistics.
    - **Predictive Modeling**: Machine learning models to predict game outcomes and player performance.
    - **Comprehensive Analysis**: In-depth analysis of game data, including play-by-play and box scores.

    ## Methodology
    Our methodology includes data collection, preprocessing, exploratory data analysis, feature engineering, model training, and evaluation. We use a variety of tools and libraries including Python, Pandas, Plotly, and scikit-learn.

    ## Data Sources
    - **WNBA Official Data**: Data collected from the official WNBA website.
    - **Third-Party APIs**: Additional data from sports data providers.
    - **Custom Data Collection**: Data collected through web scraping and other methods.
    - **Note**: Our dataset includes complete records for the 2018-2023 seasons and partial information (up until May 24, 2024) for the ongoing 2024 season.

    ## Future Work
    - **Model Improvement**: Continuously improving our predictive models for better accuracy.
    - **User Interface**: Enhancing the user interface for better user experience.
    - **Additional Features**: Adding more features such as player comparison and advanced statistics.

    ---

    ## Team
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("./images/anoop.jpeg", caption="", width=150)
        st.markdown("[Anoop Nair](https://www.linkedin.com/in/anooprajnair/)")
    
    with col2:
        st.image("./images/iishaan.png", caption="", width=150)
        st.markdown("[Iishaan Shekhar](https://www.linkedin.com/in/iishaan-shekhar/)")
    
    with col3:
        st.image("./images/akaash.jpeg", caption="", width=147)
        st.markdown("[Akaash Venkat](https://www.linkedin.com/in/akaashvenkat/)")
    
    with col4:
        st.image("./images/IHsiuKao.jpeg", caption="", width=150)
        st.markdown("[I-Hsiu Kao](https://www.linkedin.com/in/ihsiukao/)")

    # Add more sections as needed
    st.markdown("""
    ## Our Mission
    To provide comprehensive and insightful analysis of WNBA data, leveraging advanced data science techniques to enhance the understanding of the game.

    ## Contact Us
    Feel free to reach out to us for any queries or collaborations.
    """)

# Use the function
about()
