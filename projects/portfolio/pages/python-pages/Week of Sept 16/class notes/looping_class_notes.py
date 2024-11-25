# please don't do this
# while True (she erased this line)

count = 10
while count >= 0:
    print(count)
    count = count - 1

# then she changed the bottom line to
    count--
# and talked about this for a while
# then wrote these lines

    # count--
    # https://chatgpt.com/share/e/66eb1c17-ccf0-800e-86d8-7fd4c28edb40

# the link doesn't work for me, just brought me to my chatgpt history

# then she wrote new lines, which look like this
count = 10
while count > 0:
    print(count)
    # count--
    # the link above
    count = count - 1

# in c++
# for (int i = 0; i >=0; i++):

for i in range(1, 10, 2):
    print(i)

# result
1
3
5
7
9

# for i in range(1, 13, 2):
#     print(i)

# result:

for i in range(1, 14):
    print(i)

for day in ("Sunday", "Monday", "Tuesday"):
    print(day)

# result:
# Sunday
# Monday
# Tuesday

weekdays = ("Sunday", "Monday", "Tuesday")

for day in (weekdays):
    print(day)

# result:
# Sunday
# Monday
# Tuesday

for number in [1, 2, 3, 4, 5]:
    if number == 3:
        break
    print(number)

# result:
# 1
# 2

for number in [1, 2, 3, 4, 5]:
    if number == 3:
        continue
    print(number)

# result:
# 1
# 2
# 3
# 4
# 5

for i in range(5):
    if i == 83:
        break
    print(i)
else:
    print("Loop completed without break")

# result:
# 1
# 2
# 3
# 4
# 5
# Loop completed without break

for i in range(5):
    if i == 83:
        break
    print(i)
else:
    print("Loop completed without break")
