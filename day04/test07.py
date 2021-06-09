def func(**n):
    w1 = n['w'];
    h1 = n['h'];

    return (w1**2 + h1**2) * 0.5;

result = func(w = 90, h = 80);
print(result);