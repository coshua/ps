from collections import deque
s = input()

st = []
def op(a, b, op):
    return a + b + op
def calc(lst):
    st = deque()
    for a in lst:
        if st and (st[-1] == '*' or st[-1] == '/'):
            sign = st.pop()
            st.append(st.pop() + a + sign)
        else:
            st.append(a)
    while len(st) > 1:
        a = st.popleft()
        sign = st.popleft()
        b = st.popleft()
        st.appendleft(a + b + sign)
    return st[0]

for i in s:
    if i == ')':
        temp = []
        while(st and st[-1] != '('):
            temp.append(st.pop())
        temp.reverse()
        s = calc(temp) # calculate the operations inside parenthesis
        st.pop() # remove matched '(' character
        st.append(s)
    else:
        st.append(i)
        
# Since there is no more parenthesis in our stack,
# we can just perform *, / then +, - operations without any other priorities.
print(calc(st))