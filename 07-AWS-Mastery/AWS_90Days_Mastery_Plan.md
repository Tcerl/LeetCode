# 📅 AWS Cloud Mastery: 90-Day Intensive Plan
**Target:** Senior Fullstack Developer (Python/Vue)
**Goal:** AWS Certified Solutions Architect Associate (SAA-C03) & Cloud Architect Proficiency.

---

## 🏗️ Month 1: The Building Blocks (Compute & Identity)
*Goal: Understand how Cloud infrastructure works and how to secure it.*

### Week 1: AWS Basics & IAM
- **Theory:** IAM Users, Groups, Roles, Policies, MFA, Organization, Well-Architected Framework.
- **Hands-on:** Setup a Free Tier account, create a non-root User, and enforce MFA.
- **Goal:** Secure your account before doing anything else.

### Week 2: Compute (EC2 & ALB)
- **Theory:** Instances types, AMIs, Key Pairs, Security Groups, Elastic IPs.
- **Hands-on (Python/Vue):**
    - Spin up an EC2 (t3.micro).
    - Deploy a simple **Vue.js** (built) app on Nginx inside EC2.
    - Set up an Application Load Balancer (ALB) to handle traffic.

### Week 3: High Availability (Auto Scaling & EBS)
- **Theory:** Launch Templates, Target Groups, Scaling Policies, EBS Snapshots.
- **Hands-on:** Simulate high CPU load on EC2 and watch AWS automatically start a new instance.
- **Goal:** "Zero Downtime" infrastructure.

### Week 4: Networking (VPC) - CRITICAL
- **Theory:** Subnets (Public vs Private), Route Tables, Internet Gateways, NAT Gateways.
- **Hands-on:** 
    - Create a VPC from scratch.
    - Place your EC2 in a Private Subnet.
    - Use a NAT Gateway to allow it to update Python libraries from the internet.

---

## 💾 Month 2: Storage, Data & Monitoring
*Goal: Managing data at scale and making systems resilient.*

### Week 5: Storage (S3 & CloudFront)
- **Theory:** Buckets, Object Versioning, Life Cycle Policies, IAM Policies vs Bucket Policies.
- **Hands-on (Vue):** 
    - Host your Vue.js Dist folder on S3.
    - Add CloudFront (CDN) to serve it globally with HTTPS.

### Week 6: Databases (RDS & ElastiCache)
- **Theory:** RDS (Multi-AZ), Read Replicas, PostgreSQL on AWS.
- **Hands-on (Python):** 
    - Create an RDS (Postgres) instance.
    - Connect your Python script to RDS from an EC2 instance.
    - Use Redis (ElastiCache) for caching slow queries.

### Week 7: NoSQL (DynamoDB)
- **Theory:** Primary Keys (Partition/Sort), GSI/LSI, Throughput.
- **Hands-on (Python):** 
    - Use the `boto3` library in Python to perform CRUD operations on DynamoDB.
    - Build a "View Counter" for your Vue app using DynamoDB.

### Week 8: Monitoring & Auditing
- **Theory:** CloudWatch (Metrics, Alarms, Logs), CloudTrail (Audit), Config.
- **Hands-on:** 
    - Setup a CloudWatch Alarm to email you (SNS) if your EC2 stays above 10% CPU for 5 minutes.
    - Setup Log Groups for your Python application logs.

---

## ⚡ Month 3: Serverless, DevOps & Certification
*Goal: Moving to modern, maintenance-free architectures.*

### Week 9: Serverless (Lambda & API Gateway)
- **Theory:** Trigger vs Action, Layers, Cold Start, API Gateway Stages.
- **Hands-on (Python):** 
    - Replace your EC2-Backend with an AWS Lambda function.
    - Connect it to the internet via API Gateway.
    - Secure the API with an API Key.

### Week 10: App Integration (SQS & SNS)
- **Theory:** Decoupling, Async processing, Pub/Sub pattern.
- **Hands-on:** 
    - Use Python to send a message to SQS (Queue).
    - Trigger a Lambda function to process that message asynchronously.

### Week 11: Infrastructure as Code (AWS CDK / Terraform)
- **Theory:** IaC benefits, Declarative vs Imperative.
- **Hands-on (Python):**
    - Use **AWS CDK (Python)** to write code that generates your entire VPC + S3 + Lambda setup.
    - Command: `cdk deploy`.

### Week 12: Review & Exam Strategy
- **Activities:**
    - Take the Official Practice Exam.
    - Memorize the "Cheat Sheet" for Storage and Network.
    - **Final Project:** Build and deploy a Go-Live ready Fullstack app (Vue + Lambda + DynamoDB) using CI/CD.

---

## 📚 Recommended Courses (2026)
1. **Ultimate AWS Certified Solutions Architect Associate (Stephane Maarek)** - Udemy.
2. **Adrian Cantrill's SAA-C03 Course** - (Deep dives).
3. **Tutorials Dojo (Jon Bonso)** - Best Practice Exams.
4. **AWS Skill Builder (Free)** - Official Cloud Quest game.

---
*Created for: Senior Fullstack Developer (Python/Vue)*
*Keep coding, keep building!*
