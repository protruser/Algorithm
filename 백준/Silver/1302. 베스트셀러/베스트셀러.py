N = int(input())

book = {}
for i in range(N):
    n = input()
    if book.get(n) == None:
        book[n] = 1
    else:
        book[n] += 1
        
book_list = sorted(book.items(), key = lambda x : (-x[1],x[0]))
print(book_list[0][0])