import streamlit as st


# Set the page configuration for the Streamlit app
st.set_page_config(
    page_title="Stock Assistant Bot",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

# Define the main content of the home page
def main():
    st.title("Stock Assistant Bot")
    st.image("stock-market.jpg", use_column_width=True)  # Replace with your own image path or URL
    
    # src="https://wallpapers.com/stock-market"

    st.markdown("""
        ## Welcome to the Future!
        
        In the fast-paced world of stock trading, having accurate and timely information is crucial. 
        However, investors often face the challenge of sifting through vast amounts of data and 
        dealing with misinformation. Our Stock Assistant Bot is here to help!
        
        ### The Problem
        - **Information Overload:** The sheer volume of stock data available can be overwhelming for both new and experienced investors.
        - **Misguidance:** It's easy to encounter conflicting advice and analysis that can lead to poor investment decisions.
        - **Accessibility:** Finding all the relevant information in one place is often a tedious and time-consuming task.
        
        ### Our Solution
        Wallace simplifies your investment journey by providing:
        
         - **Real-time Stock Prices**: Get the latest closing price for any stock symbol.
         - **Technical Analysis**: Calculate key indicators like Simple Moving Average (SMA), Exponential Moving Average (EMA), Relative Strength Index (RSI), and Moving Average Convergence Divergence (MACD).
         - **Historical Charts**: Visualize the stock price movement over the last year with a generated plot.
         - **Interactive Experience**: Engage with the bot through natural language input to receive stock information and analysis.
         - **Data-Driven Insights**: Leverage advanced calculations and visualizations to inform your investment decisions.
        
        Ready to make informed investment decisions with confidence? Let's get started!
    """)


    # Call-to-action button
    if st.page_link("pages/1_Stock-Assistant.py", label=':blue[Talk to Wallace]',use_container_width=None):
        # You can redirect the user to another page or perform some action here
        # For example, you could use st.session_state to track the interaction
        st.session_state['bot_interaction'] = True
        # Redirect to the bot interaction page (you'll need to implement this)
        # st.write("This will take you to the bot interaction page.")

    # Display a message if the user has clicked the button
    if 'bot_interaction' in st.session_state and st.session_state['bot_interaction']:
        st.success(" Click Above to Interact!")
        #time.sleep(2)
        st.snow()


# Sidebar content
def sidebar():
    st.sidebar.title("Wallace")
    st.sidebar.write("""**:blue[
        This bot is designed to assist you with stock market information and guidance.
        Use the button on the side bar and in the end of the home page to start your interaction with the bot.
    ]**""")

# Layout the home page
sidebar()
main()

# Footer
st.markdown("---")
st.markdown("""
    Wallace &copy; 2024. All Rights Reserved.
    Developed by :blue[Hough TSA Team #25927-1].
""")