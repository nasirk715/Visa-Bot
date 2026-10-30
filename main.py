# Visa Bot - nasirk715
# Simple auto-reply bot for visa business

def get_reply(message):
    msg = message.lower()
    if "price" in msg or "rate" in msg or "kitna" in msg:
        return "Dubai Visa: 8.30 Lac (2 Lac advance, baki visa per). 1 Year Visa. \nSaudi, Turkey, Schengen available."
    elif "document" in msg or "docs" in msg or "kagaz" in msg:
        return "Documents: Passport, CNIC Pic, White Background Photo. Bas ye 3 chezen bhej dein."
    elif "time" in msg or "kitne din" in msg:
        return "InshaAllah 3-5 working days me visa ajayega."
    elif "payment" in msg or "advance" in msg:
        return "2 Lac Advance. Baqi visa lagne ke baad. JazzCash/Easypaisa available."
    else:
        return "Assalamu Alaikum! Visa ke liye Price, Documents, Time likh kar bhejen. Foran jawab milega."

# Test
print(get_reply("price kya hai?"))
