def int_func(s):
    my_list = s.split()
    for word in my_list:
        letters = 0
        for i in range(len(list(word))):
            if 97 <= ord(list(word)[i]) <= 122:
                letters += 1
        print(word.title() if letters == len(word) else "", end=" ")


int_func("nice imagine super stream cool")
