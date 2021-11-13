a = map(str, input(
          "1. At least 1 letter between [a-z]\n"
          "2. At least 1 number between [0-9]\n"
          "3. At least 1 letter between [A-Z]\n"
          "4. At least 1 character from [$#@]\n"
          "5. Minimum length of transaction password: 6\n"
          "6. Maximum length of transaction password: 12\n"
          "\n"
          "Enter Password : ").split(","))
for i in a:
    if i.isupper() or i.islower() or i.isnumeric() or i.isdigit() or i.isalnum() or i.isalpha() or len(i) < 6 \
            or len(i) > 12:
        continue
    elif "@#$%^&*()_+!~{}[]|/?" in i:
        continue
    print(i)
    break
else:
    print("Invalid Password")
