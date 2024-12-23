# Write the program "99 Bottles of Beer on the Wall" using a while loop. Be mindful to change the word 'bottles' to 'bottle' when you are down to the last one. You need to do the full 99 bottles

count = 99
bottle = "bottles"

while count > 0:
    print(f"{count} {bottle} of beer on the wall,")
    print(f"{count} {bottle} of beer!")
    print("Take one down, pass it around,")
    count -= 1  # subtract 1 from count
    if count > 1:
        print(f"{count} {bottle} of beer on the wall!\n")
    elif count == 1:
        bottle = "bottle"
        print(f"{count} {bottle} of beer on the wall!\n")
    else:
        print(f"No more bottles of beer on the wall!\n")
