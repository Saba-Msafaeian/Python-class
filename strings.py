# 0110 => 6
# python
# ASCII
# UTF-8

# print(chr(75))

st = 'pyTHon'
# print(st[0])
# print(len(st))

# st = st.capitalize()
# print(st)

# st = st.lower()
st = st.casefold()
# print(st)

# print(st.count('p'))

n = '12.3'
# print(n.isdigit())
if n.isnumeric():
    l = int(n)
    
txt = "we are coding in \npython programming language"
txt = """we are coding in, python programming language"""

txt = "#python #coding #ai"
x = txt.split("#", 2)
print(x)


txt = "computer"
txt = txt.replace('o', 'z')
print(txt)

# for i in range(len(txt)):
#     print(txt[i], end = ' ')

for i in txt:
    if i == 'o':
        print(i, end = '_')

# c o m p u t e r

