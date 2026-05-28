# 🔐 CipherForge A 5-phase encryption algorithm built from scratch in Python.

**A custom 5-layer encryption algorithm** built as part of Year 9 Digital Technologies.

## About

This project implements a multi-layered encryption system that I designed from scratch. Each layer adds a different type of protection, similar to how real encryption algorithms like AES work.

## Algorithm Phases

| Phase | Name            | Status      |
| ----- | --------------- | ----------- |
| 1     | Substitution    | ✅ Finished |
| 2     | Transposition   | ✅ Finished |
| 3     | Key-Dependent   | ✅ Finished |
| 4     | Noise Injection | ✅ Finished |
| 5     | Wild Card       | ✅ Finished |

## License

MIT License — see [LICENSE](LICENSE) for details.

## 📋 Description

CipherForge is an educational encryption system that demonstrates how real-world encryption algorithms like AES work. It applies 5 layers of transformation to convert plaintext into unreadable ciphertext.

## ✨ Features

5-phase encryption pipelineWeb interface for easy encryption/decryption

Key-based security with trillions of combinations

Automated test suite for verification

# 🔧 The 5 Phases

## Phase 1: Substitution

Shifts all characters by a fixed amount

## Phase 2: Transposition

Reverses characters in blocks

## Phase 3: Key-Dependent

Uses password for variable shifting

## Phase 4: Noise Injection

Adds decoy characters

## Phase 5: Wild Card (Simple reversal)

Reverses the whole message as a whole and the reverts back to original form when decrypted🚀

# Getting Started

1. Run in Codespaces
2. Click Code → Codespaces → Create codespace
3. Wait for environment to load
4. Run: python app.py
5. Open the Ports tab and click the globe icon for port 5000
6. Run Tests by running the file python test_engine.py in the terminal

# 🔑 Key Format

## The encryption key is a dictionary with these fields:

key = {
"shift": 5, # Phase 1: shift amount (1-94)
"block_size": 4, # Phase 2: block size (2-20)
"password": "SECRET", # Phase 3: encryption password
"noise_interval": 3, # Phase 4: insert noise every N chars
"noise_char": "~" # Phase 4: noise character to insert
}

# 📊 Security Analysis

## Strengths

- Multi-layer encryption defeats simple attacks
- Password-based encryption provides large key space
- Noise injection defeats frequency analysis

## Weaknesses (Educational Context)

- Not mathematically proven like AES
- Smaller key space than production encryption
- Vulnerable to known-plaintext attacks with enough samples

# 📝 License MIT LICENSE

See LICENSE file👤

## Author, Kaymon Gurrala - Tempe High School - 2026

Built as part of Year 9 Digital Technologies
