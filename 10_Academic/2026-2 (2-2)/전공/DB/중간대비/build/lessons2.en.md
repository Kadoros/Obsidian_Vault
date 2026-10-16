@unit U2 | The ER Model (Conceptual Design) | 2_intro-ER.pdf p.11–47 + 2-2_ER_model-practices.pdf
@intro Requirements → entities and attributes → relationships and constraints → refinement. The exam is likely to give requirement sentences and ask you to draw an ER diagram or write (min, max), so practice turning "a requirement sentence → the right notation".

@lesson L2-1 | Design Process, Entities and Attributes | 2_intro-ER p.12–21

## The database design process {#design-process}

1. **Requirements Collection and Analysis**: understand the data requirements of prospective users. Output = a detailed set of user requirements
2. **Conceptual Design**: choose a data model and translate the requirements into a **conceptual schema** (ER model)
3. **Implementation**: implement the database from the conceptual schema
   - **Logical design**: the database schema (e.g., relational schema; ER-to-relational mapping in week 3)
   - **Physical design**: the physical layout of the database

COMPANY requirements: the company is organized into **departments** (unique name and number, several locations, a manager and the manager's start date); a department controls a number of **projects** (unique name and number, a single location). An **employee** has a name, SSN, address, salary, sex, birth date and the projects they work on; for insurance purposes, each employee's **dependents** (name, sex, birth date, relationship) are also kept.

## Entities and attributes {#entity-attr}

**ER (Entity-Relationship) model**: describes data as **collections of entities and relationships**. Drawn as an ER diagram.
- **Entity**: a "thing" in the real world with an **independent existence**, distinguishable from other things. It may be a physical object (an employee) or a conceptual one (a company)
- **Attribute**: a particular property that describes an entity. e.g., employee: name, address, age, home phone
- **Relationship**: an association among several entities

## Types of attributes {#attr-types}

| Classification | Pair | Examples |
|---|---|---|
| ① Composite vs simple | **Composite**: can be divided into smaller parts / **Simple (atomic)**: not divisible | Address = (Street_address, City, State, Zip) / City, Zip |
| ② Single-valued vs multivalued | **Single-valued**: one value per entity / **Multivalued**: a set of values | Age, SSN / Phone numbers, College degrees, a department's Locations |
| ③ Stored vs derived | **Stored**: actually stored in the DB / **Derived**: computed from other attributes | Birth_date / Age (derived from birth date) |

> Trap: do not confuse "multivalued" with "composite". Composite = one value splits into several parts; multivalued = there are several values. An attribute can be both (e.g., {Address_phone(Phone, Address)}).

## Key attributes {#key-attr}

**Key attribute**: an attribute whose values are **distinct** for each entity → uniquely identifies each entity.
- e.g., a STUDENT's student ID, a PERSON's SSN
- Several attributes together can form one key (e.g., CAR's Registration = (Number, State), a composite key)
- An entity type can have **more than one** key (e.g., CAR's keys = Registration, Vehicle_id)
- Shown **underlined** in the diagram

## ER diagram notation {#er-notation}

| Symbol | Meaning |
|---|---|
| Rectangle | Entity type |
| **Double** rectangle | Weak entity type |
| Diamond | Relationship type |
| **Double** diamond | Identifying relationship type |
| Oval | Attribute |
| Oval with underlined name | Key attribute |
| **Double** oval | Multivalued attribute |
| Oval with ovals attached | Composite attribute |
| **Dashed** oval | Derived attribute |
| E₁ — R **═** E₂ (double line) | **Total participation** of E₂ in R |
| E₁ ─1─ R ─N─ E₂ | Cardinality ratio 1:N |
| R ─(min,max)─ E | Structural constraint (min, max) on participation of E in R |

## Initial conceptual design: COMPANY {#initial-design}

- **DEPARTMENT**: Name, Number, {Locations}, Manager, Manager_start_date. Name and Number are each keys (both unique). Locations is multivalued
- **PROJECT**: Name, Number, Location, Controlling_department. Name and Number are keys
- **EMPLOYEE**: Name (composite: Fname, Minit, Lname), SSN (key), Address, Salary, Birth_date, Sex, Department, Supervisor, {Works_on(Project, Hours)}
- **DEPENDENT**: Employee, Dependent_name, Sex, Birth_date, Relationship

Problem: attributes such as Manager, Department, Supervisor, Works_on and Employee actually **refer to other entities**. Relationships are hidden **implicitly** as attributes → they must be turned into explicit **relationship types** (L2-4 refinement).

@lesson L2-2 | Relationship Types, Degree, Roles, Constraints | 2_intro-ER p.23–30, 36–37

## Relationship type, degree, role names {#rel-type}

**Relationship type**: described by a name + the participating entity types. It defines a set of associations among the participating entities.
- e.g., WORKS_FOR: between EMPLOYEE and DEPARTMENT. It associates each employee with the department they work for
- **Degree**: the number of participating entity types. Binary, ternary, … most are binary
  - Binary example: rᵢ = (eⱼ, dₖ); ternary example: SUPPLY's rᵢ = (sⱼ, pₖ, jₗ) (SUPPLIER, PART, PROJECT)
- **Role name**: the role a participating entity plays in each relationship instance. Helps explain what the relationship means. e.g., in WORKS_FOR, EMPLOYEE = worker, DEPARTMENT = employer

## Recursive relationship {#recursive}

A relationship in which **the same entity type participates more than once in different roles**. **Role names are required** to distinguish the participants.
- e.g., SUPERVISION: EMPLOYEE participates as supervisor (line '1') and as supervisee (line '2')
- r₂ = (e₁, e₂): Kim is Lee's supervisor / r₁ = (e₅, e₁): Kim is Kang's supervisee

## Constraint ① Cardinality ratio {#cardinality}

**The maximum number of relationship instances that an entity can participate in.** For binary relationships: 1:1, 1:N, M:N.

| Ratio | Example | Real-world constraint |
|---|---|---|
| **1:N** | WORKS_FOR (DEPARTMENT 1 : EMPLOYEE N) | An employee works for only one department; a department can have any number of employees |
| **1:1** | MANAGES (EMPLOYEE 1 : DEPARTMENT 1) | An employee manages at most one department; a department has at most one manager |
| **M:N** | WORKS_ON (EMPLOYEE M : PROJECT N) | An employee works on many projects; a project has many employees |

> Trap: in 1:N, one entity on the **N-side** is related to **at most one** entity on the 1-side. "One employee → at most one department", so EMPLOYEE is the N-side.

## Constraint ② Participation constraint {#participation}

Specifies **whether the existence of an entity depends on its being related to another entity**. It concerns the minimum number of participations.
- **Total participation**: **every** entity must participate in the relationship. Double line. e.g., every employee must work for some department, so EMPLOYEE has total participation in WORKS_FOR (= existence dependency)
- **Partial participation**: not every entity needs to participate. Single line. e.g., not every employee manages a department, so EMPLOYEE has partial participation in MANAGES

## (min, max) notation {#minmax}

Attach a **(min, max)** pair to each participation to show cardinality and participation together. 0 ≤ min ≤ max, max ≥ 1.
- **min = 0 → partial participation, min ≥ 1 → total participation**
- max = the maximum number of relationship instances that the entity can participate in
- e.g., MANAGES: EMPLOYEE (0,1), DEPARTMENT (1,1)

> Trap: (min,max) is written **on that entity's side and means how many times one such entity** participates in the relationship. The "1" and "N" of 1:N notation are written on the **opposite** side (DEPARTMENT ─1─ WORKS_FOR ─N─ EMPLOYEE). So for WORKS_FOR the (min,max) values look reversed: EMPLOYEE (1,1), DEPARTMENT (4,N).

Slide Exercise 1 (INSTRUCTOR–TEACHES–COURSE–USES–TEXT):
- A course may or may not use a textbook, but not more than five → COURSE's participation in USES **(0, 5)**
- A course is taught by at least 1 and at most 4 instructors → COURSE's participation in TEACHES **(1, 4)**
- A textbook is used in some courses → TEXT's participation in USES **(1, N)**
- An instructor teaches 2 to 4 courses → INSTRUCTOR's participation in TEACHES **(2, 4)**

@lesson L2-3 | Relationship Attributes, Weak Entities | 2_intro-ER p.31–35

## Attributes of relationship types {#rel-attr}

Relationship types can also have attributes. e.g., MANAGES' StartDate, WORKS_ON's Hours, WORKS_FOR's StartDate.

| Relationship | Where the attribute can be migrated |
|---|---|
| **1:1** | To **either** participating entity type (MANAGES.StartDate → DEPARTMENT or EMPLOYEE) |
| **1:N** | **Only to the entity type on the N-side** (WORKS_FOR.StartDate → EMPLOYEE) |
| **M:N** | **Cannot be migrated to either entity**, because it is determined only by the combination of participating entities (WORKS_ON.Hours is determined by the employee–project combination) |

> Exam point: "Why can a 1:N relationship attribute go only to the N-side?" → one N-side entity participates in at most one relationship instance, so its value is uniquely determined. A 1-side entity participates in many instances, so it would have many values.

## Weak entity types {#weak-entity}

**Weak entity type**: an entity type that **does not have key attributes of its own**. It depends on an **identifying (owner) entity type**.
- A weak entity must be related to an identifying entity
- **Identifying relationship**: the relationship that relates a weak entity type to its owner entity type. Double diamond
- A weak entity type **always has total participation** in its identifying relationship
- **Partial key**: the attribute that distinguishes weak entities related to the same owner. Dashed underline
  - e.g., DEPENDENT's Dependent_name (assuming no two dependents of the same employee share a name)
  - The partial key alone cannot identify an entity (another employee may also have a dependent named Tom) → identified by **owner's key + partial key**

@lesson L2-4 | Refining the COMPANY Design, Practice (MOVIE, CONF_REVIEW) | 2_intro-ER p.38–47, 2-2 p.14–26

## Refining the COMPANY design {#refine}

Change attributes that represent relationships **into relationship types**.

| Relationship | Participants | Cardinality | Participation | Attributes |
|---|---|---|---|---|
| **MANAGES** | EMPLOYEE, DEPARTMENT | 1:1 | EMPLOYEE partial, DEPARTMENT total | Start_date (Manager_start_date) |
| **WORKS_FOR** | EMPLOYEE, DEPARTMENT | 1:N (DEPARTMENT 1, EMPLOYEE N) | Both total | None |
| **CONTROLS** | DEPARTMENT, PROJECT | 1:N (DEPARTMENT 1, PROJECT N) | PROJECT total, DEPARTMENT partial | None |
| **SUPERVISION** | EMPLOYEE (supervisor, supervisee) | 1:N (supervisor 1, supervisee N) | Both partial | None |
| **WORKS_ON** | EMPLOYEE, PROJECT | M:N | Both total | Hours |
| **DEPENDENTS_OF** | EMPLOYEE (identifying), DEPENDENT (weak) | 1:N (EMPLOYEE 1) | EMPLOYEE partial, DEPENDENT total | None (identifying relationship) |

What moved: DEPARTMENT's Manager and Manager_start_date → MANAGES; PROJECT's Controlling_department → CONTROLS; EMPLOYEE's Department, Supervisor, Works_on → WORKS_FOR, SUPERVISION, WORKS_ON; DEPENDENT's Employee → DEPENDENTS_OF.

> Caution: the SUPERVISION description on slide p.42 has the 1-side/N-side roles swapped. One supervisor has many supervisees, so **the supervisor is the 1-side**, and the resulting diagram (p.45) also gives (min,max) supervisor (0,N), supervisee (0,1).

**Summary of the 3 steps of ER schema design**: (1) describe entity types and attributes from the requirements → (2) specify relationship types and constraints → (3) change attributes that represent relationships into relationship types. Focus on the **schema**, not instances.

## Practice: MOVIE / CONF_REVIEW {#er-practice}

**MOVIE DB** (2-2 p.14–23)
- MOVIE: composite key MKey(Title, Year), Length, Plot_outline, {Genre} multivalued
- ACTOR, DIRECTOR: key (Name, Date_of_birth). PRODUCTION: key Name, Address
- **PRODUCES** (PRODUCTION 1 : MOVIE N): a movie is produced by one production company. MOVIE total participation
- **ACTS** (ACTOR M : MOVIE N): relationship attributes Role, {Quotes} (multivalued). Total participation on both sides
- **DIRECTS** (DIRECTOR M : MOVIE N): MOVIE total participation (at least one director)
- **DIR_ACTS**: a director may also act in a movie (Role, {Quotes})

**CONF_REVIEW DB** (2-2 p.24–26, solution in db-exercises)
- AUTHOR(A_email key, First_name, Last_name), PAPER(P_id key, Title, Abstract, File_name), REVIEWER(R_email key, name, Phone_no, Affiliation, {Interest_topic})
- **SUBMITS** AUTHOR (1,N) – PAPER (1,M): an author is recorded only after submitting a paper; a paper may have multiple authors (M:N)
- **IS_CONTACT** AUTHOR (0,N) – PAPER (1,1): each paper has exactly one contact author. SUBMITS alone cannot express this requirement, so it is a separate relationship
- **REVIEWS** REVIEWER (1,N) – PAPER (2,4): 2 to 4 reviewers per paper. Relationship attributes: Recommendation; Comments(For_committee, Feedback) composite; Rating(C1 Technical_merit, C2 Readability, C3 Originality, C4 Relevance) composite

> Exam point: "exactly one per …" = (1,1); "may or may not" = min 0; "at least a, at most b" = (a,b); "many" = max N. The key skill is spotting these words in a requirement sentence and turning them into notation.
