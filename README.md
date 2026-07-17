# 🎙️ Story Narrator - Text to Speech using AWS

A serverless **Text-to-Speech** web application built using **AWS Lambda, Amazon Polly, Amazon S3, DynamoDB, API Gateway, HTML, CSS, and JavaScript**.

Users can upload a `.txt` file or write a story directly in the browser. The application converts the text into natural speech using Amazon Polly, stores the generated MP3 file in Amazon S3, saves metadata in DynamoDB, and displays the narrated stories with an audio player.

---

# 🚀 Features

- Upload `.txt` files
- Write stories directly in the browser
- Convert text to speech using Amazon Polly
- Store generated audio in Amazon S3
- Save narration metadata in DynamoDB
- Display previously narrated stories
- Built using AWS Serverless Architecture
- Responsive Web Interface

---

# 🏗️ Architecture

```
                User
                  │
                  ▼
         HTML / CSS / JavaScript
                  │
                  ▼
            API Gateway
             /         \
            ▼           ▼
     TextToSpeech    GetAudioFiles
         Lambda          Lambda
            │               │
            ▼               ▼
       Amazon Polly     DynamoDB
            │               ▲
            ▼               │
          Amazon S3 ─────────
```

---

# ⚙️ AWS Services Used

| Service | Purpose |
|----------|----------|
| Amazon S3 | Store uploaded text files and generated audio |
| AWS Lambda | Process uploaded text and generate speech |
| Amazon Polly | Convert text into natural speech |
| DynamoDB | Store narration metadata |
| API Gateway | Expose REST APIs |
| CloudWatch | Logging and Monitoring |

---

# 📂 Project Structure

```
.
├── index.html
├── style.css
├── script.js
├── README.md
└── images/
```

---

# 🔄 Workflow

### Step 1

User uploads a text file or writes a story.

↓

### Step 2

The request is sent to API Gateway.

↓

### Step 3

API Gateway invokes the **TextToSpeech Lambda**.

↓

### Step 4

Lambda uploads the text file to Amazon S3.

↓

### Step 5

Lambda reads the uploaded text.

↓

### Step 6

Amazon Polly converts the text into speech.

↓

### Step 7

The generated MP3 is stored inside Amazon S3.

↓

### Step 8

Metadata is stored in Amazon DynamoDB.

↓

### Step 9

The website calls **GetAudioFiles Lambda**.

↓

### Step 10

Previously generated narrations are displayed with an audio player.

---

# 📸 Screenshots

## Home Page

![](images/Screenshot%202026-07-17%20104133.png)

---

## Amazon S3 Bucket

![](images/Screenshot%202026-07-17%20104143.png)

---

## Project Files

![](images/Screenshot%202026-07-17%20104159.png)

---

## AWS Lambda Configuration

![](images/Screenshot%202026-07-17%20104231.png)

---

## API Gateway Routes

![](images/Screenshot%202026-07-17%20104304.png)

---

## Narrated Stories

![](images/Screenshot%202026-07-17%20104317.png)

---

# 🛠️ Technologies Used

- HTML5
- CSS3
- JavaScript
- AWS Lambda
- Amazon Polly
- Amazon S3
- Amazon DynamoDB
- API Gateway
- CloudWatch

---

# API Endpoints

## Upload Story

```
POST /upload
```

Uploads a text file or story for narration.

---

## Get Narrated Stories

```
GET /audio
```

Returns all narrated stories stored in DynamoDB.

---

# Future Improvements

- Voice selection
- Multiple language support
- Delete narration
- Download generated MP3
- User authentication
- Search and filter narrations

---

# Author

**Darshan Desale**

AWS | Full Stack Developer | AI & ML Student

---
