import streamlit as st
from langchain_core.messages import HumanMessage
from tools.conversion_tools import get_conversion_factor, convert
from utils.llm_setup import llm_with_tools
import json

st.set_page_config(page_title="Currency Converter", page_icon="💱", layout="centered")

st.title("💱 Currency converter")

base_currency = st.text_input("Enter \"from currency\" (e.g., INR or USD):").upper()
target_currency = st.text_input("Enter \"to currency\" (e.g., USD or INR):").upper()
amount = st.number_input("Enter amount:", min_value=0.0, step=0.1)

if st.button("Convert"):
    if not base_currency or not target_currency:
        st.warning("Please enter both currencies.")
    else:
        with st.spinner("Fetching conversion rate and calculating..."):
            messages = [HumanMessage(f"What is the conversion factor between {base_currency} and {target_currency}, and based on that can you convert {amount} {base_currency} to {target_currency}")]
            ai_message = llm_with_tools.invoke(messages)
            messages.append(ai_message)

            conversion_rate = None
            result_value = None

            for tool_call in ai_message.tool_calls:
                if tool_call['name'] == 'get_conversion_factor':
                    tool_message1 = get_conversion_factor.invoke(tool_call)
                    conversion_rate = json.loads(tool_message1.content).get('conversion_rate')
                    messages.append(tool_message1)

                if tool_call['name'] == 'convert' and conversion_rate:
                    tool_call['args']['conversion_rate'] = conversion_rate
                    tool_message2 = convert.invoke(tool_call)
                    result_value = tool_message2.content
                    messages.append(tool_message2)

            if result_value:
                st.success(f"✅ {amount} {base_currency} = {result_value} {target_currency}")
            else:
                st.error("Conversion failed. Try again.")