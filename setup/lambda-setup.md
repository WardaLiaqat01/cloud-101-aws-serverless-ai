# Lambda Setup (Python)

In this step, we will create the backend of our application using **AWS Lambda**.

Lambda allows us to run code **without managing servers**.  
We only upload our code, and AWS takes care of scaling, availability, and infrastructure.

---

## What we are building

We will create **two Lambda functions**:

1. **Quote Function**
   - Returns a random motivational quote
   - Triggered by `GET /quote`

2. **Sentiment Function**
   - Analyzes the sentiment of text using an AWS AI service
   - Triggered by `GET /sentiment`

---

## Step 1: Open AWS Lambda

1. Log in to the AWS Console
2. Search for **Lambda**
3. Click **Create function**

---

## Step 2: Create the Quote Lambda Function

1. Select **Author from scratch**
2. Function name: `quote-function`
3. Runtime: **Python 3.10**
4. Architecture: **x86_64**
5. Attach existing lambda function with basic execution policy and "comprehend full access" policy
6. Click **Create function**

---

## Step 3: Add Quote Function Code

Replace the default code with the respective lambda codes.

