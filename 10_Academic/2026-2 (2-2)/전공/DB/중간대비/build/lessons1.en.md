@unit U1 | Database System Concepts and Architecture | 1_course_intro.pdf + 2_intro-ER.pdf p.3–10
@intro The differences between a DB, a DBMS and a database system, the four characteristics of the database approach, the three-schema architecture and data independence. This part is ideal for one-line definition questions, so memorize the English keywords along with each idea.

@lesson L1-1 | DB, DBMS and Database System | 1_course_intro p.15–18, 24

## DB, DBMS, Database System {#db-def}

| Term | Definition |
|---|---|
| **Database (DB)** | A logically coherent collection of related data. It is managed by a DBMS |
| **DBMS** | Software that efficiently "manages" data in a structured way. It is used for **defining, constructing, manipulating and sharing** databases. e.g., IBM DB2, Oracle, MS SQL Server, MySQL, SQLite |
| **Database System** | **DB + DBMS software** |

> Exam point: pair the four DBMS verbs (define, construct, manipulate, share) with "database system = DB + DBMS".

## Why use a DBMS? {#why-dbms}

Slide example: storing a messaging app's data (friend info, messages) in a **text file**, one record per line with attributes separated by commas, causes three groups of problems.

- **Data Integrity**: How do we enforce the message length limit? What if a friend's info is entered twice by mistake? What about friends with the same name?
- **Data Management**: How do we find a specific message quickly? What if many users read and write at the same time?
- **Data Durability**: What if the machine crashes while the app is writing? How do we recover after a crash?

→ We cannot solve these technical problems ourselves every time, so we use a DBMS. Applications: e-commerce, banking, social media, universities/libraries, airline and railway reservations.

## When NOT to use a DBMS {#when-not}

**Overhead of a DBMS**
- **High initial investment** in hardware, software and training
- The cost of **generality** that a DBMS provides for defining and processing data
- Overhead of security, concurrency control, recovery and integrity functions → "too heavy"

**When a customized database is better**
- Simple, well-defined applications that are **not expected to change at all** (no insertions, deletions or updates)
- **Stringent real-time requirements** that a DBMS cannot meet
- **Embedded systems** with limited storage capacity
- **No multiple-user access** to the data

@lesson L1-2 | Four Characteristics of the Database Approach | 1_course_intro p.19–25

## 1) Self-Describing Nature {#self-desc}

A database system contains not only the database itself but also **metadata**.
- **Metadata**: the definition of the database structure and constraints
- Metadata is stored in the **DBMS catalog**. It is essential for maintaining the database
- How to define it = SQL DDL (weeks 4–5)

> Trap: metadata is stored in the "catalog". In a file system, the data structure definitions are embedded in the application programs.

## 2) Data Abstraction {#abstraction}

**Insulation between programs and data**
- A database system provides a **conceptual representation (logical level)** of data: objects, their properties and their interrelationships
- It hides the complex **physical-level** details (how data is stored, how operations are implemented)
- Programs are not affected when the data structure changes → **program-data independence**

## 3) Support of Multiple Views {#multi-views}

Each user may need a different perspective of the data.
- **View**: **virtual data that is derived from the database but not explicitly stored**
- Users do not need to know whether the data they see is stored or derived
- e.g., in a university DB, view 1 = print each student's transcript, view 2 = check each course's prerequisites

## 4) Sharing of Data and Multiuser Transaction Processing {#sharing}

- Multiple users access the database **at the same time**. Data from many applications is integrated and managed in a single database
- e.g., several reservation agents try to assign the last remaining seat on a flight at the same time
- **Concurrency control** is required
- **Transaction**: a collection of operations that performs a single logical function
- A transaction must satisfy **ACID**: **A**tomicity, **C**onsistency, **I**solation, **D**urability → week 14

> Exam point: know the four characteristics' exact English names + one line each: "self-describing / data abstraction / multiple views / sharing & multiuser transaction processing".

@lesson L1-3 | Data Models, Three-Schema Architecture, Data Independence | 2_intro-ER p.3–10

## Three categories of data models {#data-models}

**Data model**: a collection of concepts that describe the structure of a database. A "tool" for data abstraction (data types, relationships, constraints, retrieval and update operations).
- Abstraction = emphasizing the essential features needed to understand the data while hiding the details of how data is organized and stored

| Category | Level | Description |
|---|---|---|
| **Conceptual** | high-level | Concepts close to the way users perceive data. e.g., the ER model (EMPLOYEE, DEPARTMENT, PROJECT) |
| **Representational** | intermediate | How the DBMS manages data. Hides physical storage details but can be implemented directly on a computer. e.g., the relational data model |
| **Physical** | low-level | How data is stored in the computer: record formats, record orderings, access paths. Meant for specialists, not typical end users |

## Three-Schema Architecture {#three-schema}

**Goal: separate user applications from the physical database** → independence between user programs and data.

| Level | Schema | What it describes |
|---|---|---|
| **External** | External schema / user view | The part of the database that a particular user group is interested in |
| **Conceptual** | Conceptual schema | The logical structure of the whole database, described with a **representational data model**: entities, data types, relationships, user operations, constraints. Hides physical storage structures |
| **Internal** | Internal schema | The physical storage structure of the database, described with a **physical data model**: details of data storage and access paths |

> Trap: actual data is stored **only at the physical (internal) level**. The external and conceptual schemas are only "descriptions".

## Mappings between schemas {#schema-mapping}

Since actual data exists only at the internal level, the DBMS must **transform** requests and results between levels.
- Request: transformed external schema → conceptual schema → internal schema, then processed over the stored database
- Result: data extracted from the stored database is reformatted to match the user's external view
- **Mapping information is also stored in the catalog**

## Data Independence {#data-indep}

**The capacity to change the schema at one level without having to change the schema at the next higher level.**

| Type | What changes | Example |
|---|---|---|
| **Logical data independence** | **Conceptual schema** | Adding new data, removing data → external schemas and application programs stay the same |
| **Physical data independence** | **Internal schema** | Reorganizing storage structures, adding an access path (index) to speed up retrieval → conceptual schema stays the same |

→ It **greatly reduces the maintenance burden** on existing application programs.

> Exam point: do not mix them up: "logical = change to the conceptual schema, physical = change to the internal schema". Physical independence is easier to achieve (adding an index is common).
