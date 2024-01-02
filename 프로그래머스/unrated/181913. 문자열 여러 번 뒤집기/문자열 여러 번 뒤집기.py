def solution(my_string, queries):
    for x, y in queries:
        my_string = my_string[:x] + my_string[x:y+1][::-1] + my_string[y+1:]
    return my_string