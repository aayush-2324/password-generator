# 🔐 Smart Password Generator

A lightweight Python command-line tool that generates strong random passwords using letters, numbers, and symbols.

## ✨ Features

- Custom password length
- Uppercase and lowercase letters
- Numbers and punctuation/symbols
- Cryptographically secure randomness with Python's `secrets` module
- Input validation and clear error messages
- Simple command-line interface

## 🛠️ Tech Stack

- Python 3
- `secrets`
- `string`

## ▶️ Run Locally

```bash
python passsec.py
```

Enter a password length of **4 or more characters** when prompted.

## 📁 Project Structure

```text
password-generator/
├── passsec.py
├── README.md
├── LICENSE
└── .gitignore
```

## 🔒 Security Note

The generator uses Python's `secrets` module instead of `random`, making it more appropriate for generating passwords and other security-sensitive random values.

## 🚀 Future Improvements

- Password strength meter
- Options to include/exclude character categories
- GUI/web interface
- Copy-to-clipboard support
- Automated tests

## 👨‍💻 Author

**Aayush** — B.Tech Data Science & AI Student

[GitHub](https://github.com/aayush-2324) · [LinkedIn](https://www.linkedin.com/in/aayush-061a99390/)
