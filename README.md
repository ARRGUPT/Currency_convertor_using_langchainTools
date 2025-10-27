# 💱 Currency Converter

A real-time currency conversion application built with Streamlit and LangChain that uses the ExchangeRate API for accurate currency conversions.

## Features

- 🔄 Real-time currency conversion
- 🤖 LLM-powered interface using Groq's LLaMA model
- 🌐 Support for multiple currencies worldwide
- ⚡ Fast conversion using ExchangeRate API
- 🛠️ Tool-augmented LLM for accurate calculations

## Setup

1. Install dependencies:
```bash
pip install streamlit langchain-groq python-dotenv requests
```

2. Set up environment variables in `.env`:
```
GROQ_API_KEY=your_groq_api_key
EXCHANGERATE_API_KEY=your_exchangerate_api_key
```

## Project Structure

```
Project_usingTools_currency_converter_app/
├── app.py                  # Main Streamlit application
├── tools/
│   └── conversion_tools.py # Currency conversion tools
└── utils/
    └── llm_setup.py       # LLM configuration
```

## How It Works

1. **Tool-based Architecture**
   - Uses LangChain tools for currency conversion
   - Integrates with ExchangeRate API for accurate rates
   - Leverages Groq's LLaMA model for natural language understanding

2. **Conversion Process**
   - Fetches real-time exchange rates
   - Performs precise calculations
   - Provides instant results through a user-friendly interface

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Enter the required information:
   - Base currency (e.g., USD, EUR, INR)
   - Target currency (e.g., EUR, USD, GBP)
   - Amount to convert

3. Click "Convert" to see the result

## API Reference

The application uses the ExchangeRate API v6 for currency conversion data:
- Endpoint: `https://v6.exchangerate-api.com/`
- Free tier available
- Supports multiple currency pairs

## Notes

- Currency codes should be in standard 3-letter format (USD, EUR, GBP, etc.)
- Conversion rates are fetched in real-time for accuracy
- The application requires an active internet connection

## License

This project is open-source and available under the MIT License.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [LangChain](https://www.langchain.com/)
- Uses [ExchangeRate API](https://www.exchangerate-api.com/)
- LLM support by [Groq](https://groq.com/)


## Streamlit app
Link:- (https://arrgupt-currency-convertor-using-langchaintools-app-6yzkmf.streamlit.app/)