#!/usr/bin/env python3


def responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("yes","sure","ok"):
        return "Great! Let's start. First I need to know where you were born."
    
    if user_message in ("no","naw","no thanks"):
        return "That's alright, maybe another time."
    
    return "I'm Crypto Astro Bot and I love to do Astrology Readings! Would you like one?"

