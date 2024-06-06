string=input()
lst_string=list(string)
set_string=set(string)
list_set_string=list(set_string)
list_set_string.sort()

count_char={
}
for character in list_set_string:
    char_value=lst_string.count(character)
    count_char[character]=char_value
print(count_char)