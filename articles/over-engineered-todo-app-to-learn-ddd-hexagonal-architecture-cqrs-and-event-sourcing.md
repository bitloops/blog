---
title: Over-engineered ToDo App to learn DDD, Hexagonal Architecture, CQRS, and Event Sourcing
description: Designing, building and managing large and complex software does not have to be so hard. We believe it is possible to radically transform how software is developed by incorporating best-practices, design principles and patterns into the software development process. 
author: Vasilis
date: 05-04-2023
image: https://storage.googleapis.com/bitloops-github-assets/ddd-hexagonal-cqrs-es-eda-2.gif
tags: [Software Engineering', 'DDD', 'CQRS', 'Hexagonal Architecture', 'Software Patterns', 'clean architecture']
---

# Enterprise Edition ToDo App - Clean and SOLID tech stack codebase example

Are you tired of building software that's hard to understand, difficult to change, and prone to bugs?

We were too. Basically, everything ends up entangled, hard to understand and any new feature requires a lot of effort. You hear about Test Driven Development or Behavior Driven Development and they sound like great ideas but you try to implement them and it just feels like a struggle. It should not be.

That's why we we went to the drawing board, did a lot of research into software architectures like Hexagonal Architecture (or Ports and Adapters) and Event Driven Architecture, patterns such as CQRS and Event Sourcing, design techniques like Domain Driven Design (DDD) and its tactical patterns, as well as Behavior Driven Development (BDD) and CQRS.

After many months of learning, building and iterating, we decided to create the Ultimate ToDo app that follows these great software design patterns and principles. It is clearly over-engineered for a simple ToDo App, but we believe it provides a great example on which anyone can use to build great applications.  

<img src="https://storage.googleapis.com/bitloops-github-assets/ddd-hexagonal-cqrs-es-eda-2.gif" alt="todo app showcase"/>

You can find the entire codebase in our GitHub Repo: <a href="https://github.com/bitloops/ddd-hexagonal-cqrs-es-eda">ddd-hexagonal-cqrs-es-eda</a>

This implementation reference has been designed to help you build software that's organized, easy to understand, and easy to change. And the best part, it uses available open-source technologies.

Let me take you step-by-step (these are large leaps though - check out the repo for more details and feel free to join our Discord to ask any questions you like)

## Overarching Architecture

Good software architecture practices preach the separation of business logic code from infrastructure code (infrastructure means all external components like database, UI, servers, etc.). This ensures your code is organized, easy to understand, and easy to change.

So, we followed the hexagonal architecture - see image below.

// TODO IMAGE

Essentially, we have separated the domain and application code from all the other code, including the website (UI), the authentication, the database and the tracing and observability tools we use.

## Understanding the domain

Yes, I know, the domain of a ToDo App is rather limited if compared to a banking, insurance or ride-hailing application, however, the principles in how to understand the domain are rather the same: you need to get domain experts, product managers and developers speaking the same language and aligning on what is required.

Events are not only useful as a way for microservices to communicate with each other but rather they are very useful conceptual tools to describe what is happening in your domain.

Think of a CRUD application. You would say "update X" and then "Y" and then do "Z". With events you can separate concerns and make the system reactive to different events. This is very core to being able to cope with complexity as a system grows. You think one event at a time rather than do "X" and then "Y" and then "Z" and so on. You say when this "X" occurs do "Y" and emit a new event informing the system that “Y” happened and that is the end of it. This helps apply the Single Responsibility Principle (SRP), separation of concerns and loose coupling. All these concepts are very important to avoiding building a "Big Ball of Mud" and allows you to keep changing the system at a constant pace.

One of our favorite approaches to thinking of events and documenting the main functionality of a system is using Event Storming! You can read all about its history here.

// TOOD Add image

This process not only helps you understand the domain better, but it also helps you structure the domain into the best modules or bounded contexts (they’re not the same thing btw, but but if you do a good job and you are also lucky (in terms of org structure) then they could be pretty much the same).

In this case in particular, we went ahead and created 3 bounded contexts (and in this case there are exactly 1 module per bounded context), as well as processes within each:

1. IAM
  a. User Login process
  b. User Registration process
2. Todo
  a. Todo Process
3. Marketing
  a.Onboarding Process

Each of these bounded contexts are separate and should be treated as such.

Focusing on the Todo Process as it is the core domain here, we have identified 5 commands, namely:

* Add Todo
* Complete Todo
* Uncomplete Todo
* Modify Todo Title
* Delete Todo

Each of these commands is a separate use case and should be separate from each other, which we’ll dig into in the next section. Each command is followed by a command handler which interacts with your domain (either some root entity or a domain service) generating a list of domain events and then passes these changes (along with the domain events) to a repository in order to be persisted and the domain events dispatched to the message bus to become available to other parts of the system that need to be informed of the changes that took place in an eventually consistent manner.  

Now, I cannot stress enough how important this design step is. If you do this well, and you really think and tweak and go back and forth with your domain experts on this, you will get to a point where the actual coding is quite simple. One very important thing to keep in mind is that many times when deciding how you should approach a situation there won’t be a perfect answer and it is always a very good idea to think and evaluate alternative ways of doing things. Only then can you hope to reach a conclusion that will help you the most. The reason there is no perfect solution is that your choices, most of the time, will involve guessing how things will evolve in the future and since you probably cannot tell what the future holds with certainty you have to make your best guess and decide how to proceed based on those assumptions. In any ways, always try to come up with alternative ways to implement something and debate the pros and cons.

## It’s all in the code!

Now that we know the bounded contexts, modules, components, aggregates, entities, value objects, commands, queries, etc. it’s time to actually start writing some code.

To begin with, we have a clear project folder structure that follows the output of the event storming:

// TODO add image

As you can see, there is a folder for the:

* APIs
* bounded-context (concretions related to your bounded contexts)
* Config
* lib/bounded-contexts (everything related to domain or business logic code specific to your application but unaware of your infrastructure)

We have full details in the GitHub repository if you want more details

## Business / Domain Logic Code

This is where the high-value code lies. This is what differentiates your application from others, and this is why it's so important to keep this well organized and be able to change it easily, cheaply and quickly.

Focusing again on the Todo process (this is a folder within the lib/bounded-contexts -> todo), it should be apparent how this process is setup:

// TODO add image

As a quick overview, you have:

* application - this coordinates the activities and holds the use cases
* commands - as suggested, it's the code that triggers the command handlers
* contracts - specifies how the todo module communicates with other modules using integration events
* domain - contains all the elements (using DDD) like value objects, entities, aggregates, domain events, rules and read models
* ports - represents the interface (using hexagonal architecture principles) between the application and the infrastructure
* queries - as suggested, this triggers the query handlers (nothing to do with SQL queries!)
* tests - this includes all the behavior driven (BDD) tests that were identified (hopefully through the event storming)

So how can this implementation reference example help you?

Well, we believe this example could help developers irrespective of their experience levels, as there are many benefits to choose from.

More experienced TypeScript developers could use it as a template on which to build future projects that follow these design patterns and best practices. It serves as a quick reference guide, or a cheat sheet on the side - a cheat sheet you can easily tailor to your liking btw (or contribute back if you have other things to add). The structure is highly scalable and can handle large amounts of data, so it can be used for production apps.

Or, if you are a developer with intermediate experience, this implementation reference could help you more quickly (and easily) implement best practices like DDD and Hexagonal Architecture, helping you build software that's more organized and easier to understand. This should hopefully reduce significantly the amount of time you would need to build something similar on your own.

And finally, if you’re a novice, then this is a great way to get exposure to a modern tech stack that will help you understand software the way it is built in companies like Uber, Netflix or Amazon. Most of the time you won’t need their scalability nor will your needs match theirs but writing SOLID code is good for any size of project. They definitely did not use this specific implementation (or even TypeScript), but the overall patterns and principles would still apply to a big degree.

## Conclusion

Ultimately, our vision is that building applications that follow these design patterns and principles should be more easily accessible by most, and we are building tools to make this entire journey easier, cheaper and faster.

There is no need to build the scaffold and boilerplate code necessary to consistently build scalable, maintainable and resilient applications. We need to focus on business logic code, and this will be even more relevant with advances in AI-generated code.

We’re already received a lot of positive feedback and the GitHub stars are very rewarding as it's been a tough few months learning all this and putting it together. I hope it can help a lot of people!
