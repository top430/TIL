from value import Account

acc = None;

while True:
    cmd = input('input cmd(c,s,d,w,q)');
    if cmd == 'q':
        break;
    elif cmd == 'c':
        print('Create');
    elif cmd == 's':
        print('Select');
    elif cmd == 'd':
        print('Deposit');
    elif cmd == 'w':
        print('Withdraw');
print('Bye .. !!');