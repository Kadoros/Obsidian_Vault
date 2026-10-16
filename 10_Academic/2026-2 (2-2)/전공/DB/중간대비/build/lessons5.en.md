@unit U5 | Advanced SQL (Nested Queries, Joins, Aggregation, Views) | 5-1_Advanced-SQL.pdf
@intro Nested queries (IN, ALL/ANY, EXISTS), joined tables (NATURAL, OUTER), aggregation with GROUP BY/HAVING, assertions and triggers, views. This is the core of the SQL-writing questions, so solve lots of problems — especially "… who do ALL …" queries (division) and GROUP BY + HAVING.

@lesson L5-1 | Nested Queries, IN, ALL/ANY | 5-1 p.3–6

## Nested queries and IN {#nested-in}

**Nested query**: a complete SELECT-FROM-WHERE block **within the WHERE clause** of another query.
- Useful when we need to fetch existing values from the database and use them in a comparison condition
- The result is a (multi)set of tuples → the enclosing one = outer query, the inner one = inner query

**IN**: compares a value v with a (multi)set of values V. **TRUE if v is one of the elements in V**.
```
SELECT DISTINCT Pnumber
FROM   PROJECT
WHERE  Pnumber IN ( SELECT Pnumber
                    FROM   PROJECT, DEPARTMENT, EMPLOYEE
                    WHERE  Dnum = Dnumber AND Mgr_ssn = Ssn AND Lname = 'Smith' )
   OR  Pnumber IN ( SELECT Pno
                    FROM   WORKS_ON, EMPLOYEE
                    WHERE  Essn = Ssn AND Lname = 'Smith' );
```
→ Same result as Query 4 (UNION version): {1, 2}. The inner queries V1 and V2 each return a set of project numbers.

## ALL / ANY (SOME) {#all-any}

**= ANY (= SOME)**: TRUE if v equals **some** value in V → **equivalent to IN**. **= ALL**: TRUE if v equals **every** value.
- Can be combined with >, >=, <, <=, <> instead of =

```
SELECT Lname, Fname
FROM   EMPLOYEE
WHERE  Salary > ALL ( SELECT Salary FROM EMPLOYEE WHERE Dno = 5 );
```
→ Employees whose salary is greater than that of **all** employees in department 5. Dept 5 salaries = {30000, 40000, 38000, 25000} → above 40000 → Wallace (43000), Borg (55000)

> Trap: `> ANY` means "greater than at least one" = greater than the minimum. `> ALL` must be greater than the maximum. Also, the lab's **SQLite does not support ALL/ANY**, so rewrite it as `> (SELECT MAX(Salary) ...)`.

## Ambiguity in nested queries and correlated queries {#correlated}

With several levels of nesting, if the outer FROM and the inner FROM have **attributes with the same name**, the query becomes ambiguous → resolve it with **aliases**.

**Query 16**: employees who have a dependent with the **same first name and the same sex** as the employee
```
SELECT E.Fname, E.Lname
FROM   EMPLOYEE AS E
WHERE  E.Ssn IN ( SELECT D.Essn
                  FROM   DEPENDENT AS D
                  WHERE  E.Fname = D.Dependent_name AND E.Sex = D.Sex );
```
- The inner query references the outer E → **correlated nested query**: behaves as if the inner query were evaluated once for each outer tuple
- If you write Sex in the inner query without an alias, it refers to the attribute of the nearest (innermost) table
- On the COMPANY state the result is 0 rows (no such dependent)

> Exam point: "It is generally advisable to create tuple variables (aliases) for **all the tables referenced** in a query" (the slide sentence as written).

@lesson L5-2 | EXISTS / NOT EXISTS, Division Queries | 5-1 p.7–9

## EXISTS and NOT EXISTS {#exists}

Boolean functions that check **whether the result of a nested query is empty**. Usually used in WHERE.
- **EXISTS (Q)**: TRUE if there is **at least one tuple** in the result of Q
- **NOT EXISTS (Q)**: TRUE if the result of Q is **empty**

**Query 6**: employees who have **no** dependents
```
SELECT Fname, Lname
FROM   EMPLOYEE
WHERE  NOT EXISTS ( SELECT * FROM DEPENDENT WHERE Ssn = Essn );
```
→ Zelaya, Narayan, English, Jabbar, Borg (5 employees)

**Managers who have at least one dependent**: AND the two conditions
```
SELECT Fname, Lname
FROM   EMPLOYEE
WHERE  EXISTS ( SELECT * FROM DEPENDENT  WHERE Ssn = Essn )
  AND  EXISTS ( SELECT * FROM DEPARTMENT WHERE Ssn = Mgr_ssn );
```
→ Franklin Wong, Jennifer Wallace

## "For all …" (division) queries {#division-sql}

**Exercise 1**: names of employees who work on **all** the projects controlled by department 5
```
SELECT Fname, Lname
FROM   EMPLOYEE
WHERE  NOT EXISTS ( ( SELECT Pnumber FROM PROJECT WHERE Dnum = 5 )
                    EXCEPT
                    ( SELECT Pno FROM WORKS_ON WHERE Ssn = Essn ) );
```
How to read it: (all dept-5 projects) − (projects this employee works on) = **missing projects**. If **nothing** is missing (NOT EXISTS), the employee works on all of them.
- e.g., dept-5 projects = {1, 2, 3}. A works on {1, 2, 4} → difference {3} ≠ ∅ → out. B works on {1, 2, 3, 4} → difference ∅ → selected
- On the COMPANY state, dept-5 projects = {1, 2, 3}, but no employee works on all three, so the result is **0 rows**

It can also be written without EXCEPT, using NOT EXISTS twice ("there is no dept-5 project that this employee does not work on"):
```
SELECT E.Fname, E.Lname
FROM   EMPLOYEE AS E
WHERE  NOT EXISTS ( SELECT * FROM PROJECT AS P
                    WHERE  P.Dnum = 5
                      AND  NOT EXISTS ( SELECT * FROM WORKS_ON AS W
                                        WHERE W.Essn = E.Ssn AND W.Pno = P.Pnumber ) );
```

> Trap: distinguish employees who work on "some" project (EXISTS, IN) from employees who work on "all" projects (NOT EXISTS + EXCEPT). If the sentence says **all**, it is the division pattern.

@lesson L5-3 | Joined Tables, NATURAL, INNER/OUTER | 5-1 p.10–14

## Joined tables {#joined-table}

**Joined table**: a table produced by a join operation **in the FROM clause**. It avoids mixing selection and join conditions in WHERE.
```
SELECT Fname, Lname, Address
FROM   (EMPLOYEE JOIN DEPARTMENT ON Dno = Dnumber)
WHERE  Dname = 'Research';
```
- The joined table = all attributes of the first table (EMPLOYEE) + all attributes of the second table (DEPARTMENT)
- Same result as Query 2, which writes `Dnumber = Dno` in WHERE

## NATURAL JOIN {#natural-join-sql}

Creates an **implicit equality condition for each pair of attributes with the same name** → no join condition is written.
- If the names differ, **rename** the attributes first to make them match
```
SELECT Fname, Lname, Address
FROM   (EMPLOYEE NATURAL JOIN
        (DEPARTMENT AS DEPT (Dname, Dno, Mssn, Msdate)))
WHERE  Dname = 'Research';
```
- DEPARTMENT's Dnumber is renamed to Dno so that it matches EMPLOYEE.Dno
- The join attribute appears **only once** in the result

## INNER JOIN and OUTER JOIN {#inner-outer}

**Inner join**: the default join. **Only tuples that have a match in the other relation** are included in the result.
```
SELECT E.Lname AS Employee_name, S.Lname AS Supervisor_name
FROM   EMPLOYEE AS E, EMPLOYEE AS S
WHERE  E.Super_ssn = S.Ssn;
```
→ 7 rows. **Borg, whose Super_ssn is NULL, is left out**.

**Outer join**: tuples without a match are also included, and the other relation's attributes are **padded with NULL**.
```
SELECT E.Lname AS Employee_name, S.Lname AS Supervisor_name
FROM   (EMPLOYEE AS E LEFT OUTER JOIN EMPLOYEE AS S ON E.Super_ssn = S.Ssn);
```
→ 8 rows. Borg's Supervisor_name = NULL.

| Join | Tuples in the result |
|---|---|
| INNER JOIN | Only pairs that satisfy the join condition |
| LEFT OUTER JOIN | **Every tuple of the left table** (right attributes NULL if no match) |
| RIGHT OUTER JOIN | **Every tuple of the right table** |
| FULL OUTER JOIN | Every tuple of both tables |

> Trap: to select "only the unmatched ones" with an OUTER JOIN, add `WHERE B.KEY IS NULL` (bottom row of the Venn diagrams on slide p.14). Compare with NULL using **IS NULL**, not `= NULL`.

@lesson L5-4 | Aggregate Functions, GROUP BY, HAVING | 5-1 p.15–22, 48

## Aggregate functions {#aggregate}

**Aggregate function**: summarizes information from multiple tuples into a **single-tuple summary**. Mostly used in SELECT or HAVING.
- **COUNT**: the number of tuples or values
- **SUM, MAX, MIN, AVG**: applied to a (multi)set of numeric values

**Query 19**: sum, maximum, minimum and average salary of all employees
```
SELECT SUM(Salary), MAX(Salary), MIN(Salary), AVG(Salary)
FROM   EMPLOYEE;
```
→ 281000, 55000, 25000, 35125

**Query 20**: the Research department only
```
SELECT SUM(Salary), MAX(Salary), MIN(Salary), AVG(Salary)
FROM   (EMPLOYEE JOIN DEPARTMENT ON Dno = Dnumber)
WHERE  Dname = 'Research';
```
→ 133000, 40000, 25000, 33250

## COUNT and NULL, aggregates in nested queries {#count-null}

- **COUNT(*)**: the **number of rows (tuples)** in the result. Query 21 `SELECT COUNT(*) FROM EMPLOYEE;` → 8; Query 22, Research only → 4
- **COUNT(attribute)**: the number of **values** of that attribute. **NULLs are not counted**. e.g., `COUNT(Super_ssn)` → 7
- **COUNT(DISTINCT Salary)**: the number of distinct salary values → 6 (Query 23)
- An aggregate result is a single value, so it can be used as **part of a condition**:
```
SELECT Lname, Fname
FROM   EMPLOYEE
WHERE  ( SELECT COUNT(*) FROM DEPENDENT WHERE Ssn = Essn ) >= 2;
```
→ Two or more dependents: Smith (3), Wong (3)

## GROUP BY {#group-by}

**Grouping**: partitions the tuples of a relation into **nonoverlapping subsets (groups)** and applies aggregate functions to each group.
- **Grouping attribute**: the basis for forming groups. Same group = tuples with the same value of the grouping attribute(s)
- Specified in the **GROUP BY** clause. The grouping attributes should also appear in SELECT so the result shows which group each row is

**Query 24**: for each department, the department number, number of employees and average salary
```
SELECT   Dno, COUNT(*), AVG(Salary)
FROM     EMPLOYEE
GROUP BY Dno;
```
→ (5, 4, 33250), (4, 3, 31000), (1, 1, 55000)

**Query 25**: for each project, its number, name and number of employees who work on it
```
SELECT   Pnumber, Pname, COUNT(*)
FROM     PROJECT, WORKS_ON
WHERE    Pnumber = Pno
GROUP BY Pnumber, Pname;
```
→ ProductX 2, ProductY 3, ProductZ 2, Computerization 3, Reorganization 3, Newbenefits 3

> Trap: with GROUP BY, SELECT may contain **only grouping attributes and aggregate functions**. Do not put an attribute that does not have a single value per group (e.g., Lname when grouping by Dno) in SELECT.

## HAVING {#having}

**HAVING**: a **condition on the summary information** of groups. Used with GROUP BY. **Only groups** that satisfy the condition appear in the result.

**Query 26**: for each project on which **more than two** employees work, the project number, name and number of employees
```
SELECT   Pnumber, Pname, COUNT(*)
FROM     PROJECT, WORKS_ON
WHERE    Pnumber = Pno
GROUP BY Pnumber, Pname
HAVING   COUNT(*) > 2;
```
→ ProductY, Computerization, Reorganization, Newbenefits (3 employees each)

**Exercise 2**: for each department whose average salary is greater than $30,000, the department name and number of employees
```
SELECT   D.Dname, COUNT(*)
FROM     EMPLOYEE AS E, DEPARTMENT AS D
WHERE    E.Dno = D.Dnumber
GROUP BY D.Dname
HAVING   AVG(E.Salary) > 30000;
```
→ Research 4, Administration 3, Headquarters 1 (the slide solution groups by E.Dno; in standard SQL it is safer to also have D.Dname from SELECT in GROUP BY)

> Exam point: **WHERE = tuple condition (before groups are formed)**, **HAVING = group condition (after aggregation)**. A condition on an aggregate, such as "average above 30,000", cannot go in WHERE.

**Order of execution**: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY

@lesson L5-5 | Assertions, Triggers | 5-1 p.24–29

## Assertions {#assertion}

Specify **general constraints that cannot be expressed by the built-in constraints (key, entity integrity, referential integrity)**.
- e.g., the salary of an employee must not be greater than the salary of the manager of the department the employee works for
```
CREATE ASSERTION SALARY_CONSTRAINT
CHECK ( NOT EXISTS ( SELECT *
                     FROM   EMPLOYEE E, EMPLOYEE M, DEPARTMENT D
                     WHERE  E.Salary > M.Salary
                       AND  E.Dno = D.Dnumber
                       AND  D.Mgr_ssn = M.Ssn ) );
```
- The condition in parentheses after **CHECK** must be **true in every database state**
- Convention: write a **query that selects the tuples violating** the desired condition and wrap it in **NOT EXISTS** → if the result is empty, TRUE (satisfied); if not empty, FALSE (violated)

## Triggers (ECA rules) {#trigger-eca}

Specify **actions to be executed automatically when certain events occur and conditions are met**. **ECA (Event, Condition, Action) rules**.
```
CREATE TRIGGER SALARY_VIOLATION
BEFORE INSERT OR UPDATE OF SALARY, SUPERVISOR_SSN
    ON EMPLOYEE
FOR EACH ROW
    WHEN ( NEW.SALARY > ( SELECT SALARY FROM EMPLOYEE
                          WHERE SSN = NEW.SUPERVISOR_SSN ) )
        INFORM_SUPERVISOR(NEW.Supervisor_ssn, NEW.Ssn);
```
- **Event**: database update operations explicitly applied to the DB (inserting a new employee, changing a salary, changing a supervisor). **BEFORE / AFTER** runs the trigger before/after the operation. **All** possible events must be considered
- **Condition**: determines whether the action should be executed after the event occurs. The **WHEN clause**. Optional. The action runs only when it is true
- **Action**: what is executed automatically = a sequence of SQL statements, a database transaction, or an external program (e.g., the external stored procedure INFORM_SUPERVISOR)
- Uses: (1) maintaining database consistency, (2) monitoring database updates, (3) updating derived data automatically
- e.g., notify the manager when an employee's travel expenses exceed a limit

> Trap: Assertion = a **constraint** (blocks the operation if violated); Trigger = an **action** (does something when the condition holds). Both slide examples compare salaries, but one "blocks" and the other "notifies".

@lesson L5-6 | Views | 5-1 p.30–47

## Definition and use of views {#view-def}

**View**: a **virtual table** derived from base tables. It may not exist physically.
- Retrieval: no restrictions. Update: usually limited (effectively read-only)
- Why use it: **simplifies complex queries**. If you often use a multi-table join or aggregation, define it as a view and use it like a **single-table query**

```
CREATE VIEW WORKS_ON1
AS SELECT Fname, Lname, Pname, Hours
   FROM   EMPLOYEE, PROJECT, WORKS_ON
   WHERE  Ssn = Essn AND Pno = Pnumber;

CREATE VIEW DEPT_INFO (Dept_name, No_of_emps, Total_sal)
AS SELECT   Dname, COUNT(*), SUM(Salary)
   FROM     DEPARTMENT, EMPLOYEE
   WHERE    Dnumber = Dno
   GROUP BY Dname;
```
- If no attribute names are given, the view uses the attribute names of the defining query (WORKS_ON1); they can also be given explicitly (DEPT_INFO)
- Querying a view: `SELECT Fname, Lname FROM WORKS_ON1 WHERE Pname = 'ProductX';` → no need to join three tables every time
- **DROP VIEW WORKS_ON1;** → the defining tables are not affected

## View implementation: query modification vs materialization {#view-impl}

A view must always be **up-to-date** → when the defining tables change, the DBMS is responsible for reflecting it in the view.

| Approach | Description | Characteristics |
|---|---|---|
| **Query modification** | **Transforms the view query into a query on the base tables**. The view is not stored physically | Convenient for users but inefficient for the DB system (complex views are recomputed every time) |
| **View materialization** | **Physically creates a temporary view table** when the view is first queried and keeps it for a while | Assumes more queries on the view will follow. **Extra storage space**. When defining tables change, use **incremental update** |

**When** to update a materialized view:
- **Immediate update**: as soon as the base tables change. Always up to date, but sometimes unnecessary and inefficient
- **Periodic update**: periodically. A view query may get a result that is not up to date
- **Lazy update**: when a view query needs it. Not up to date until a query arrives

If a materialized view is not queried for a certain period, it is removed and recomputed from scratch when needed later.

## Updating views {#view-update}

Retrieval from a view is always possible, but INSERT/DELETE/UPDATE is impossible in many cases.

**A view is updatable when the view update corresponds to exactly one update on the base relations.**
- **Single table + no aggregates** → maps to one base-table update → **allowed**. But the view's attributes must include (1) the base relation's **PK** and (2) **all NOT NULL attributes** without a DEFAULT (when inserting a tuple through the view those values cannot be empty)
- **Join (multiple tables)** → can be mapped in several ways, so **generally not updatable**
- **Grouping and aggregation** → the update **does not make sense** → **not updatable**

Example 1 (multiple interpretations): `UPDATE WORKS_ON1 SET Pname = 'ProductY' WHERE Lname = 'Smith' AND Fname = 'John' AND Pname = 'ProductX';`
- Interpretation a: change the project Smith works on → set Pno in WORKS_ON to ProductY's number (as intended)
- Interpretation b: rename 'ProductX' in PROJECT to 'ProductY' → the view result looks the same, but with a **side effect**: every tuple that worked on ProductX changes

Example 2 (impossible): `UPDATE DEPT_INFO SET Total_sal = 100000 WHERE Dname = 'Research';` → Total_sal is a **computed value** (SUM), not physically stored → meaningless

## Views for authorization {#view-auth}

Views can **hide certain attributes or tuples** from unauthorized users.
```
CREATE VIEW DEPT5EMP AS
SELECT * FROM EMPLOYEE WHERE Dno = 5;            -- restricts tuples

CREATE VIEW BASIC_EMP_DATA AS
SELECT Fname, Lname, Address FROM EMPLOYEE;      -- restricts attributes
```
- DEPT5EMP: lets the manager of department 5 see only department 5 employees. The user is granted **query privileges only on the view**, not on EMPLOYEE
- BASIC_EMP_DATA: general employees see only names and addresses

Slide Exercises 3 and 4, solutions:
```
CREATE VIEW DEPT_INFO (DeptName, MgrFname, MgrLname, MgrSalary)
AS SELECT D.Dname, E.Fname, E.Lname, E.Salary
   FROM   DEPARTMENT AS D, EMPLOYEE AS E
   WHERE  D.Mgr_ssn = E.Ssn;                      -- department and manager info

CREATE VIEW ProjectInfo (Pname, Dname, NumEmployees, TotalHours)
AS SELECT   P.Pname, D.Dname, COUNT(*), SUM(W.Hours)
   FROM     PROJECT AS P, WORKS_ON AS W, DEPARTMENT AS D
   WHERE    P.Pnumber = W.Pno AND D.Dnumber = P.Dnum
   GROUP BY P.Pnumber, P.Pname, D.Dname;          -- project summary
```
