import itertools
import streamlit as st

st.title("Trovare combinazione fatture")

target=st.number_input('Numero da trovare')

col1, col2, col3 = st.columns(3)
with col1:
    ticker1 = st.number_input('Numero 1',min_value=0.01)
with col2:
    ticker2 = st.number_input('Numero 2',min_value=0.01)
with col3:
    ticker3 = st.number_input('Numero 3',min_value=0.01)
    
col4, col5, col6 = st.columns(3)
with col4:
    ticker4 = st.number_input('Numero 4',min_value=0.01)
with col5:
    ticker5 = st.number_input('Numero 5',min_value=0.01)
with col6:
    ticker6 = st.number_input('Numero 6',min_value=0.01)
    
col7, col8, col9 = st.columns(3)
with col4:
    ticker7 = st.number_input('Numero 7',min_value=0.01)
with col5:
    ticker8 = st.number_input('Numero 8',min_value=0.01)
with col6:
    ticker9 = st.number_input('Numero 9',min_value=0.01)
col10, col11, col12 = st.columns(3)
with col10:
    ticker10 = st.number_input('Numero 10',min_value=0.01)
with col11:
    ticker11 = st.number_input('Numero 11',min_value=0.01)
with col12:
    ticker12 = st.number_input('Numero 12',min_value=0.01)

numbers = [ticker1, ticker2, ticker3, ticker4, ticker5, ticker6, ticker7, ticker8, ticker9, ticker10, ticker11, ticker12]

# Generate all possible combinations of the numbers
combinations = list(itertools.combinations(numbers, 2)) + list(itertools.combinations(numbers, 3))+ list(itertools.combinations(numbers, 4))+ list(itertools.combinations(numbers, 5))+ list(itertools.combinations(numbers, 6))+ list(itertools.combinations(numbers, 7))+ list(itertools.combinations(numbers, 8))

# Check if any combination sums to the target
result = []
for combination in combinations:
    if sum(combination) == target:
        result.append(combination)

if len(result)>0:
    st.text(f'Il risultato è: {result}')
else:
    st.write("Nessuna combinazione per", target)

result = "\n".join(str(x) for x in result)
st.sidebar.text(f'Il risultato è:')
st.sidebar.text(result)
