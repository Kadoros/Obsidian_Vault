@unit U1 | Intro to SW Engineering and OOP | L02 Intro to OOP.pdf + Handout 1
@intro Software crisis → software engineering → factors of good software → programming paradigms → OOP concepts. Question 1's blanks (software crisis, complexity, maintenance, global/dependent) come from here almost every year. Memorizing the exact English words is what earns the points.

@lesson L1-1 | Software Crisis · Life Cycle · Software Engineering | L02 p.3–6

## Software Crisis {#crisis}

- Rapid increases in computer power and in the **complexity** of the problems (SW); software technology cannot follow the complexity
- The difficulty of writing correct, understandable, and verifiable computer programs
- Symptoms: unmanageable, difficult to maintain, **over-budget**, **over-time (late)**, poor quality, software often did not meet requirements
- **Cause: complexity**

> Exam point: blanks in 2025·2023·2022. "(software crisis) arose because as computer hardware power grew rapidly, (complexity) of the software systems increased even faster".

## Software Life Cycle {#lifecycle}

1. **Requirement Analysis**: problem specification
2. **Design**: program structure, module specification
3. **Implementation**
4. **Test**: unit test, integration test
5. **Maintenance**

**Fred Brooks**: over 90% of the **costs** of a typical system arise in the **maintenance phase**, and any successful piece of software will inevitably be maintained.

> Exam point: blanks in 2024·2017 "over 90% of (the costs) of a typical system arise in (the maintenance) phase, and any successful piece of software will inevitably be (maintained)".

## Definition and Goals of Software Engineering {#se-def}

**Definition**
- [IEEE] The application of a **systematic, disciplined, quantifiable** approach to the development, operation, and maintenance of software, that is, the application of engineering to software
- [Fritz Bauer] The establishment and use of sound engineering principles in order to **economically** obtain software that is reliable and works efficiently

**Goals**
- Produce **correct, efficient, and reliable** software
- **Minimize the cost** of software development and maintenance

**Four goals of SE ("Goals of SE" slide)**
| Goal | Meaning |
|---|---|
| **Maintainability** | the ability to easily make changes, enhancements, or improvements |
| **Dependability** | the ability to **rely on** the software to function properly when needed |
| **Efficiency** | the ability for software to use computing resources effectively (mainly space and time) |
| **Usability** | the ability for the end user to easily and effectively put the software to proper use |

> Exam point: blanks in 2022·2019 "(software engineering) … to (economically) obtain software that is reliable and works efficiently", 2025 "minimize (the cost)", 2017 "(Dependability) means the ability to rely on the software to function properly when needed".

@lesson L1-2 | Factors of Good Software · Software Properties | L02 p.2, 7 + Handout 1

## Factors of Good Software (Handout 1) {#quality}

| Factor | Meaning |
|---|---|
| **correct** (correctness) | satisfies the user requirements/specification without error |
| **efficient** (efficiency) | optimizes resource usage (space/time, HW utilization) to deliver fast response times |
| **easy to maintain** (maintainability) | easy to read (readability), easy to modify (modifiability), easy to extend (extensibility, scalability), easy to reuse (reusability), easy to debug/test (testability), modular (modularity), easy to port (portability) |
| **stable, reliable, robust** | stability, reliability, robustness |
| **easy to use** (usability) | easy to use, easy to run |
| **secure** (security), integrity | protects data against unauthorized access, corruption, or malicious exploits |
| interoperability | easily exchanges data with other systems via standardized protocols and interfaces |
| concise, complete, consistent, well-documented, well structured | conciseness, implements all required functionality, consistency (e.g. naming conventions), documentation, good structure |

> Exam point: you must be able to write the parts of maintainability in English: "easy to read, modify, extend, reuse, debug/test, port" (2019·2016 "A program with high maintainability is easy to (read), easy to (modify), easy to (extend)…").

## Stability · Reliability · Robustness {#robust}

- **stability**: keeps functioning correctly as conditions change and over time (if it works sometimes and fails other times, it is unstable)
- **reliability**: the ability to **consistently perform its required functions without failure** under specified conditions for a specified period
- **robustness**: keeps functioning under exceptional situations (invalid input, disasters)
- The three words mean almost the same thing; only the emphasis differs slightly

> Trap: 2025 blank "(reliability) means the ability of the software to consistently perform its required functions without failure under specified conditions for a specified period" vs 2017 "(Dependability) means the ability to rely on the software to function properly when needed". Tell them apart by the definition sentence.

## Software Properties {#sw-props}

- **Modularity** – divide and conquer
- **Encapsulation** – hide the implementation
- **Localization** – collect similar things together
- **Abstraction** – simplifying complex reality
- **Uniformity** – make everything look similar
- **Completeness** – do everything required
- **Confirmability** – be able to prove that the software works properly

@lesson L1-3 | Programming Paradigms | L02 p.8–15

## Unstructured Programming {#unstructured}

- Consists of **only one main program**: a sequence of commands or statements
- **Only global data**
- Uses the **goto statement**
- Disadvantage: if the same statement sequence is repeated, it must be written out again every time
- **Spaghetti code**: code with a complex and tangled structure, with goto's jumping all over the place → almost impossible to understand, hard to follow the flow, difficult to modify

> Exam point: 2024 blank "(Unstructured programming) makes extensive use of GOTO statements… a program contains only a single code block".

## Procedural and Modular Programming {#procedural}

**Procedural programming** — the abuses of spaghetti code led to structured programming languages
- Program = **a sequence of procedure calls**; procedure = a grouped sequence of statements
- More structured (reduces repetition) and more error-free
- **Structured Programming** ≒ **top-down approach** ≒ **divide and conquer** ≒ **functional decomposition**

**Modular programming**
- SW is composed of separate parts (**modules**); procedures of a common functionality are grouped together into modules
- The program uses modules through an **interface**: **interface is visible, implementation is hidden**
- Improves maintainability

> Exam point: 2022 blank "structured programming ≒ (top-down approach) ≒ (divide and conquer) ≒ functional decomposition".

## Don't Use Global Variables {#global-vars}

- **Using global variables is unsafe**
  - Sharing data (global variables) violates the principle of modular programming
  - Every module can access every global variable without restriction → no module can be developed or understood independently
  - It makes **all modules dependent on one another**
- Solution: **Modularized Data** — **localize** data inside the modules → modules become more independent of one another → safe

> Exam point: almost every year (2024·2022·2019·2017·2016)! "Using (global) variables is often unsafe because this makes all modules (dependent) on one another."

## Problems of Procedural/Modular Programming and OOP {#oop-why}

**Problems of procedural/modular programming**
- **Decoupled** (separation of) data and operations
- Doesn't work well in large systems: difficult to debug, extend, and maintain; code reuse limited
- Explicit creation and destruction

**OOP**
- Program = **a set of interacting objects**; each object keeps its own state
- **Combines data and operations into an object**
- Structured: "data + function = program"; OOP: "data + function = object, **object + object = program**"
- OOP does not view the problem domain as a flow of processing, but as **objects that communicate with each other through message passing**
- An object works as a **component** of software, and **the interface of an object should be well defined**

**Why OO?** Good for developing large software, maintainability, **reuse software, not rewrite** → increases productivity, quality, understandability, scalability and lifetime. SW **reliability also increases** because reusable modules are already well tested.

> Exam point: 2024 blank "(Object-oriented programming) is a programming paradigm based on the concept of (objects), which can contain data and code".

@lesson L1-4 | OOP Concepts: ADT · Object · Encapsulation · Inheritance · Polymorphism | L02 p.24–33

## Abstract Data Type (ADT) {#adt}

- **ADT**: a set of data variables and associated operations that are **precisely specified independent of any particular implementation**
- **ADT = data + operations (no implementation)**
- In OOP, we don't define data for defining procedures; we **define the procedures necessary for defining data**
- An ADT is a type that combines data and procedures. In C++, a **class** is used to define an ADT
- The user only needs to know **what** an ADT does, not **how** it does it (e.g. push/pop of a stack)

> Exam point: 2025 essay "ADT is called abstract because … (its data and operations are specified independently of any particular implementation)".

## Class and Object {#class-object}

- **class**: defines the attributes (= **member variables**) and behaviors (= **member functions**) of an object
- **object**: **an instance of a class**. Consists of internal data, internal operations, and **interface operations**
  - Has identity, attributes, behavior (methods), and relationships with other objects
  - **Only class methods** can access the internal data of an object
  - **Message passing**: requesting some work from another object by calling a method
- **Class vs Object**
  - Each object generated by the same class is a **different object** (each gets its own memory space and address)
  - Objects created by the same class **share the class's methods**
  - An object can be dynamically constructed or destructed during run-time

> Exam point: 2016 blank "(An object) is an instance of a class".

## Information Hiding · Encapsulation (Overview) {#encap-intro}

- **Encapsulation conceals the functional details** of a class from objects that send messages to it
- **Internal data of an object can be modified only through an interface**
- Object diagram: interface operations (specification) on the outside; data and internal operations (implementation) inside

> Exam point: 2025 blank "In the concept of information hiding, (internal data) of an object can be modified only through (an interface)". Details in U4.

## Inheritance and Polymorphism {#inherit-poly}

- **Inheritance**: a child class (sub class) inherits the attributes and behaviors of the parent class (super class) and can define its own. The child's properties should be mostly similar to the parent's. **Goal: object (class) reuse** → reduces the cost of large SW development
- **Polymorphism**: allows the same method (message) to have different meanings. The ability of objects of different types to respond to method calls of the same name, each according to an appropriate type-specific behavior
  - In C++: **virtual function, operator overloading, function overloading, template**
- Dynamic binding
- **Benefits of the object model**: builds a system that evolves over time (extendible, stable); thinking in objects and classes is easier for humans; separating the client and implementor prevents accidental damage through data encapsulation; reusability

> Trap: inheritance and virtual functions come after the midterm (weeks 6–7 in the course schedule, not yet covered this year). Same as the "out of scope" mark on the dashboard.
