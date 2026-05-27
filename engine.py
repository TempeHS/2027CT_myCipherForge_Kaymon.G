"""
CipherForge — Encryption Engine
================================
Author: Kaymon G
Date: 2026
"""


def phase1_encrypt(text, key):
    """Phase 1: Substitution — shift every character by a fixed amount."""
    shift = key.get("shift", 5)
    result = ""
    for char in text:
        if 32 <= ord(char) <= 126:
            position = ord(char) - 32
            new_position = (position + shift) % 95
            result += chr(new_position + 32)
        else:
            result += char
    return result


def phase1_decrypt(text, key):
    """Phase 1: Reverse the substitution."""
    shift = key.get("shift", 5)
    result = ""
    for char in text:
        if 32 <= ord(char) <= 126:
            position = ord(char) - 32
            new_position = (position - shift) % 95
            result += chr(new_position + 32)
        else:
            result += char
    return result


def phase2_encrypt(text, key):
    """Phase 2: Transposition — reverse blocks of characters."""
    block_size = key.get("block_size", 4)
    result = ""
    for i in range(0, len(text), block_size):
        block = text[i : i + block_size]
        result += block[::-1]
    return result


def phase2_decrypt(text, key):
    """Phase 2: Reverse the transposition (self-inverse)."""
    block_size = key.get("block_size", 4)
    result = ""
    for i in range(0, len(text), block_size):
        block = text[i : i + block_size]
        result += block[::-1]
    return result


def phase3_encrypt(text, key):
    """Phase 3: Password-dependent variable shift."""
    password = key.get("password", "SECRET")
    result = ""
    for i, char in enumerate(text):
        if 32 <= ord(char) <= 126:
            password_char = password[i % len(password)]
            password_shift = ord(password_char) % 95
            position = ord(char) - 32
            new_position = (position + password_shift) % 95
            result += chr(new_position + 32)
        else:
            result += char
    return result


def phase3_decrypt(text, key):
    """Phase 3: Reverse the password-dependent shift."""
    password = key.get("password", "SECRET")
    result = ""
    for i, char in enumerate(text):
        if 32 <= ord(char) <= 126:
            password_char = password[i % len(password)]
            password_shift = ord(password_char) % 95
            position = ord(char) - 32
            new_position = (position - password_shift) % 95
            result += chr(new_position + 32)
        else:
            result += char
    return result


def phase4_encrypt(text, key):
    """Phase 4: Insert noise character every N positions."""
    interval = key.get("noise_interval", 3)
    noise = key.get("noise_char", "~")
    result = ""
    count = 0
    for char in text:
        result += char
        count += 1
        if count % interval == 0:
            result += noise
    return result


def phase4_decrypt(text, key):
    """Phase 4: Remove noise characters at known positions."""
    interval = key.get("noise_interval", 3)
    result = ""
    real_count = 0
    i = 0
    while i < len(text):
        result += text[i]
        real_count += 1
        i += 1
        if real_count % interval == 0 and i < len(text):
            i += 1
    return result


def phase5_encrypt(text, key):
    """Phase 5: Wild Card — reverse the whole text"""
    result = text[::-1]
    return result


def phase5_decrypt(text, key):
    """Phase 5: Reverse it back"""
    result = text[::-1]
    return result


def encrypt(plaintext, key):
    """Apply all 5 encryption phases in sequence."""
    result = plaintext
    result = phase1_encrypt(result, key)
    result = phase2_encrypt(result, key)
    result = phase3_encrypt(result, key)
    result = phase4_encrypt(result, key)
    result = phase5_encrypt(result, key)
    return result


def decrypt(ciphertext, key):
    """Reverse all 5 encryption phases in reverse order."""
    result = ciphertext
    result = phase5_decrypt(result, key)
    result = phase4_decrypt(result, key)
    result = phase3_decrypt(result, key)
    result = phase2_decrypt(result, key)
    result = phase1_decrypt(result, key)
    return result
