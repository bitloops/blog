---
title: Developer productivity has a cancer and its called technical debt!
description: Developers want to be productive, solve problems and see their hard work come to fruition. Technical debt reduces productivity greatly when unmanaged!
author: Antonis
date: 03-December-2022
image: https://storage.googleapis.com/bitloops-github-assets/Blog%20Images/code.jpg
tags: ['Technical Debt', 'Developer Productivity', 'Clean Architecture', 'Clean Code']
---

We’ve all heard the term technical debt, but most don’t really understand it. The concept was created to explain all of the extra development work that is required when software is badly designed and implemented.

In summary, every time a developer builds redundant, poorly designed or useless code, that developer is creating technical debt. The most common types of technical debt are:

- Architecture debt is due to poorly designed software or architecture that negatively affects future maintenance
- Design and code debt is due to poorly designed code or design violations that lead to frequent maintenance activities in the future
- Test automation debt is due to ill-conceived test automation code that do not fulfil planned testing tasks correctly
- Documentation debt is due to insufficient or outdated technical documentation that impacts the knowledge of teams


But more importantly is understanding the consequence of technical debt. Both developers and non developers struggle to understand the major impact that technical debt can have on an application or business. If left unattended, technical debt will lead to:
- Higher total cost of ownership
- Longer time to market
- Reduced agility
- Negative customer experience
- Poor security
 
 
And do you know why the term debt is used? Well for 2 reasons:
1. **You can pay it back:** later I will explain that sometimes there are good reasons to create and accept technical debt, but you need to refactor, you need to dedicate the time to sort it out later (pay it back)
2. **There is interest and it compounds:** just like financial debt, the interest accumulates on top of your debt, so it just gets larger and larger and larger, and consequently gets harder and harder to pay back. In fact, the longer it takes to fix technical debt, the more entropy (and costly) new development becomes to a point where a company can go technically bankrupt


'''bash
Like financial debt, technical debt can lead to technical bankruptcy, and it actually happens more often than we realize. Companies accumulate so much technical debt that it becomes almost impossible to manage the code base, reaching a point of very high software development entropy. In fact, the quality of the code and software is so poor that usability issues start appearing, and the team spends all of its time fixing bugs, rather than working on new features. Often, once the product has reached this point, the business itself is unable to reorganize and develop a new product from scratch. 
'''

It's important to note though that developers are not creating technical debt on purpose. There are generally 2 mains reasons for technical debt:
1. Inexperience
2. Pressure to release features quickly

Everyone understands the tradeoff between speed and quality, but in software development speed today normally means slow tomorrow. Product Managers, CEOs and other executives demand faster and cheaper releases in the short term, not knowing that cutting corners is a sure way to create problems in the future if not fixed. 

Essentially, there are 2 paths a developer can choose:
A. Easy path that is faster but leads to messier code or design that gets the feature working, but creates unnecessary dependencies, coupling with other services and code that nobody really understands
B. Hard path that takes longer (in the short term) but leads to cleaner and well designed code, but ensures future developments can be easily added or modified 


## What causes technical debt?

There are several reasons why technical debt is created, and it's impossible to list all of them, but we can discuss the most common ones:

### 1. Poor software code quality

When a software engineer starts writing code, the options are almost limitless. There are probably hundreds of ways that particular code could be written to create the intended feature, and most engineers could identify tens of them on the spot. Of those hundreds of options, only a few are relevant and appropriate for that particular feature, only 2 or 3 are the most suitable for the application in question. The trouble is engineers don’t spend enough time thinking, planning and understanding the existing software, its layers and architectures to implement the best possible solution. Generally what happens is:
- Existing code may already be poorly designed, unclear and commonly referred to as spaghetti code
- There is no documentation that clearly explains the guidelines, constraints and expectations
- New developers are onboarded in an ad hoc way without clear instructions, training and support
- Developers try to implement something they read online, or introduce a piece of technology that sounds exciting but they don’t really understand 
- Poor understanding of the overall business, the domain language and the problem they’re trying to solve

### 2. Inexperienced IT leadership

Let's be honest, software development as an industry has gone through radical changes over the past 10 years. The evolution of cloud and containerization, increase in network speed and the growth in microservices that are reused across systems has “changed the game” in many aspects. 

IT leaders struggle to manage their teams and keep up with all these changes, and what tends to happen is the adoption of incorrect tools, platforms, principles or architectures. It is vital that all tech companies have an enterprise architecture that defines the tools, technologies and platforms that are used to build the application, as well as the coding principles, ubiquitous language and coding style. The lack or unavailability of these items will allow developers to build in their own way, their own style which will most likely not be the best for the company. 

### 3. Lack or no technical documentation
But who has time for this?

This is a widely known issue. Creating, managing and updating technical documentation is hard work, and the problem is if it’s only partly done, it could actually create more technical debt given the false sense of security.

There is no magic solution here. Technical documentation is required, but it needs to be as automated as possible. Alternatively, the actual code needs to be written in a higher level language that is intrinsically documentation: always up to date, always helpful.  

### 4. Becoming indispensable: job security 

We would all like to believe this is less common than what it is, but the truth is many engineers feel the power they have over their employer and their team when they’re the only one that understands how the system or a microservice works. By not sharing job-related information, or writing code in complex, convoluted ways, these engineers end by being viewed as indispensable for the business. 

### 5. Lack of testing 

Strong software engineers will all agree that proper testing is vital to build high quality, low technical debt software. However, only tech leaders with experience and a long term vision will dedicate resources to this task as it does increase short term time/cost of development. 

The truth is, teams that do not implement tests will increase short term development speed (and reduce costs), however, down the road, the lack of tests will greatly increase the time to build the next feature (increasing the cost of any new feature). Without these tests, the introduction of new features and services can impact existing services, and without proper testing, it becomes very difficult and resource intensive to conduct debugging. 

Test-driven development is widely regarded as a best practice in software development, but it does require upfront investment. 

### 6. Poor software development process/lifecycle

Teams that do not have clearly defined processes for software development will create poor quality software. It is imperative that tech leaders clearly define software development methods and processes that guide all team members to ensure adherence to the defined architecture, principles, language and structure design. In addition, it is crucial that all code be reviewed by peers to ensure it is high quality, that it is understood and that the best practices defined are followed. 

### 7. Unavoidable technical debt

Sometimes, technical debt creeps up behind you. It's just unavoidable. You do everything correctly, but due to changes in the business, or the progress of technology, you end up with a system that needs to be refactored. 
 
This happens constantly when there are scope changes, or new management vision, or even the acquisition of a complementary business / system. This should be simply viewed as part of the roles and responsibilities of the engineering team, and another challenge to solve! That includes being responsible for identifying the changes required, having the vision and flexibility to change existing systems. 
 
## Good technical debt - yes, it does exist

Technical debt is not always bad. Just like financial debt can be very useful, so can technical debt. There are many valid reasons why a team may accept some technical debt in their application. 

There are clearly situations where delivery is more important than the internal quality of the code or functionality. Sometimes we need to create a feature that satisfies a user’s need ASAP, or the time to market is a critical competitive advantage, but we must be critically aware of this, and if the feature is to remain live, refactoring needs to be planned, scheduled and executed.  This also applies to MVPs or hypotheses of features that the team believes will add value.

Whilst incurring good technical debt is definitely an acceptable and valuable solution, teams must ensure they return at some point to revise and improve the code based for that feature. The longer teams wait to refactor code, the more likely it will cause issues, or get buried in the “spaghetti code” that nobody understands. This is the interest that gets accumulated over time


Refactoring is the term used to describe the changes done to code that improve the overall design, cleanliness and structure, without impacting the actual functionality or output. Teams need to constantly plan and schedule refactoring for 2 mains reasons:
1. Re-write poorly written code 
2. Evolve existing code (even if it was initially written with high quality) as the problem is better understood or a complementary feature so requires
 
## Ok, I don’t want bad technical debt, now what?
 
Well, there is no single solution to avoiding bad technical debt. We (software engineers)  know what good code looks like, or what great, high-quality software looks like. The problem is learning and practicing the principles that allow us to design, implement and maintain these high-quality systems. 
 
There are several software development design patterns, best practices and methodologies that the industry as a whole agrees greatly improves the quality of software and improves flexibility and maintainability of systems such as SOLID, DDD, Clean Architecture / Clean Code, Layered / Hexagonal Architecture, YANGI, KISS, DRY, Dependency Injection, TDD to name a few. 
 
It is impossible to learn all these principles, and know how to implement them accurately in  a project, however, if you are keen on getting a good start on learning and understanding how to build great software, we suggest the following: 
 
### Don’t start coding!

1. Clearly understand your domain first (read up about DDD)
2. Create a ubiquitous language (meaning a common language) for your domain so everyone in your team knows exactly what each term means
3. Breakdown the domain into subdomains or smaller modules that are easier to understand, develop and maintain
4. Think about the Use Cases and Behaviors of your users, not the features

### Think about the architecture
1. Design a robust and flexible system architecture based on the domain
2. Ensure the Application is infrastructure agnostic

### Coding!
1. Ensure clear separation of concerns, meaning keep things that are independent from each other, independent from a code perspective
2. Ensure high cohesion, meaning that aspects that are closely related should be kept together from a code perspective
3. Clearly separate the domain logic and rules from the application “coordination” code
4. Learn more about test-driven development (TDD) as it will make your system more resilient and keep developer productivity high
5. Never (rarely) include domain logic in the infrastructure or application code


### Maintenance
1. Build and enforce code review processes, and manage access controls tightly
2. Streamline development, minimizing bugs in boilerplate code
3. Create and maintain technical documentation
4. Make time for refactoring work! Going a little slower today will ensure you can go much faster tomorrow!
 
If you’re really inspired to learn more, I strongly recommend reading any (or all) of these books. These are probably the bibles of good software development, and will undoubtedly make you a better software engineer! 
 
 
## Final thoughts
Software systems are becoming larger and more complex, which means technical debt will become increasingly a problem if not dealt with adequately. Moreover, if you want to release new features and products in a short lead time, you want to onboard new developers quickly and effectively and you want low developer churn (happy developers), then reconsidering how you manage code/software development is crucial!
