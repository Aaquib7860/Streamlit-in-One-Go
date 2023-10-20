import streamlit as st
st.title('Title -> This is My App')                                             # title
st.header('header -> This is Header!')                                          # header
st.subheader('subheader -> This is subheader!')                                 # subheader
st.text('text -> This is text!')                                                # text


st.markdown('# Markdown size 1 -> Hi')                                          # markdown
st.markdown('## Markdown size 2 -> Hi')
st.markdown('### Markdown size 3 -> Hi')
st.markdown('#### Markdown size 4 -> Hi')
st.markdown('##### Markdown size 5 -> Hi')
st.markdown('Markdown -> Hi')

st.success('success')                                                           # success
st.info('Information')                                                          # Information
st.warning('Warning!')                                                          # warning
st.error('Error!')                                                              # error
st.exception(ZeroDivisionError('Division is not possible!'))                    # exception

st.subheader('Help')
st.help(ZeroDivisionError)                                                      # Help

st.subheader('Write')
st.write('range(1,10)')
st.write(range(1,10))
st.write(1+2+3)
st.write( )

st.subheader('Code')
st.code('x = 10\n'                                                              # code
         'for i in range(1,10):\n'
         '      print(i)')

st.subheader('Checkbox')
                                                            # checkbox
if(st.checkbox('Adult')):                                                       # checkbox with Validation
    st.write("you're a Adult")
elif(st.checkbox('Male')):
     st.write("you're a Male")

st.subheader('Radio')
radioButton = st.radio('Select : ',('Male','Female','Other'))                   # radio Button

if(radioButton == 'Male'):
    st.write("You're a Male")
elif(radioButton == 'Female'):
    st.write("You're a Female")
elif(radioButton == 'Other'):
    st.write("You're an Other Gender")

st.subheader('Select Box')                                                       # selectBox
selectBox = st.selectbox("Data Science : ", ['Machine Learing',
                                             'Data Analysis',
                                             'Web Scripting',
                                             'Image Proccessing',
                                             'Natural Language Proccesing',
                                             'Deep Learing'])
st.write("You've Selected : ", selectBox)

st.subheader('Multi-Select-Box')                                                # multiSelectBox
multiSelectBox = st.multiselect("Data Science : ", ['Machine Learing',
                                             'Data Analysis',
                                             'Web Scripting',
                                             'Image Proccessing',
                                             'Natural Language Proccesing',
                                             'Deep Learing'])
st.write("You've Selected ", len(multiSelectBox),"Courses")

st.subheader('Button')                                                          # Button
if(st.button('Click Me')):
    st.write("You've clicked Me!")

st.subheader('Slider')
vol = st.slider("Select the Volume", 0,100, step = 1)                           # slider
st.write("Volume is : ", vol)

st.subheader('Text Input')
username = st.text_input('Username : ')                                         # text_input
password = st.text_input('Password : ', type = 'password')

st.subheader('Number Input')
st.text_area('Write Somthing Intresting about yourself')                        # text_area

st.subheader('Number Input')
st.number_input('Select your Age', 18, 110)                                     # number_input

st.subheader('Date Input')                                                      # date_input
st.date_input('Date')

st.subheader('Time Input')                                                      # time_input
st.time_input('Time')
