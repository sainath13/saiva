Atlassian | P40 | India [Offer]

![](https://leetcode.com/_next/static/images/anonymous_avatar-0e699fe8591585574e6a9e6e905f91af.svg)
[Atlassian](https://leetcode.com/discuss/topic/atlassian/)[Interview](https://leetcode.com/discuss/topic/interview/)
### **Background**

- **Education:** Tier-3
- **Experience:** 5 Years (3 Years in FAANG)
- **Designation:** SE-2
- **Current Company:** Startup
---
### **Interview Experience**

I applied to multiple SDE2 openings on **the** portal. I got **a** call from a recruiter. I'll consider the recruiter contact day as Day 0.

#### Day 1 : Karat Interview (1 hr)

##### System design Questions
1.) We are working on a clone of Facebook. We want to add a numeric count to every post showing how many friends the post's author has at the time of viewing the post. The database schema looks like this:  
**USER**
- `user_id` (primary key)
- `name`
- `created_date`
**USER RELATIONSHIP**
- `friendship_id` (primary key, unique to each relationship)
- `user_id` (indexed)
- `user2_id` (indexed)
- `start_date`
Focusing on the database, how would you implement the friend-count feature? Note that we will soon be more popular than Facebook, so the solution needs to scale.

2.) We are working on a clone of Google Docs. The software has the following features and limitations:

- Multiple users may work on a single document at the same time.
- A document must be handled by a single server, no matter how many users **there are**.
- We have a fixed number of servers which will be sufficient to handle our **expected load** properly.

Our load balancer uses a round-robin system to permanently assign documents to each server, so **that** each will have an equal number of documents. Do you have any concerns about this load **balancing** system? In those cases, how would you fix the **scalability issue**?

3.) Which consistency model is more appropriate for each of these applications: **strong** or **eventual** consistency? Why?

- An API call that needs to respond within 20 milliseconds, used to retrieve **video stream metadata**. The metadata includes things like the author name, rating, and **view count**.
- A web analytics platform recording every single click on a popular web page.
- A banking system that makes deposits and payments to checking accounts.

4.) **Another scenario was that** there was a bug on an application, and you ended up having a lot of failed requests. You have a database that stores all IDs, and you also have large log files from about 500 different production servers that log the IDs of the successful requests. How would you come up with a solution to find the IDs that were missing?

##### Coding Question

The question was similar to [68. Text Justification](https://leetcode.com/problems/text-justification/description/) and had one **follow-up**. I was able to fully solve the question and **gave my** approach for the **follow-up**.

---

#### Day 6 : Data Structures Interview (1 hr)

You have `N` services **in** a network. You are given which servers are connected and the connection latency. For example `[1, 2, 200]` means service `1` calls service `2` and it has a latency of 200ms. You are given `Q` queries where you have to output the minimum latency from Service `X` to Service `Y`.

**The** interviewer wanted to discuss why classic DFS and BFS should not be the solution, how **Dijkstra's** algorithm **would** work, **what the** other ways **are** to solve this, and **the** time complexity.

In the end, I provided the solution using **Dijkstra's** algorithm.

**Rating:** Hire (Medium confidence)

---

#### Day 7 : Code Design Interview (1 hr)

**Customer Satisfaction**

a) Imagine we have a customer support ticketing system. The system allows customers to rate the support agent out of 5. To start with, write a function which accepts a rating, and another which will show me all of the agents and the average rating **each** one has received, ordered from highest to lowest.  
c) Now I want to be able to see who the best agents are each month. Change the implementation so I can get that information.

I **followed the** `Test-Driven Development (TDD)` approach as mentioned by the recruiter in the preparation guide. Atlassian recruiters are really helpful.

**Rating:** Hire (Medium confidence)

---

#### Day 13 : System Design Interview (1 hr)

**Question: Tagging Management Service**

Atlassian has a number of different products, each containing different types of content. As an example, let’s look at three of our products:

- Jira – Issues
- Confluence – Pages
- Bitbucket – Pull requests

We want to build a system that allows users to tag content from different products, and then to view content by tags. A goal of this system is that it should be built **in** a product-agnostic way so that we could add new products in the future without a large amount of work. There are three key experiences that we want to build here:

- As a user, I can add, remove, and update tags on content.
- As a user, I can click on a tag and see all content that has been associated with that tag.
- As a user, I can see a dashboard of popular tags.

**The** recruiter focused on API Specification, DB Schema, DB Choice (SQL/NoSQL), Communication protocols, SQS vs **RabbitMQ** vs Kafka, **and** Rate **limiting**.

**Rating:** Hire (Low confidence)

The recruiter mentioned the reason for the "low confidence hire" was that the **interviewer** felt the design was a little rushed.

---

#### Day 16 : Managerial Interview (1 hr)

**This involved** standard managerial-type **questions** based on my previous work experiences.

**Rating:** Hire (High confidence)

---

#### Day 20 : Values Interview (45 mins)

**The questions were similar to those mentioned** in the following LeetCode article:  
[[Disclosed] Atlassian Full Loop Question [SSE & SDE 2]](https://leetcode.com/discuss/post/6974858/disclosed-atlassian-full-loop-question-b-ulje/)

**Rating:** Hire (High confidence)

---

##### Day 31 : **Got** confirmation about the HC Result

##### Day 35 : **The** recruiter scheduled a team matching meeting

##### Day 38 : **I had the** team matching call

##### Day 41 : **I received the offer**

---

##### Compensation:

[Atlassian | P40 | India [Accepted]](https://leetcode.com/discuss/post/7069410/atlassian-p40-india-accepted-by-anonymou-p3qh/)

---

##### Remarks

Here are my thoughts on my recent 6-month job search:

- **The Market:** It's tough out there. Interviews are hard, and there is little room for mistakes.
- **My Journey:** It was a long road. I was rejected by many companies like Apple, Dream11, Microsoft (2 times), Arcesium, Myntra, Tekion, Google, Salesforce (Ghosted), and Uber (Ghosted) before I finally got offers from Microsoft and Atlassian.
- **What Helped:** My previous experience at a FAANG company made my resume stand out and helped me get more calls for interviews.
- **My Advice:** Just keep going. Don't let the rejections discourage you. Keep interviewing, and you will find the right job.


### **Background**

- **Education:** Tier-3
- **Experience:** 5 Years (3 Years in FAANG)
- **Designation:** SE-2
- **Current TC:** ₹35L (Fixed)
- **Current Company:** Startup

### **Atlassian Offer (P40)**

- **Base Salary:** ₹47,00,000
- **Retirals (PF):** ₹2,26,000
- **Performance Bonus:** ₹7,00,000 (Target: 15% of base)
- **Stock:** $100,000 USD vested over 4 years (≈ ₹21,89,000 per year)
- **Signing Bonus:** ₹6,50,000
---
### **Total Compensation Breakdown**
- **First Year Total Compensation (with signing bonus):**  
    ₹47L + ₹2.26L + ₹7L + ₹21.89L + ₹6.5L = **₹84.65 Lakhs**
- **Annual Compensation (from 2nd year onwards):**  
    ₹47L + ₹2.26L + ₹7L + ₹21.89L = **₹78.15 Lakhs**
**Note:** Negotiated using a competing offer from Microsoft.
#### Interview Experience