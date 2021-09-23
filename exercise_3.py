# Logical Operators (Exercise)

is_magician = True
is_expert = False

# Check if magician and expert
if is_magician and is_expert:
    print("You are a master magician")

# Check if magician but not expert
elif is_magician and not is_expert:
    print("At least you are getting there...")

# Check if you are not a magician
elif not is_magician:
    print("You need magic powers")