def solve(eq,var='x'):
    eq1 = eq.replace("=","-(")+")"
    c = eval(eq1,{var:1j})
    return -c.real/c.imag

## Test 1
print(solve("x - 2*x + 5*x - 46*(235-24) = x + 2"))
