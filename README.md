# 🧠 terminAI

A simple, terminal-based AI chat assistant powered by OpenAI’s `gpt-3.5-turbo`.

---

## ✨ Features

* Live chat with AI from your terminal
* Uses OpenAI’s latest SDK (`v1.x`)
* Automatically loads your API key from `.env`
* Customizable temperature, max tokens, and model
* Runs fully inside Docker (no Python setup required)

---

## 🎞️ Requirements

* Docker
* OpenAI API key (get one at [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys))

---

## 🚀 Getting Started (Docker Only)

### 1. Clone the repo

```bash
git clone https://github.com/mahdiashrafee-oss/terminAI.git
cd terminAI
```

### 2. Create your `.env` file

```env
# .env
OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### 3. Build and run with Docker

```bash
docker build -t terminai .
docker run -it terminai
```

---

## 💠 Tech Stack

* Python 🐍 (inside Docker)
* OpenAI SDK (`v1.x`)
* dotenv (`python-dotenv`)
* Docker (runtime container)

---

## 🧠 Sample Interaction

```bash
You: write the word "SUN" in ASCII art
Bot: Here is the word "SUN" in ASCII art:

  SSS   U   U  N   N
 S   S  U   U  NN  N
 S      U   U  N N N
  SSS   U   U  N  NN
     S  U   U  N   N
 S   S  U   U  N   N
  SSS    UUU   N   N
You: exit
```

---

## 🤖 Author

* [@mahdiashrafee](https://github.com/mahdiashrafee-oss)

