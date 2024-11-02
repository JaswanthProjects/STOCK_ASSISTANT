# Stock Assistant Bot
#### Written by Jaswanth Sai Deevela and Rithik Ronald
- The stock bot leverages the power of GPT to understand natural language queries and respond accordingly.
- It seamlessly integrates with the Yahoo Finance API to access real-time stock data.
- The project demonstrates the use of Streamlit for building interactive web applications.
- The project showcases the ability to use function calling API to integrate code execution with GPT's capabilities.
## Motivation and Features:

The video showcases the functionality of the chatbot, allowing users to ask questions about the stock market, including:
- Current stock prices: The chatbot can fetch and display the current stock price of a given company, even without specifying the ticker symbol. For example, you can simply ask "What is the current stock price of Apple?"
- Technical analysis: The chatbot can calculate basic technical indicators, such as the 10-day exponential moving average (EMA), MACD (Moving Average Convergence Divergence), and RSI (Relative Strength Index).
- Stock price plotting: The chatbot can generate and display a Matplotlib plot of the stock price over the last year.
- Competitor identification: The chatbot can identify competitors for a given company.
## Python Functions:

- The program defines various Python functions to handle different tasks:
    - `get_stock_price`: Fetches the latest stock price for a given ticker symbol.
    - `calculate_SMA`: Calculates the simple moving average (SMA) for a given stock and window.
    - `calculate_EMA`: Calculates the exponential moving average (EMA) for a given stock and window.
    - `calculate_RSI`: Calculates the Relative Strength Index (RSI) for a given stock.
    - `calculate_MACD`: Calculates the Moving Average Convergence Divergence (MACD) for a given stock.
    - `plot_stock_price`: Generates and saves a plot of the stock price over the last year for a given ticker.
 
## Installation:

Requirements:
 - An OpenAI API key [Insert your API key in the code]

Steps:
```bash
git clone https://github.com/JaswanthProjects/STOCK_ASSISTANT.git
cd STOCK_ASSISTANT/
pip3 install -r requirements.txt
python -m streamlit run Stock-Assistant.py
```
### Homepage:
![image](https://github.com/JaswanthProjects/STOCK_ASSISTANT/assets/85422176/1740ed0c-ef62-427b-986a-0b3c80c762f1)
### Get Stock Price: 
![image](https://github.com/JaswanthProjects/STOCK_ASSISTANT/assets/85422176/43978743-f76c-4737-911f-d5eabdb1883c)
### Calculate SMA:
![image](https://github.com/JaswanthProjects/STOCK_ASSISTANT/assets/85422176/0fb5812c-f507-4fbb-94d0-cb1c9c1b0cc6)
### Calculate EMA:
![image](https://github.com/JaswanthProjects/STOCK_ASSISTANT/assets/85422176/bf3f3c6f-0001-431c-94e7-461dc4102e8f)
### Calculate RSI: 
![image](https://github.com/JaswanthProjects/STOCK_ASSISTANT/assets/85422176/9e0109cd-695b-4322-ad2b-0cb4a83ee498)
### Plot Stock Price:
![image](https://github.com/JaswanthProjects/STOCK_ASSISTANT/assets/85422176/8320387b-f0a0-406c-98ee-8a81c02eb14c)





