# S3 Frontend Setup (Static Website Hosting)

In this step, we will host our frontend (Single HTML file for now) using **Amazon S3**.

Amazon S3 is an object storage service, but it can also be used to host **static websites** without any servers.

---

## What we are building

We will:
- Upload frontend file to S3
- Enable static website hosting
- Connect the frontend to API Gateway

At the end, users will access the app directly from a browser.

---

## Step 1: Create an S3 Bucket

1. Log in to the AWS Console
2. Search for **S3**
3. Click **Create bucket**
4. Bucket name: choose a **globally unique name**  
   Example: `cloud101-frontend-demo`
5. Region: use the **same region** as your API Gateway and Lambda
6. Uncheck **Block all public access**
7. Acknowledge the warning
8. Click **Create bucket**

---

## Step 2: Enable Static Website Hosting

1. Open your S3 bucket
2. Go to the **Properties** tab
3. Scroll to **Static website hosting**
4. Click **Edit**
5. Enable static website hosting
6. Index document: `index.html`
7. Click **Save changes**

---

## Step 3: Upload Frontend Files

Upload the index.html file to your bucket

You can upload by:
- Clicking **Upload**
- Dragging and dropping the file
- Clicking **Upload**

---
**Don't forget to add the bucket policy for the S3 bucket**

## Step 4: Connect Frontend to API Gateway

Don't forget to replace your API URL in the index.html js section

```js
const API_BASE_URL = "https://your-api-id.execute-api.region.amazonaws.com";


