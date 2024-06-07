import streamlit as st

# Set up the main header and logo
st.image("/Files/Images/FWS_Logo.png", width=200)
st.title("Footwear Studios - Projektmanagement")

# Project Details Section
st.header("Project Details")
project_name = st.text_input("Project name")
production_location = st.text_input("Production location")
total_order_number = st.text_input("Total order number")
last_updated_by = st.text_input("Last Updated by")
date = st.text_input("Date (ddmmyy)")

# Phase 1: Material Testing Section
st.header("Phase 1: Material Testing")
st.write("Material samples are provided to CTC for testing. The materials are intended to be used for production. Once CTC confirms, we place bulk order. Color do not matter at this stage.")

# Create a function to display test details table
def display_test_details(part_name, tests):
    st.subheader(f"Concerned part: {part_name}")
    for test in tests:
        st.write(f"**Test:** {test['name']}")
        test['material'] = st.text_input("Material", key=f"{test['name']}_material")
        test['eco_content'] = st.text_input("Eco-content", key=f"{test['name']}_eco_content")
        st.write(f"**Method reference:** {test['method_reference']}")
        st.write(f"**Target value:** {test['target_value']}")
        st.write(f"**Applicable:** {test['applicable']}")
        st.write(f"**Cost EUR:** {test['cost_eur']}")
        st.write(f"**Cost USD:** {test['cost_usd']}")
        st.write(f"**Cost RMB:** {test['cost_rmb']}")
        test['test_deadline'] = st.text_input("Test deadline", key=f"{test['name']}_test_deadline")
        test['test_result'] = st.text_input("Test result", key=f"{test['name']}_test_result")
        test['value_recorded'] = st.text_input("Value recorded", key=f"{test['name']}_value_recorded")
        test['comments'] = st.text_input("Comments", key=f"{test['name']}_comments")

# Upper part tests
upper_tests = [
    {"name": "Resistance to tear strength", "method_reference": "ISO 17696", "target_value": "", "applicable": "FALSE", "cost_eur": "48,00€", "cost_usd": "", "cost_rmb": "126,00¥"},
    {"name": "Flexion resistance (dry and wet)", "method_reference": "NF EN ISO 17694", "target_value": "", "applicable": "FALSE", "cost_eur": "83,00€", "cost_usd": "", "cost_rmb": "782,00¥"},
    {"name": "Water resistance", "method_reference": "ISO 17702", "target_value": "", "applicable": "FALSE", "cost_eur": "89,50€", "cost_usd": "", "cost_rmb": "369,00¥"},
]

display_test_details("Upper", upper_tests)

# Lining / Tongue part tests
lining_tongue_tests = [
    {"name": "Abrasion resistance", "method_reference": "EN 13520 / ISO 17704", "target_value": "", "applicable": "FALSE", "cost_eur": "101,50€", "cost_usd": "", "cost_rmb": "273,00¥"},
]

display_test_details("Lining / Tongue", lining_tongue_tests)

# Insole part tests
insole_tests = [
    {"name": "Determination of water absorption", "method_reference": "EN ISO 22649", "target_value": "", "applicable": "FALSE", "cost_eur": "71,00€", "cost_usd": "", "cost_rmb": ""},
]

display_test_details("Insole", insole_tests)

# Laces part tests
laces_tests = [
    {"name": "Abrasion resistance of shoe laces", "method_reference": "ISO 22774", "target_value": "", "applicable": "FALSE", "cost_eur": "77,50€", "cost_usd": "", "cost_rmb": "304,00¥"},
    {"name": "Shoe lace breaking strength", "method_reference": "CTC Method", "target_value": "", "applicable": "FALSE", "cost_eur": "101,50€", "cost_usd": "", "cost_rmb": ""},
]

display_test_details("Laces", laces_tests)

# Outsole part tests
outsole_tests = [
    {"name": "Flex resistance", "method_reference": "ISO 22774", "target_value": "", "applicable": "FALSE", "cost_eur": "77,50€", "cost_usd": "", "cost_rmb": "304,00¥"},
]

display_test_details("Outsole", outsole_tests)
