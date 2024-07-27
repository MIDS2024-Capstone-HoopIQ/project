import streamlit as st

def about():
    st.title("About HoopsIQ")

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

    ## Future Work
    - **Model Improvement**: Continuously improving our predictive models for better accuracy.
    - **User Interface**: Enhancing the user interface for better user experience.
    - **Additional Features**: Adding more features such as player comparison and advanced statistics.

    ---

    ## Team
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("./images/anoop.jpeg", caption="Anoop Nair", width=150)
        st.markdown("[Anoop Nair](https://ca.slack-edge.com/T0WA5NWKG-U036K0B99DH-13e5b97869fb-512)")
    
    with col2:
        st.image("./images/iishan.png", caption="Iishan Shekar", width=150)
        st.markdown("[Iishan Shekar](https://ca.slack-edge.com/T0WA5NWKG-U04C1PERAFP-b5839f0ff587-512)")
    
    with col3:
        st.image("./images/aakash.jpeg", caption="Aakash Venkat", width=150)
        st.markdown("[Aakash Venkat](https://ca.slack-edge.com/T0WA5NWKG-U02M5LL1WE9-f713bcd6c2c7-512)")
    
    with col4:
        st.image("./images/IHsiuKao.jpeg", caption="I-Hsiu Kao", width=150)
        st.markdown("[I-Hsiu Kao](https://ca.slack-edge.com/T0WA5NWKG-U049MTV2GDV-488e5391f931-512)")

    # Add more sections as needed
    st.markdown("""
    ## Our Mission
    To provide comprehensive and insightful analysis of WNBA data, leveraging advanced data science techniques to enhance the understanding of the game.

    ## Contact Us
    Feel free to reach out to us for any queries or collaborations.
    """)

# Use the function
about()