@unit U3 | The Relational Data Model and ER-to-Relational Mapping | 3-1_RDB.pdf
@intro Terminology (relation, tuple, attribute, domain, degree), the key family (superkey ⊃ key = candidate key ∋ primary key), the three integrity constraints, which constraints insert/delete/update can violate, and ER-to-relational mapping. For mapping, all you really need is to get "where does the FK go" right.

@lesson L3-1 | Basic Concepts of the Relational Model | 3-1 p.4–12

## The relational data model {#rel-model}

- Proposed by **Ted Codd** of IBM in 1970
- Represents data as **relations (tables)**. Each relation consists of **tuples (rows)** and **attributes (column headers)**
- Each row = a fact about a particular entity (a collection of related data values); attributes specify how to interpret the values in each row

**Four advantages**: **Simplicity** (flat table structure), **Data integrity** (ensures valid, consistent and accurate data), **Ease of data manipulation** (powerful high-level languages such as SQL handle complex conditions flexibly), **Security** (authentication, authorization, encryption)

## Domain, relation schema, instance {#domain-schema}

- **Domain D**: a **set of atomic values** allowed for an attribute. Domain = data type + constraints
  - e.g., Usa_phone_numbers: format (ddd)ddd-dddd; Employee_ages: integers between 15 and 80
- **Relation schema R(A₁, …, Aₙ)**: relation name + list of attributes. e.g., STUDENT(Name, Ssn, …, Gpa)
- **Degree**: the **number of attributes n** of a relation schema. e.g., STUDENT(Name, Ssn, Home_phone, Address, Office_phone, Age, Gpa) has degree 7
- **Relation instance (state) r(R)**: a **set** of n-tuples {t₁, …, tₘ}
- **Tuple t**: an **ordered** list of n values <v₁, …, vₙ>. Each vᵢ is an element of dom(Aᵢ) or the special value **NULL**

> Trap: degree = number of attributes (columns). The number of tuples (rows) is called the cardinality. Do not mix them up.

## Characteristics of relations {#rel-chars}

- **Values in a tuple must be atomic** (not further divisible)
  - **Composite and multivalued attributes are not allowed**
  - Multivalued attribute → represented by a **separate relation**
  - Composite attribute → represented only by its **simple component attributes**
- **NULL**: used when a value is unknown, unavailable, or does not apply to that tuple (undefined/not applicable)
- A relation is a **set** of tuples, so by definition **all tuples must be distinct**

## Relational database schema and state {#db-schema-state}

- **Relational database schema S** = a set of relation schemas {R₁, …, Rₘ} + a **set of integrity constraints IC**
  - e.g., COMPANY = {EMPLOYEE, DEPARTMENT, DEPT_LOCATIONS, PROJECT, WORKS_ON, DEPENDENT}
  - In the schema diagram, **underline = primary key**, **arrow = referential integrity** (FK → referenced PK)
- **Relational database state DB** = a set of relation states {r₁, …, rₘ}, where rᵢ is a state of Rᵢ
  - If it satisfies all integrity constraints it is a **valid state**; if it violates even one, it is an **invalid state**

@lesson L3-2 | Keys and Integrity Constraints | 3-1 p.13–21

## Superkey and key {#superkey-key}

A DBMS must provide ways to define and enforce constraints. The three core constraints = **key constraints, entity integrity, referential integrity**.

**Key constraint**: "no two distinct tuples can have the same value for the SK attributes" → in every state r, t₁[SK] ≠ t₂[SK].
- **Superkey (SK)**: a **subset of attributes that uniquely identifies each tuple**. Every relation has at least one default superkey (the set of all its attributes)
- **Key (K)**: a superkey such that removing any attribute A leaves a set that is no longer a superkey = a **minimal superkey**
  - Minimality is required for a key, optional for a superkey
  - e.g., {Ssn, Home_phone} is a superkey. Even after removing Home_phone, {Ssn} is unique → {Ssn, Home_phone} is not a key; {Ssn} is a key

> Trap: key ⊂ superkey. "Every key is a superkey, but not every superkey is a key."

## Candidate key and primary key {#candidate-pk}

- If a relation schema has more than one key, each is called a **candidate key**
- One of the candidate keys is designated as the **primary key** and used to identify tuples. **Underlined** in the schema
- e.g., CAR's candidate keys = License_number, Engine_serial_number → License_number is chosen as the PK
- It is usually better to choose a PK with **a single attribute or a small number of attributes**

## Entity integrity constraint {#entity-integrity}

**"No primary key value can be NULL"** → for every tuple t, t[PK] ≠ NULL.
- Reason: if two or more tuples had NULL primary keys, we **could not distinguish them** when referencing them from other relations
- e.g., an attribute that has NULLs, such as Office_phone, cannot be a key
- For a composite PK, **no part of the PK** may be NULL

## Referential integrity constraint {#ref-integrity}

**"The FK value of tuple t₁ must either equal the PK value of some tuple t₂, or be NULL"**
- **Foreign key (FK)**: a set of attributes in relation R₁ that **references** R₂. If t₁[FK] = t₂[PK], t₁ references t₂
- The FK of R₁ has the **same domain** as the PK of R₂
- R₁ = the **referencing relation**, R₂ = the **referenced relation**
- e.g., EMPLOYEE.Dno → DEPARTMENT.Dnumber. 'John Smith' has Dno=5 → references the 'Research' department tuple = Smith works for Research
- Why it is needed: to maintain **consistency** among tuples of two relations. If Dno=3 but department 3 does not exist, the value cannot be interpreted
- An FK can **reference its own relation** (EMPLOYEE.Super_ssn → EMPLOYEE.Ssn)

Slide exercise (find the FKs):
- SALESPERSON(Ssn, Name, Start_year, Dept_no), TRIP(Ssn, From_city, To_city, Departure_date, Return_date, Trip_id), EXPENSE(Trip_id, Account#, Amount)
  → TRIP.Ssn → SALESPERSON, EXPENSE.Trip_id → TRIP
- STUDENT(Ssn, …), COURSE(Course#, …), ENROLL(Ssn, Course#, Quarter, Grade), BOOK_ADOPTION(Course#, Quarter, Book_isbn), TEXT(Book_isbn, …)
  → ENROLL.Ssn → STUDENT, ENROLL.Course# → COURSE, BOOK_ADOPTION.Course# → COURSE, BOOK_ADOPTION.Book_isbn → TEXT

@lesson L3-3 | Update Operations and Constraint Violations | 3-1 p.23–30

## Insert {#op-insert}

Kinds of operations: **retrievals** and **updates**. Basic update operations = Insert, Delete, Update (Modify). Each one may violate constraints when applied.

**Insert**: adds one tuple to a relation. Given the relation name + a list of values (in attribute order).

**Insert can violate all three constraints.**

| Violation | Cause | Slide example (COMPANY state) |
|---|---|---|
| **Key constraint** | The new tuple's key value already exists in another tuple | <'Alicia', …, **'999887777'**, …, 4> → Ssn 999887777 already belongs to Zelaya |
| **Entity integrity** | The new tuple's PK (or part of it) is NULL | <'Cecilia', …, **NULL**, …, 4> |
| **Referential integrity** | The tuple referenced by the FK does not exist | <'Cecilia', …, '677678989', …, **7**> → no department with Dnumber=7 |

<'Cecilia', 'F', 'Kolonsky', '677678989', …, NULL, 4> **satisfies all constraints** (Super_ssn being NULL is allowed because it is an FK).

## Delete {#op-delete}

**Delete**: specify the relation name + the PK value of the tuple to delete.

**Delete can violate only referential integrity** (when the deleted tuple is referenced by other tuples).
- Delete Ssn='999887777' from EMPLOYEE → referenced by 2 WORKS_ON tuples → **violation**
- Delete Ssn='333445555' from EMPLOYEE → referenced by 4 WORKS_ON tuples + 2 EMPLOYEE tuples (Super_ssn) → **violation** (in fact DEPARTMENT.Mgr_ssn and DEPENDENT.Essn also reference it)
- Delete Essn='999887777' AND Pno=10 from WORKS_ON → nothing references it → OK

## Update (Modify) {#op-update}

**Update**: specify the attribute(s) to change and the new value(s).

**Update can violate key constraints and referential integrity. It is a problem only when a PK or FK attribute is modified.**
- Change Dno of the employee with Ssn='999887777' to **7** → no department 7 → **referential integrity** violation
- Change Ssn='999887777' to **'987654321'** → already Wallace's Ssn (key constraint) + tuples in WORKS_ON etc. that referenced 999887777 become orphans (referential integrity) → **both** violated
- Changing a PK to NULL also violates entity integrity (the slide summary lists only key and referential)

> Exam point: exactly as in the summary table — Insert = key, entity and referential **all possible**; Delete = **referential only**; Update = **key and referential** (only when changing a PK/FK).

@lesson L3-4 | ER-to-Relational Mapping ①: Entities, Multivalued Attributes, Weak Entities | 3-1 p.32–36

## Mapping regular entity types {#map-entity}

Mapping order: entity types (regular, weak) → multivalued attributes → relationship types (1:1, 1:N, M:N, n-ary).

**Regular entity type E**
1. Create a relation R that includes **all simple attributes** of E. For a composite attribute include **only its simple component attributes** (Name → Fname, Minit, Lname)
2. Choose one of E's key attributes as the **PK** of R (other keys become UNIQUE candidate keys)
3. Multivalued attributes are not included here → next step

e.g., DEPARTMENT(Dname, **Dnumber**) — Locations is left out for now.

## Mapping multivalued attributes {#map-multival}

**Multivalued attribute A** (not allowed in a relation)
1. Create a **separate relation R** for each A
2. Put A and the PK K of the original relation into R. K is an **FK** in R (referencing the original relation). Key values repeat
3. The **combination (A, K) is the PK**

e.g., DEPT_LOCATIONS(**Dnumber**, **Dlocation**), Dnumber → DEPARTMENT. (5, Seoul), (5, Incheon), (5, Suwon), (3, Seoul), (3, Daejeon)

## Mapping weak entity types {#map-weak}

**Weak entity type W**
1. Create a relation R that includes all simple attributes of W (only component attributes of composites)
2. Include the **PK of the owner entity type as an FK** → this is the **mapping of the identifying relationship type**
3. The **combination of the owner's PK + the partial key is the PK**

e.g., DEPENDENT(**Essn**, **Dependent_name**, Sex, Bdate, Relationship), Essn → EMPLOYEE.Ssn

> Trap: the identifying relationship (DEPENDENTS_OF) does not get its own relation. Putting the owner's PK in as an FK is itself the mapping of the identifying relationship.

@lesson L3-5 | ER-to-Relational Mapping ②: Relationship Types | 3-1 p.37–49

## Mapping 1:1 relationships {#map-11}

Three approaches: **foreign key approach** (most common and useful), **merged relation approach** (combine the two entities into one relation), **cross-reference (relationship relation) approach**.

**Foreign key approach**
1. Identify the participating entity types S and T
2. Choose one side (S) and include **the PK of the other side (T) as an FK**. It is better to choose **the side with total participation as S**
3. Also include the simple attributes of the relationship in S

e.g., MANAGES: choose DEPARTMENT (total participation) as S → DEPARTMENT(Dname, **Dnumber**, Mgr_ssn, Mgr_start_date), Mgr_ssn → EMPLOYEE.

**Why the total-participation side?** If we instead choose EMPLOYEE (partial participation) as S, EMPLOYEE gets D_managed and Mgr_start_date, and for most employees, who do not manage a department, these values would be **NULL**. Putting them on the total-participation side produces no NULLs.

## Mapping 1:N relationships {#map-1n}

Two approaches: **foreign key approach** (preferred because it reduces the number of relations), cross-reference approach.

**Foreign key approach**
1. Identify the relation S that represents the entity type on the **N-side**
2. Include in S the **PK of the other (1-side) relation T as an FK**
3. Also include the simple attributes of the relationship in S

Reason: one N-side entity instance is related to **at most one** 1-side entity → can be represented by a single FK value.
- WORKS_FOR → **Dno** in EMPLOYEE (→ DEPARTMENT)
- SUPERVISION → **Super_ssn** in EMPLOYEE (→ EMPLOYEE, self-reference)
- CONTROLS → **Dnum** in PROJECT (→ DEPARTMENT)

> Trap: putting the FK on the 1-side makes it multivalued, violating atomicity. The FK **always goes on the N-side**.

## Mapping M:N relationships {#map-mn}

**Only one** approach: the **cross-reference (relationship relation) approach**. An M:N relationship cannot be represented by a single FK.
1. Create a **separate relation S** to represent relationship type R
2. Include the **PKs of the participating entity relations as FKs** in S
3. The **combination of the FKs is the PK**
4. Also include the simple attributes of the M:N relationship in S

e.g., WORKS_ON(**Essn**, **Pno**, Hours), Essn → EMPLOYEE, Pno → PROJECT. Relationship relation = lookup table.

## Mapping n-ary relationships {#map-nary}

**Cross-reference approach** (same procedure as M:N)
1. Create a separate relation S
2. Include the PKs of the n participating entity relations as FKs
3. The combination of all FKs is the PK (usually; if some participation has max = 1, that FK can be left out of the PK)
4. Include the simple attributes of the relationship

e.g., SUPPLY(**Sname**, **Proj_name**, **Part_no**, Quantity) — references SUPPLIER, PROJECT, PART.

## ER ↔ relational model correspondence {#map-summary}

| ER model | Relational model |
|---|---|
| Entity type | Entity relation |
| 1:1 or 1:N relationship type | Foreign key (or relationship relation) |
| M:N relationship type | Relationship relation + **two** FKs |
| n-ary relationship type | Relationship relation + **n** FKs |
| Simple attribute | Attribute |
| Composite attribute | Set of simple component attributes |
| Multivalued attribute | Relation + foreign key |
| Value set | Domain |
| Key attribute | Primary key (or secondary key) |

Slide Exercise 3 (UNIVERSITY: COLLEGE, INSTRUCTOR, DEPT, STUDENT, COURSE, SECTION), solution order:
1. Regular entities → COLLEGE(CName, COffice, CPhone), INSTRUCTOR(Id, Rank, IName, IOffice, IPhone), DEPT(DName, DCode, DOffice, DPhone), COURSE(CCode, Credits, CoName, Level, CDesc), SECTION(SecId, SecNo, Sem, Year, Bldg, RoomNo, DaysTime), STUDENT(Sid, DOB, FName, MName, LName, Addr, Phone, Major)
2. 1:1 → DEAN: DeanId in COLLEGE (COLLEGE has (1,1) total participation); CHAIR: ChairId, CStartDate in DEPT
3. 1:N → INSTRUCTOR.Employed (EMPLOYS), DEPT.Admined (ADMINS), COURSE.Offered (OFFERS), SECTION.Taught (TEACHES), SECTION.Belongs (SECS), STUDENT.Dept (HAS)
4. M:N → TAKES(**Sid**, **SecId**, Grade)
