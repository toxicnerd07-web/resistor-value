import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Resistor Virtual Lab",
    page_icon="🔬",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
.title{
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#0b6cf0;
}

.section{
    font-size:22px;
    font-weight:bold;
    color:#333;
}

.resultbox{
    padding:20px;
    border-radius:10px;
    background-color:#e8f5e9;
    text-align:center;
    font-size:26px;
    font-weight:bold;
    color:#1b5e20;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">Resistor Color Code Virtual Lab</p>', unsafe_allow_html=True)

# Sidebar navigation
menu = st.sidebar.selectbox(
    "Select Section",
    ["Theory","Procedure","Experiment"]
)

# Color code data
digits = {
"Black":0,
"Brown":1,
"Red":2,
"Orange":3,
"Yellow":4,
"Green":5,
"Blue":6,
"Violet":7,
"Grey":8,
"White":9
}

multiplier = {
"Black":1,
"Brown":10,
"Red":100,
"Orange":1000,
"Yellow":10000,
"Green":100000,
"Blue":1000000,
"Gold":0.1,
"Silver":0.01
}

tolerance = {
"Brown":"±1%",
"Red":"±2%",
"Gold":"±5%",
"Silver":"±10%"
}

# Function to format resistance
def format_resistance(value):

    if value >= 1000000:
        return str(round(value/1000000,2)) + " MΩ"

    elif value >= 1000:
        return str(round(value/1000,2)) + " kΩ"

    else:
        return str(value) + " Ω"

# THEORY
if menu == "Theory":

    st.markdown('<p class="section">Objective</p>', unsafe_allow_html=True)

    st.write("""
To determine the resistance value of a resistor using the resistor color code method.
""")

    st.markdown('<p class="section">Theory</p>', unsafe_allow_html=True)

    st.write("""
Resistors are passive electronic components used to limit current in circuits.
The value of resistance is indicated using colored bands printed on the resistor body.

A typical **4-band resistor** contains:

• Band 1 – First digit  
• Band 2 – Second digit  
• Band 3 – Multiplier  
• Band 4 – Tolerance
""")

# PROCEDURE
elif menu == "Procedure":

    st.markdown('<p class="section">Procedure</p>', unsafe_allow_html=True)

    st.write("""
1. Observe the color bands on the resistor.
2. Identify the first band and note the color.
3. Select the corresponding color from the dropdown.
4. Repeat for all four bands.
5. Click **Calculate Resistance**.
6. The resistor value will be displayed automatically.
""")

# EXPERIMENT
elif menu == "Experiment":

    st.markdown('<p class="section">Resistor Experiment</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        band1 = st.selectbox("Band 1 (First Digit)", list(digits.keys()))
        band3 = st.selectbox("Multiplier", list(multiplier.keys()))

    with col2:
        band2 = st.selectbox("Band 2 (Second Digit)", list(digits.keys()))
        band4 = st.selectbox("Tolerance", list(tolerance.keys()))

    if st.button("Calculate Resistance"):

        d1 = digits[band1]
        d2 = digits[band2]
        mult = multiplier[band3]

        resistance = ((d1 * 10) + d2) * mult

        result = format_resistance(resistance)

        st.markdown(
            f'<div class="resultbox">Resistance = {result} {tolerance[band4]}</div>',
            unsafe_allow_html=True
        )

st.write("---")
st.write("Virtual Electronics Laboratory")
