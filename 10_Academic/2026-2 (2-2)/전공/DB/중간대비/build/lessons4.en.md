@unit U4 | Basic SQL (DDL, DML, SELECT) | 4-1_SQL.pdf + 3-2_setup-for-sql.pdf + SQL-week6-lab.pdf
@intro Constraint syntax in CREATE TABLE, referential triggered actions (ON DELETE/UPDATE), what INSERT, DELETE and UPDATE can violate, and SELECT-FROM-WHERE. You only get better at SQL by writing it. The practice answers include the actual results of running each query on the textbook COMPANY state (3-1 p.12).

@lesson L4-1 | Introduction to SQL, CREATE SCHEMA/TABLE, Constraints | 4-1 p.3–10

## SQL and NL2SQL {#sql-intro}

- **SQL (Structured Query Language)**: a special-purpose **declarative** language. Designed for IBM's first DBMS; originally called **SEQUEL** (Structured English Query Language). Pronounced 'S-Q-L' or 'SEQUEL'
- **DDL (Data Definition Language)**: commands on databases and **tables**. CREATE / ALTER / DROP (schema, table)
- **DML (Data Manipulation Language)**: commands on **tuples** in tables. Retrieval: SELECT; modification: INSERT / DELETE / UPDATE
- **NL2SQL**: technology that translates natural-language queries into SQL. Challenges = ambiguity of natural language, schema understanding and linking (schema linking), generalization to unseen databases, generating complex queries. Even LLM-based methods are still far from perfect → **understanding SQL properly matters**

## CREATE SCHEMA / CREATE TABLE {#create-table}

**SQL schema**: the elements that describe a schema — tables, types, constraints, views, domains, etc. Identified by a schema name.

```
CREATE SCHEMA COMPANY AUTHORIZATION 'Jsmith';
```
- **Authorization identifier**: the user who owns the schema

**CREATE TABLE**: creates a new relation by giving its name, attributes and initial constraints.
- The table name can be prefixed with the schema name: `CREATE TABLE COMPANY.EMPLOYEE`
- Attributes = a list of <attribute name, data type> pairs
- Initial constraints = attribute constraints, integrity constraints

```
CREATE TABLE EMPLOYEE
( Fname      VARCHAR(15)    NOT NULL,
  Minit      CHAR,
  Lname      VARCHAR(15)    NOT NULL,
  Ssn        CHAR(9)        NOT NULL,
  Bdate      DATE,
  Address    VARCHAR(30),
  Sex        CHAR,
  Salary     DECIMAL(10,2),
  Super_ssn  CHAR(9),
  Dno        INT            NOT NULL,
  PRIMARY KEY (Ssn) );
```

## Attribute constraints: NOT NULL, DEFAULT {#attr-constraints}

- **NOT NULL**: the attribute's value cannot be NULL. **Always implicitly** applied to PK attributes (= entity integrity)
- **DEFAULT <value>**: if a new tuple does not give a value for the attribute, the default value is used
  - e.g., a new employee's default department: `Dno INT NOT NULL DEFAULT 1`; in DEPARTMENT, `Mgr_ssn CHAR(9) NOT NULL DEFAULT '888665555'`

## Key constraints: PRIMARY KEY, UNIQUE, FOREIGN KEY {#key-clauses}

```
CREATE TABLE DEPARTMENT
( Dname           VARCHAR(15)  NOT NULL,
  Dnumber         INT          NOT NULL,
  Mgr_ssn         CHAR(9)      NOT NULL,
  Mgr_start_date  DATE,
  PRIMARY KEY (Dnumber),
  UNIQUE (Dname),
  FOREIGN KEY (Mgr_ssn) REFERENCES EMPLOYEE(Ssn) );
CREATE TABLE DEPT_LOCATIONS
( Dnumber    INT          NOT NULL,
  Dlocation  VARCHAR(15)  NOT NULL,
  PRIMARY KEY (Dnumber, Dlocation),
  FOREIGN KEY (Dnumber) REFERENCES DEPARTMENT(Dnumber) );
```
- **PRIMARY KEY**: the attribute(s) that make up the PK. If composite, list several inside the parentheses
- **UNIQUE**: an alternate key = a **candidate key**
- **FOREIGN KEY ... REFERENCES table(attribute)**: an FK that references the PK of another relation
- Naming a constraint: `CONSTRAINT DEPTPK PRIMARY KEY (Dnumber)` → the name is needed to drop it later with ALTER

> Exam point: referential integrity can be violated when a referenced PK is updated or deleted; **SQL's default action is to reject** the operation. The alternative = referential triggered actions (L4-2).

@lesson L4-2 | Referential Triggered Actions, DROP, ALTER | 4-1 p.11–20

## Referential triggered actions {#ref-actions}

An action attached to an FK that answers **"what happens when a tuple referenced by other tuples is deleted/updated?"**
- **Triggers**: `ON DELETE`, `ON UPDATE`
- **Actions**: `SET NULL`, `CASCADE`, `SET DEFAULT` (if none is given, the default = reject; called REJECT in the slide exercise)

| Action | When the referenced tuple is deleted | When it is updated |
|---|---|---|
| SET NULL | Set the referencing FK to NULL | Set the FK to NULL |
| SET DEFAULT | Set the FK to its default value | Set the FK to its default value |
| CASCADE | **Delete the referencing tuples too** | Change the referencing FK **to the new value** |

```
CREATE TABLE EMPLOYEE
( ...,
  Dno INT NOT NULL DEFAULT 1,
  CONSTRAINT EMPPK PRIMARY KEY (Ssn),
  CONSTRAINT EMPSUPERFK FOREIGN KEY (Super_ssn) REFERENCES EMPLOYEE(Ssn)
      ON DELETE SET NULL      ON UPDATE CASCADE,
  CONSTRAINT EMPDEPTFK  FOREIGN KEY (Dno) REFERENCES DEPARTMENT(Dnumber)
      ON DELETE SET DEFAULT   ON UPDATE CASCADE );
```

**Slide discussion (p.13)**: what happens if EMPSUPERFK's ON DELETE is changed to **CASCADE** and `DELETE FROM EMPLOYEE WHERE Lname = 'Borg';` is executed?
- Wong and Wallace, whose supervisor is Borg (888665555), are deleted too → then Smith, Narayan, English, Zelaya and Jabbar, whose supervisors are Wong and Wallace, are deleted in a chain → **all 8 EMPLOYEE tuples disappear**. The key point is that CASCADE propagates recursively
- (This considers only EMPSUPERFK. In reality, if other FKs such as WORKS_ON.Essn and DEPENDENT.Essn use the default action (reject), those tuples reference employees that would be deleted, so the whole DELETE is rejected)

**Slide Exercise 1 (LIBRARY)** sample answer:
| FK | ON DELETE | ON UPDATE | Reason |
|---|---|---|---|
| BOOK_AUTHORS.Book_id → BOOK | CASCADE | CASCADE | If a book is deleted, its author info is no longer needed |
| BOOK.Publisher_name → PUBLISHER | REJECT | CASCADE | Do not allow deleting a publisher that still has books |
| BOOK_COPIES.Book_id → BOOK | CASCADE | CASCADE | If a book is removed from the catalog, its copies are no longer managed |
| BOOK_COPIES.Branch_id → LIBRARY_BRANCH | CASCADE | CASCADE | Deleting a branch = the branch closes |
| BOOK_LOANS.Book_id → BOOK | REJECT (or CASCADE) | CASCADE | Even if removed from the catalog, loaned books must be returned |
| BOOK_LOANS.Branch_id → LIBRARY_BRANCH | CASCADE (or REJECT) | CASCADE | When a branch closes, its loans are forgiven |
| BOOK_LOANS.Card_no → BORROWER | REJECT | CASCADE | A borrower can leave only after returning all books |

> Exam point: there is no single right answer; an answer is accepted **if the reason is sound**. ON UPDATE is almost always CASCADE (when a key changes, references must follow it to stay traceable).

## DROP SCHEMA / DROP TABLE {#drop}

Schema modification = changing the **schema**, not tuples (adding/dropping tables, attributes, constraints).

- **DROP SCHEMA**: drops an entire schema
  - `CASCADE`: also drops all elements of the schema (tables, domains, etc.)
  - `RESTRICT`: drops the schema **only if it has no elements** (the user must drop the elements one by one)
- **DROP TABLE**: drops a specific table. Removes all tuples + **the table definition from the catalog**
  - To delete only the tuples and keep the definition, use the **DELETE** command
  - `CASCADE`: automatically drops constraints and elements that reference the table too
  - `RESTRICT`: drops the table only if no constraint or element references it

## ALTER TABLE {#alter}

Changes a table definition: adding/dropping attributes and constraints, changing column definitions (type, constraints).
```
ALTER TABLE COMPANY.EMPLOYEE ADD COLUMN Job VARCHAR(12);
ALTER TABLE COMPANY.EMPLOYEE DROP COLUMN Address CASCADE;
ALTER TABLE COMPANY.EMPLOYEE DROP CONSTRAINT EMPSUPERFK CASCADE;
```
- DROP COLUMN `CASCADE`: automatically drops constraints that reference the column too / `RESTRICT`: only if no element references the column
- A column added with ADD COLUMN is NULL (or the DEFAULT value) in existing tuples. So putting NOT NULL on a new column requires a DEFAULT

@lesson L4-3 | INSERT, DELETE, UPDATE | 4-1 p.22–27

## INSERT {#dml-insert}

**Form 1: values for all attributes** — list the values **in the same order** as the attributes were specified in CREATE TABLE
```
INSERT INTO EMPLOYEE
VALUES ('Richard', 'K', 'Marini', '653298653', '1962-12-30',
        '98 Oak Forest, Katy, TX', 'M', 37000, '653298653', 4);
```
**Form 2: explicit attribute names** — attributes that are **NOT NULL and have no DEFAULT must** be included
```
INSERT INTO EMPLOYEE (Fname, Lname, Dno, Ssn)
VALUES ('Richard', 'Marini', 4, '653298653');
```
**Constraint violation examples (rejected)**
- `INSERT INTO EMPLOYEE (Fname, Lname, Ssn, Dno) VALUES ('Robert', 'Hatcher', '980760540', 2);` → no department with Dnumber=2 → **referential integrity**
- `INSERT INTO EMPLOYEE (Fname, Lname, Dno) VALUES ('Robert', 'Hatcher', 5);` → no Ssn → **NOT NULL** (it is the PK, so entity integrity)

## DELETE and UPDATE {#dml-delete-update}

**DELETE**: the WHERE clause selects the tuples to delete from **one relation**
- Explicitly deletes from only one table at a time. With a referential triggered action (ON DELETE CASCADE) it can propagate to other relations
- The number of tuples deleted varies (on the COMPANY state):

```
DELETE FROM EMPLOYEE WHERE Lname = 'Brown';        -- 0 tuples
DELETE FROM EMPLOYEE WHERE Ssn = '123456789';      -- 1 tuple
DELETE FROM EMPLOYEE WHERE Dno = 5;                -- 4 tuples
DELETE FROM EMPLOYEE;                              -- all of them!
```
> Caution: **if WHERE is omitted, all tuples are deleted.** The table definition remains (unlike DROP TABLE).

**UPDATE**: the WHERE clause selects the tuples to modify in **one relation**, and **SET** specifies the attributes to change and their new values
```
UPDATE PROJECT  SET Plocation = 'Bellaire', Dnum = 5  WHERE Pnumber = 10;
UPDATE EMPLOYEE SET Salary = Salary * 1.1             WHERE Dno = 5;
```
- A single UPDATE can modify several tuples (the 4 employees with Dno=5 all get a 10% raise at once)
- With ON UPDATE CASCADE it propagates to other relations

@lesson L4-4 | SELECT-FROM-WHERE, Aliases | 4-1 p.28–34

## The SELECT-FROM-WHERE block {#sfw}

```
SELECT  <attribute list>      -- projection attributes
FROM    <table list>          -- relations needed by the query
WHERE   <condition>;          -- selection conditions + join conditions
```
**Query 1**: the birth date and address of 'John B. Smith'
```
SELECT Bdate, Address
FROM   EMPLOYEE
WHERE  Fname = 'John' AND Minit = 'B' AND Lname = 'Smith';
```
→ 1965-01-09, 731 Fondren, Houston, TX

**Query 2**: the name and address of all employees who work for the 'Research' department
```
SELECT Fname, Lname, Address
FROM   EMPLOYEE, DEPARTMENT
WHERE  Dname = 'Research' AND Dnumber = Dno;
```
- `Dname = 'Research'` = **selection condition** (picks the tuples of interest from one table)
- `Dnumber = Dno` = **join condition** (combines DEPARTMENT tuples with EMPLOYEE tuples)
- Result: Smith, Wong, Narayan, English (4 employees)

## Ambiguous attribute names and aliases {#qualify-alias}

**Qualifying**: if attributes in different relations have the same name, distinguish them as `RelationName.Attribute`.
```
SELECT Fname, EMPLOYEE.Name, Address
FROM   EMPLOYEE, DEPARTMENT
WHERE  DEPARTMENT.Name = 'Research' AND DEPARTMENT.Dnumber = EMPLOYEE.Dnumber;
```
**Alias (tuple variable)**: shortens repeated long names, and is required when referring to **the same relation twice**.
```
SELECT E.Fname, E.Lname, S.Fname, S.Lname
FROM   EMPLOYEE AS E, EMPLOYEE AS S
WHERE  E.Super_ssn = S.Ssn;
```
→ The names of employees and their immediate supervisors. E = employee role, S = supervisor role. Borg, who has no supervisor, is not in the result (7 rows).

> Trap: on slide p.32, `FROM EMPLOYEE AS E WHERE E.Super_ssn = E.Ssn` has only one alias, so it becomes a query for "employees who are their own supervisor" (0 rows). It shows that using the same table in two roles requires **two** aliases.

## Missing WHERE and * {#missing-where-star}

**Missing WHERE**: no tuple selection condition → all tuples of the relations in FROM are retrieved.
- With two or more relations, **all possible tuple combinations (the Cartesian product)** are produced
- `SELECT Ssn, Dname FROM EMPLOYEE, DEPARTMENT;` → 8 × 3 = **24 rows**
- Leaving out even one condition gives a wrong and very large result, so **write every condition in WHERE**

**Asterisk (*)**: the values of **all attributes** of the selected tuples. `SELECT * FROM EMPLOYEE WHERE Dno = 5;` → 4 rows, 10 columns.

@lesson L4-5 | Multisets, Set Operations, ORDER BY, Operators | 4-1 p.35–41

## Multisets and DISTINCT {#multiset-distinct}

**SQL treats a table not as a set but as a multiset** → a table or query result may contain **duplicate tuples**, and SQL **does not eliminate duplicates automatically**.

Why?
- Duplicate elimination is an **expensive** operation (sort the tuples first, then remove duplicates)
- The user may want to see duplicates
- Duplicates are needed when applying aggregate functions (e.g., average salary) → week 5

Keywords
- **ALL** (default): keeps duplicates. `SELECT ALL Salary FROM EMPLOYEE;` → 8 rows (25000 appears 3 times)
- **DISTINCT**: eliminates duplicates. `SELECT DISTINCT Salary FROM EMPLOYEE;` → 6 rows

## Set operations UNION / EXCEPT / INTERSECT {#set-ops}

- **UNION**, **EXCEPT** (difference), **INTERSECT**. The result is a **set** of tuples → **duplicates are eliminated**
- Applies only to **type-compatible** relations (same number of attributes, and corresponding attributes have the same domain)
- Multiset versions: **UNION ALL, EXCEPT ALL, INTERSECT ALL** (keep duplicates)
  - R(A) = {a1, a2, a2, a3}, S(A) = {a1, a2, a4, a5}
  - R UNION ALL S = {a1, a1, a2, a2, a2, a3, a4, a5}
  - R EXCEPT ALL S = {a2, a3}
  - R INTERSECT ALL S = {a1, a2}

**Query 4**: project numbers of projects that involve an employee whose last name is 'Smith', either as a **worker** or as a **manager** of the department that controls the project
```
( SELECT DISTINCT Pnumber
  FROM   PROJECT, DEPARTMENT, EMPLOYEE
  WHERE  Dnum = Dnumber AND Mgr_ssn = Ssn AND Lname = 'Smith' )
UNION
( SELECT DISTINCT Pnumber
  FROM   PROJECT, WORKS_ON, EMPLOYEE
  WHERE  Pnumber = Pno AND Essn = Ssn AND Lname = 'Smith' );
```
→ Smith is not a manager, so the first block is empty; as a worker, 1 and 2 → result {1, 2}

## ORDER BY, arithmetic operators, BETWEEN {#order-arith}

**ORDER BY**: sorts result tuples by attribute values. **Default is ascending (ASC)**; DESC for descending.
```
SELECT   D.Dname, E.Lname, E.Fname, P.Pname
FROM     DEPARTMENT AS D, EMPLOYEE AS E, WORKS_ON AS W, PROJECT AS P
WHERE    D.Dnumber = E.Dno AND E.Ssn = W.Essn AND W.Pno = P.Pnumber
ORDER BY D.Dname DESC, E.Lname ASC, E.Fname ASC;
```
**Arithmetic operators** + − * /: applied to numeric attributes. **The relation state does not change** (only the result reflects it)
```
SELECT E.Fname, E.Lname, 1.1 * E.Salary AS Increased_sal
FROM   EMPLOYEE AS E, WORKS_ON AS W, PROJECT AS P
WHERE  E.Ssn = W.Essn AND W.Pno = P.Pnumber AND P.Pname = 'ProductX';
```
→ Smith 33000, English 27500

**BETWEEN**: a range condition. `(Salary BETWEEN 30000 AND 40000)` = `((Salary >= 30000) AND (Salary <= 40000))` → **both ends inclusive**
```
SELECT * FROM EMPLOYEE WHERE (Salary BETWEEN 30000 AND 40000) AND Dno = 5;
```
→ Smith (30000), Wong (40000), Narayan (38000)

> Lab note (3-2, week 6 lab): the lab uses SQLite + Python (pandas, sqlglot). Read NL_queries.txt, write SQL in mysql.py, and run test.py to produce the result CSVs. The submitted zip file must be named with your student ID. **SQLite does not support ALL or ANY.**
