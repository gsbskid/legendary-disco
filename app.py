import streamlit as st 

st.image('logo.png')

st.title('Ask Supple AI Anything')

col_1 , col_2 , col_3 = st.columns(3)

poem = col_1.button('🖊️ Write a poem')
travel = col_1.button('✈ Travel Hacks')
note = col_1.button('🌟 Note taking tips')

cats = col_2.button('🐈 Why do cats purr?')
movie = col_2.button('📽️ Movie suggestions')
animals = col_2.button('🐶 Animals at a brunch')

novel = col_3.button('✍️ Imageine a novel')
advice = col_3.button('⚖️ Managment advice')

inp = st.empty()
text = inp.text_input('Enter your question ')

if poem : 
    inp.empty()
    text = st.text_input('Enter your question' , 'Write a poem')
if travel : 
    inp.empty()
    text = st.text_input('Enter your question' , 'Travel Hacks')
if note : 
    inp.empty()
    text = st.text_input('Enter your question' , 'Note taking tips')
if cats : 
    inp.empty()
    text = st.text_input('Enter your question' , 'Why do cats purr?')
if movie :
    inp.empty()
    text = st.text_input('Enter your question' , 'Movie suggestions')
if animals : 
    inp.empty()
    text = st.text_input('Enter your question' , 'Animals at a brunch')
if novel : 
    inp.empty()
    text = st.text_input('Enter your question' , 'Imageine a novel')
if advice : 
    inp.empty()
    text = st.text_input('Enter your question' , 'Managment advice')


if st.button('Ask') : st.write('Output will be displayed here')
