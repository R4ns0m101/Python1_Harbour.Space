lyric = """[Intro]
Desert you
Ooh-ooh-ooh-ooh
Hurt you

[Verse 1]
We're no strangers to love
You know the rules and so do I (Do I)
A full commitment's what I'm thinking of
You wouldn't get this from any other guy

[Pre-Chorus]
I just wanna tell you how I'm feeling
Gotta make you understand

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

[Verse 2]
We've known each other for so long
Your heart's been aching, but you're too shy to say it (To say it)
Inside, we both know what's been going on (Going on)
We know the game, and we're gonna play it

[Pre-Chorus]
And if you ask me how I'm feeling
Don't tell me you're too blind to see

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

[Bridge]
Ooh (Give you up)
Ooh-ooh (Give you up)
Ooh-ooh
Never gonna give, never gonna give (Give you up)
Ooh-ooh
Never gonna give, never gonna give (Give you up)
[Verse 3]
We've known each other for so long
Your heart's been aching, but you're too shy to say it (To say it)
Inside, we both know what's been going on (Going on)
We know the game, and we're gonna play it

[Pre-Chorus]
I just wanna tell you how I'm feeling
Gotta make you understand

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
"""

count_never_gonna = lyric.count("never gonna") + lyric.count("Never gonna")
print(count_never_gonna)

remove_section = lyric.replace("[Intro]","")
remove_section = remove_section.replace("[Verse 1]","")
remove_section = remove_section.replace("[Pre-Chorus]","")
remove_section = remove_section.replace("[Verse 2]","")
remove_section = remove_section.replace("[Chorus]","")
remove_section = remove_section.replace("[Bridge]","")
remove_section = remove_section.replace("[Verse 3]","")
print(remove_section)


print(remove_section.count("\n"))


count_alphabet = 0
for index in lyric:
    if index.isalpha():
        count_alphabet += 1

print(count_alphabet)