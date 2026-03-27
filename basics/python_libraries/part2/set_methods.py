st = {1, 5, 3, 1}
print(st)

st.add(0)
print(st)

st.remove(5)
print(st)

if 15 in st:
    st.remove(15)
print(st)

st.discard(15)
print(st)

print(st.pop())