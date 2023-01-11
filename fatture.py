import itertools
import streamlit as st

st.title("Trovare combinazione fatture")

col1, col2, col3 = st.columns(3)
with col1:
    ticker1 = st.number_input('Numero 1',min_value=0.01)
with col2:
    ticker2 = st.number_input('Numero 2',min_value=0.01)
with col1:
    ticker3 = st.number_input('Numero 3',min_value=0.01)
    
    
ticker2 = st.number_input('Numero 2',min_value=0.01)
ticker3 = st.number_input('Numero 3',min_value=0.01)
ticker4 = st.number_input('Numero 4',min_value=0.01)
ticker5 = st.number_input('Numero 5',min_value=0.01)
ticker6 = st.number_input('Numero 6',min_value=0.01)
ticker7 = st.number_input('Numero 7',min_value=0.01)
ticker8 = st.number_input('Numero 8',min_value=0.01)
ticker9 = st.number_input('Numero 9',min_value=0.01)
ticker10 = st.number_input('Numero 10',min_value=0.01)

target=st.number_input('Numero da trovare')

numbers = [ticker1, ticker2, ticker3, ticker4, ticker5, ticker6, ticker7, ticker8, ticker9, ticker10]
#target = 3493

# Generate all possible combinations of the numbers
combinations = list(itertools.combinations(numbers, 2)) + list(itertools.combinations(numbers, 3))+ list(itertools.combinations(numbers, 4))+ list(itertools.combinations(numbers, 5))+ list(itertools.combinations(numbers, 6))+ list(itertools.combinations(numbers, 7))+ list(itertools.combinations(numbers, 8))

# Check if any combination sums to the target
result = []
for combination in combinations:
    if sum(combination) == target:
        result.append(combination)

if len(result)>0:
    st.text(result)
else:
    st.write("Nessuna combinazione per", target)
