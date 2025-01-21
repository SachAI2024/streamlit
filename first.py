import streamlit as st
import numpy as np
import time

#import seaborn as sns
import matplotlib.pyplot as plt


t1, t2, t3 = st.columns([1,3,1])
m1, m2 = st.columns(2)
b1, b2, b3 = st.columns([1,3,1])

with t2:
	st.markdown("`Title`")
	st.title("Sailesh is Exploring Streamlit")
	st.write("------------------------------------------------------")

with m1:
	st.markdown("`Heading`")
	st.header("Introduction")
	st.write("------------------------------------------------------")	
	st.markdown("`Sub Heading`")
	st.subheader("Installation")
	st.write("------------------------------------------------------")
	st.markdown("`Text`")
	st.text("Learn how to install Streamlit")
	st.write("------------------------------------------------------")
	st.text("use command Streamlit run <your py file>")
	st.write("------------------------------------------------------")

with m2:
	st.markdown("`Markdown`")
	st.markdown("Install Streamlit using `pip install streamlit ")
	st.write("------------------------------------------------------")
	st.markdown("`Write`")
	st.write("Once installed, run Streamlit using the command `streamlit hello`")
	st.write("------------------------------------------------------")
	st.markdown("`Latex`")
	st.latex(r"s \left ( t \right ) = ut + \dfrac{1}{2} at^2")
	st.write("------------------------------------------------------")

with b2:
	st.markdown("`Caption`")
	st.caption("Streamlit text options")

df = np.random.randn(5,5)

c1,c2,c3 = st.columns(3)

with c1:
	st.markdown("## Line Chart")
	st.line_chart(df)
with c2:
    st.markdown("## Area Chart")
    st.area_chart(df)
with c3:
	st.markdown("## Bar chart")
	st.bar_chart(df)
	


z1, z2 = st.columns(2)

with z1:
	st.markdown("## Image")	
	st.image("https://bit.ly/edus3ha")

with z2:
	st.markdown("## Video")
	st.video("https://bit.ly/canibs3")

st.markdown("## Audio")
st.audio("https://bit.ly/rainaws3")




with st.spinner("Counting on going..."):
    progress_bar = st.progress(0)
    for done in range(100):
        time.sleep(0.1)
        progress_bar.progress(done + 1)    
st.success("Counting complete.")
st.balloons()



st.markdown("### st.error()")
st.error("Syntax error")

st.markdown("### st.exception()")
st.exception(ZeroDivisionError("Divide by zero error"))

st.markdown("### st.warning()")
st.warning("This will be deprecated soon")

st.markdown("### st.info()")
st.info("App running optimally")



#Buttons and actions

import pandas as pd

st.button("Click button")

sample_data = {"Mammals": ["Cat", "Dog", "Bat", "Fox", "Pig"],
               "Birds": ["Parrot", "Eagle", "Duck", "Pegeon", "Vulture"]}
df = pd.DataFrame(sample_data)

st.dataframe(df)

if st.button("Click to show only mammals"):
    st.dataframe(df["Mammals"])




########

st.checkbox("Click to add a check mark")

sample_data = {"Mammals": ["Cat", "Dog", "Bat", "Fox", "Pig"],
               "Number": [5, 3, 7, 1, 6]}
df = pd.DataFrame(sample_data)

st.dataframe(df)

if st.checkbox("Click to show a graph of the data"):
    fig, ax = plt.subplots()
    ax = sns.barplot(x="Mammals", y="Number", data=df)
    st.pyplot(fig)


st.radio("Which of these is not a mammal?",
["Dog", "Cat", "Eagle", "Pig"])

st.selectbox("Which of these is a mammal?",
["Pigeon", "Dove", "Fox", "Vulture"])

st.select_slider("Which of these is not a bird?",
["Ostrich", "Flamingo", "Turkey", "Bat", "Pigeon"])


####################


st.markdown("## Single-Line Input")
text_input = st.text_input("Give an example of a mammal")
st.write(text_input)

st.markdown("## Multi-Line Input")
text_area = st.text_area("Give a list of 3 birds")
st.write(text_area)
####################

integer_number2 = st.number_input("Enter an integer",
                                 min_value=-10,
                                 max_value=10,
                                 value=0)
st.write(integer_number2, type(integer_number2))

float_number2 = st.number_input("Enter a float",
                               min_value=-1.0,
                               max_value=1.0,
                               value=0.0)
st.write(float_number2, type(float_number2))

##################file systems##############

file = st.file_uploader("Select a file to upload", type=["png", "jpg"])

if file is not None:
    st.image(file)


###################files download#################



import streamlit as st

with st.form("Order Form"):
    st.write("Order Details")
    fruit = st.select_slider("Select a fruit",
                             ["Banana", "Pawpaw", "Guava", "Mango"])

    quantity = st.number_input("Select the number of fruits", min_value=0)

    city = st.text_input("Type in your city")

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write("You have ordered {} {}(s) to be picked up at the {} branch"
                 .format(quantity, fruit, city))

st.write("These values, {}, {}, and {}, that were set inside the form are\
         accessible outside the form".format(quantity, fruit, city))



import streamlit as st

sample_data = [3.12, -4.31, 6.76, -9.88, 1.09]
col1, col2, col3 = st.columns([2.6,5,3.8])

col1.subheader("Line Chart")
col1.line_chart(sample_data)

col2.subheader("Area Chart")
col2.area_chart(sample_data)

with col3:
    st.subheader("Bar Chart")
    st.bar_chart(sample_data)



import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({"Mammal": ["Sea Lion", "Seal", "Walrus"], "Count": [3, 5, 2]})

st.dataframe(df)
with st.expander("Click to see a bar graph of the above data"):
    fig, ax = plt.subplots()
    ax.set_title("Mammal Count")
    ax = sns.barplot(x="Mammal", y="Count", data=df)
    st.pyplot(fig)
import streamlit as st
import pandas as pd

df1 = pd.DataFrame({"Cats": ["Lion", "Tiger", "Leopard"],
               "Raptors": ["Eagle", "Falcon", "Hawk"],
               "Snakes": ["Viper", "Anaconda", "Python"]})

df2 = pd.DataFrame({"Cats": ["Jaguar", "Panther"],
               "Raptors": ["Osprey", "Kite"],
               "Snakes": ["Cobra", "Boomslang"]})

st.dataframe(df1)
st.dataframe(df2)

df = st.dataframe(df1)
df.add_rows(df2)





import streamlit as st
import pandas as pd

df1 = pd.DataFrame({"Cats": [3, 2, 5],
               "Raptors": [6, 5, 1],
               "Snakes)": [4, 5, 7]})

df2 = pd.DataFrame({"Cats": [7, 9],
               "Raptors": [2, 6],
               "Snakes)": [3, 4]})

st.line_chart(df1)
st.line_chart(df2)

chart = st.line_chart(df1)
chart.add_rows(df2)








import streamlit as st
from time import time

x = 200
y = 3000000
    
def non_cached_function(x, y):
    return x ** y

start = time()
non_cached_function(x,y)
duration = round((time() - start),3)

st.write("Non-Cached Function took {} seconds to run".format(duration))

@st.cache
def cached_function(x, y):
    return x ** y

start = time()
cached_function(x,y)
duration = round((time() - start),3)

st.write("Cached Function took {} seconds to run".format(duration))









import streamlit as st
import time

with st.empty():
    for seconds in range(5):
        st.markdown (f"### ⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.markdown("### ✔️ 5 seconds over!")

placeholder = st.empty()
#Replace the placeholder with some text:
placeholder.markdown("### Hello")
time.sleep(2)
placeholder.info("This replaces Hello")



import streamlit as st

delta = None
step = 0.5

humidity = 75.0

raise_humidity = st.button("Raise humidity")
if raise_humidity:
    humidity += step
st.metric("The humidity is: ", humidity, delta)

if "temperature" not in st.session_state:
    st.session_state["temperature"] = 25.0

raise_temperature = st.button("Raise temperature")
if raise_temperature:
    st.session_state["temperature"] += step
    delta = step
lower_temperature = st.button("Lower temperature")
if lower_temperature:
    st.session_state["temperature"] -= step
    delta = -step

st.metric("The temperature is: ", st.session_state["temperature"], delta)


