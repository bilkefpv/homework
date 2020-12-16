print("Primer: 100+3")


def result(val1, val2, operator):
    val1=int(val1)
    val2=int(val2)
    if operator=="*":
        return val1*val2
    if operator == "+":
        return val1 + val2
    if operator == "-":
        return val1 - val2
    if operator == "/" or operator==":":
        return val1 / val2


ops = "+-*/:"


def reformat_list(s):
    # ["1","2","+","4"] --> ["12","4"]
    i=0
    res = []
    val = ""
    while True:
        if i >= len(s):
            if val != "":
                res.append(int(val))
            break
        try:
            int(s[i])
            val += s[i]
        except ValueError:
            if val != "":
                res.append(int(val))
                val=""
        i+=1
    return res


def correct_format(s:list):
    s = list(s)
    for i,x in enumerate(s):
        if x == "" or x==" ":
            del s[i]
    num_of_operators =sum(s.count(f) for f in ops)
    num_of_parantheis = sum(s.count(f) for f in "()")
    return len(reformat_list(s)) == num_of_operators + 1 if num_of_operators == 1 and num_of_parantheis == 0 else False


while True:
    operator = None
    inp = input("Calculate: ")
    for inpt in inp:
        if inpt in ops:
            operator = inpt
    if operator is not None and correct_format(inp):
        val1, val2 = inp.split(operator)
        break
    else:
        print("Sorry.Try again...")

print(result(val1,val2,operator))
