def mutate_string(string, position, character):
    new_list=list(string)
    new_list[position]=character
    final_list="".join(new_list)
    return(final_list)
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)