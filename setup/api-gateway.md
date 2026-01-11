# API Gateway Setup

In this step, we will expose our backend Lambda functions using **Amazon API Gateway**.

API Gateway acts as the **front door** for our application.  
The frontend (browser) talks to API Gateway, and API Gateway forwards requests to the correct Lambda function.

---

## What we are building

We will create one HTTP API with two routes:

- `GET /quote` → returns a random quote
- `POST /sentiment` → analyzes text sentiment using an AI service

Each route will be connected to a **different Lambda function**.

---

## Step 1: Open API Gateway

1. Log in to the AWS Console
2. Search for **API Gateway**
3. Click **Create API**

---

## Step 2: Create an HTTP API

1. Select **HTTP API**
2. Click **Build**
3. Choose **Add integrations later**
4. Click **Next**
5. Give your API a name (e.g. `cloud101-api`)
6. Click **Next**
7. Skip stages for now and click **Create**

---

## Step 3: Create Routes

1. Open your newly created API
2. Go to the **Routes** tab
3. Click **Create**

Create the following routes:

### Route 1: Quote API
- Method: `GET`
- Resource path: `/quote`

### Route 2: Sentiment API
- Method: `GET`
- Resource path: `/sentiment`

Click **Create** after adding each route.

---

## Step 4: Integrate Routes with Lambda

Now we connect each route to the correct Lambda function.

---

### Integrate `/quote` route

1. Click on the `/quote` route
2. Click **Attach integration**
3. Integration type: **Lambda**
4. Lambda function: `quote-function`
5. Click **Attach integration**

---

### Integrate `/sentiment` route

1. Click on the `/sentiment` route
2. Click **Attach integration**
3. Integration type: **Lambda**
4. Lambda function: `sentiment-function`
5. Click **Attach integration**

✅ Make sure **each route points to its own Lambda function**.

---


## Step 5: Deploy the API

1. Go to the **Deploy** tab
2. Click **Deploy**
3. Copy the **Invoke URL**

You will use this URL in the frontend.

---

## Step 7: Test the API

Open your browser and visit:[API Invoke URL/[route]]

