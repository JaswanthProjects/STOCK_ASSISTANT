import streamlit as st


def create_card(title, url, description):
    st.markdown(f"""
        <div class="resource-card">
            <h2 class="resource-title"><a href="{url}" target="_blank">{title}</a></h2>
            <p class="resource-description">{description}</p>
        </div>
        """, unsafe_allow_html=True)


# Page title
st.markdown("<h1 style='text-align: center; margin-left:660px; width: 200px; margin-bottom:50px'>Resources</h1>", unsafe_allow_html=True)

def create_card_row(resources, horizontal_gap=16, vertical_gap=8, cards_per_row=3):
    # Custom CSS to set the gap between cards
    st.markdown(f"""
        <style>
            .resource-card {{
                padding: 25px;
                border-radius: 8px;
                background-color: #f1f1f1;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
                text-align: center;
                margin-bottom: {vertical_gap}px; /* Vertical gap */
                color: #333;
            }}
            .resource-card:hover {{
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                transform: translateY(-5px);
            }}
            .resource-title {{
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 8px;
                color: #60B4FF;
                text-decoration: none;

            }}

            .st-cf {{
                padding-left: {horizontal_gap // 2}px !important;
                padding-right: {horizontal_gap // 2}px !important;
            }}
        </style>
        """, unsafe_allow_html=True)

    # Break the resources into rows of 'cards_per_row' cards each
    for i in range(0, len(resources), cards_per_row):
        row_resources = resources[i:i + cards_per_row]
        cols = st.columns(cards_per_row)
        for col, resource in zip(cols, row_resources):
            with col:
                create_card(resource['title'], resource['url'], resource['description'])

# Example usage
resources = [
    {"title": "Forbes", "url": "https://www.forbes.com/advisor/investing/how-to-invest-in-stocks/", "description": "Your go-to source for top-level stock investment guidance."},
    {"title": "Webull", "url": "https://www.webull.com/paper-trading?source=paper-trading-gl-search-pc&gad_source=1&gclid=CjwKCAjw5v2wBhBrEiwAXDDoJTIfOWHbdxeWqZIV4Pr2cPhYWD4cy42WIZOM4C86beGnTwncd0AUHxoCyA4QAvD_BwE", "description": "Practice stocks risk-free and with expertise before investing."},
    {"title": "Chase", "url": "https://www.chase.com/personal/investments/advisor-contact-form?sitelink=headline_Persado&jp_cmp=pw/Investment_Non+Brand_Broad_CWM_SEM_US_Desktop_Standard_NA/sea/p77939261548/Non+Brand+-+Investment+Advisors+JPM+Site&gad_source=1&gclid=CjwKCAjw5v2wBhBrEiwAXDDoJf2PFuU34J5ZdutE34btqBWeRljF7IhULFwMVRdGSwapnw6c1IonvRoCoc8QAvD_BwE&gclsrc=aw.ds", "description": "Get credible and personalized advice from Chase's finest advisors."},
    {"title": "Robinhood", "url": "https://www.robinhood.com/us/en/?source=google_sem&utm_source=google&utm_campaign=8140492057&utm_content=84157067517&utm_term=658156483831__how%20to%20invest%20in%20stocks__e&utm_medium=cpc&utm_adgroup=control_nfa&gad_source=1&gclid=CjwKCAjw5v2wBhBrEiwAXDDoJZB3ZJIDw_VQ9SPzUdTBjyf02M0LGe93jfhqjkVG8nHTBXD33EwCPBoCvhoQAvD_BwE", "description": "Invest in stocks easily with Robinhood's user-friendly platform."},
    {"title": "Bestmoney", "url": "https://www.bestmoney.com/investments/compare-stock-brokers?utm_source=google&kw=how%20to%20invest%20in%20stocks&c=686594585195&t=search&p=&m=e&adpos=&dev=c&devmod=&mobval=0&network=g&campaignid=20393160698&adgroupid=157829875576&targetid=kwd-384473610218&interest=&physical=9009919&feedid=&a=&ts=&topic=&clicktype=&camtype=&gad_source=1&gclid=CjwKCAjw5v2wBhBrEiwAXDDoJfMlX7zJNS3qEIiZGReKSa2wd6j_BaYzWjxxyOCxz59Npu7w8So0TxoCotsQAvD_BwE", "description": "Choose Best Stock Market Apps of 2024 and Invest in Innovation."},
    {"title": "Mark Tilbury", "url": "https://www.youtube.com/watch?v=8Ij7A1VCB7I", "description": "IN's and Out's of Stocks with One of the World's Best Investor."},
    # Add more resources if needed
]

# You can customize the horizontal and vertical gaps here
create_card_row(resources, horizontal_gap=30, vertical_gap=20, cards_per_row=3)

# Sidebar content
def sidebar():
    st.sidebar.title("Wallace")
    st.sidebar.write("""**:blue[
        This bot is designed to assist you with stock market information and guidance.
        Use the button on the side bar and in the end of the home page to start your interaction with the bot.
    ]**""")


# Layout the home page
sidebar()


# Footer
st.markdown("---")
st.markdown("""
    Wallace &copy; 2024. All Rights Reserved.
    Developed by :blue[Hough TSA Team #25927-1].
""")
