def check_pw(pw):
    points = 0
    feedback = []

    # check length
    if len(pw) >= 8:
        points += 4
    else:
        feedback.append("Password is too short!")

    # check uppercase letters (without regex)
    has_upper = False
    for ch in pw:
        if ch.isupper():
            has_upper = True
            break
    if has_upper:
        points += 2
    else:
        feedback.append("Try using some uppercase letters.")

    # check lowercase letters
    has_lower = False
    for ch in pw:
        if ch.islower():
            has_lower = True
            break
    if has_lower:
        points += 2
    else:
        feedback.append("Add some lowercase letters!")

    # check numbers
    has_num = False
    for ch in pw:
        if ch.isdigit():
            has_num = True
            break
    if has_num:
        points += 2
    else:
        feedback.append("Numbers make it stronger!")

    # check special chars (simple)
    specials = "!@#$%^&*()?"
    has_special = False
    for ch in pw:
        if ch in specials:
            has_special = True
            break
    if has_special:
        points += 3
    else:
        feedback.append("Special characters are cool, add some!")

    # check common words (just lowercase)
    common = ["password", "1234", "admin", "qwerty"]
    for c in common:
        if c in pw.lower():
            points -= 5
            feedback.append("No common words like 'password' please!")

    if points < 0:
        points = 0

    # strength
    if points >= 12:
        strength = "Strong"
    elif points >= 8:
        strength = "Okay"
    else:
        strength = "Weak"

    return points, strength, feedback


print("Hey! Let's check how strong your password is :)")
pw = input("Type your password here: ")

score, level, tips = check_pw(pw)

print("\nYour password score is:", score)
print("Strength level:", level)
if tips:
    print("Here's what you can do better:")
    for t in tips:
        print("-", t)
else:
    print("Wow! Your password is pretty strong!")
