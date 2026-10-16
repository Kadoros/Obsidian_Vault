@unit U6 | Relational Algebra | 6-1_relational-algebra.pdf + db-exercises Week 7
@intro σ π ρ, set operations, ×, ⋈ (theta, equi, natural), ÷, ℑ (aggregation), outer joins. The key skill is breaking a query into steps of the form "intermediate relation name ← operation". In your answers you may write words such as SELECT, PROJECT, JOIN instead of the symbols and still get credit.

@lesson L6-1 | Introduction to Relational Algebra, Query Trees | 6-1 p.3–6

## What is relational algebra? {#ra-intro}

- **Relational algebra**: a theoretical, mathematical model of "**how** to retrieve data" → **procedural**
- **SQL** is a high-level **declarative** language → it states only "**what** data is needed", without caring how it is retrieved
- The **basic set of operations** of the formal relational model. Rigorously based on mathematical concepts of sets

Why it matters:
- The **formal foundation** for relational model operations (select, project, rename, join, Cartesian product, …)
- **The basis for query processing and optimization**: it specifies the **sequence** of operations that produces the result

> Exam point: "SQL = what (declarative), relational algebra = how (procedural)". Also, relational algebra is a **closed system**: the result of every operation is again a relation.

## Query (execution) tree {#query-tree}

**Query tree**: a tree used inside the DBMS to represent a query = a relational algebra expression.
- **Leaf nodes = input relations**, **internal nodes = relational algebra operations**
- **Execution starts at the leaves and ends at the root** (executed bottom-up)
- It shows the order of operations explicitly, which makes the query easy to understand

Slide example: for every project located in 'Stafford', the project number, the controlling department number, and the department manager's last name, address and birth date
```
SELECT P.Pnumber, P.Dnum, E.Lname, E.Address, E.Bdate
FROM   PROJECT P, DEPARTMENT D, EMPLOYEE E
WHERE  P.Dnum = D.Dnumber AND D.Mgr_ssn = E.Ssn AND P.Plocation = 'Stafford';
```
Tree: (1) σ Plocation='Stafford' (P) → (2) ⋈ P.Dnum=D.Dnumber D → (3) ⋈ D.Mgr_ssn=E.Ssn E → root π Pnumber, Dnum, Lname, Address, Bdate

**Query processing**: the process of choosing a suitable execution strategy (query tree) among the possible ones. **One SQL query can have several query trees (plans)** → which one is best is query optimization (week 13).

@lesson L6-2 | Unary Operations: SELECT, PROJECT, RENAME | 6-1 p.8–15

## SELECT (σ) {#ra-select}

**σ<selection condition>(R)**: selects the **subset of tuples of a relation that satisfy the selection condition** → **horizontal filtering**.
- The condition is applied to **each tuple individually**
- The result has the **same attributes** as R → **degree of the result = degree of R**
- Condition = clauses of the form `<attribute> <comparison op> <constant>` or `<attribute> <comparison op> <attribute>`, connected by **AND, OR**
  - Comparison operators {=, <, ≤, >, ≥, ≠}. All of them for ordered values (numbers, dates); only {=, ≠} for unordered values (e.g., colors)
- e.g., σ Dno=4 (EMPLOYEE) → Zelaya, Wallace, Jabbar
- e.g., σ (Dno=4 AND Salary>25000) OR (Dno=5 AND Salary>30000) (EMPLOYEE) → Wong, Wallace, Narayan

**Properties**
- **Commutative**: σ c1(σ c2(R)) = σ c2(σ c1(R))
- A cascade of σ operations **can be combined into one** with AND: σ c1(σ c2(…σ cn(R))) = σ c1 AND c2 AND … AND cn(R)

> Trap: the relational algebra SELECT (σ) corresponds to SQL's **WHERE clause, not the SELECT clause**. `σ Dno=4 AND Salary>25000 (EMPLOYEE)` = `SELECT * FROM EMPLOYEE WHERE Dno=4 AND Salary>25000;`

## PROJECT (π) {#ra-project}

**π<attribute list>(R)**: keeps **only the desired columns** and discards the rest → **vertical filtering**.
- Degree of the result = number of attributes in the attribute list
- **Duplicate elimination**: if the attribute list contains no key (only nonkey attributes), duplicate tuples may appear, but **π removes duplicates** → the result is a **set** of distinct tuples
  - e.g., π Sex, Salary (EMPLOYEE) → **7 rows**, not 8 ((F, 25000) appears twice → once)
- SQL counterpart: the π attribute list = the **SELECT clause**. But SQL does not remove duplicates, so the exact equivalent is `SELECT DISTINCT Sex, Salary FROM EMPLOYEE;`

## RENAME (ρ) {#ra-rename}

**ρ**: renames the relation, its attributes, or both.
- ρ S(B₁, …, Bₙ)(R): both / ρ S(R): relation name only / ρ (B₁, …, Bₙ)(R): attribute names only
- Also written as an assignment: `R(First_name, Last_name, Salary) ← π Fname, Lname, Salary (TEMP)`
- In SQL, renaming is done with **AS (aliasing)**

## Sequences of operations (intermediate relations) {#ra-sequence}

Two ways to apply several operations:
- **Method 1**: name the intermediate relations to make the sequence explicit
```
DEP5_EMPS ← σ Dno=5 (EMPLOYEE)
RESULT    ← π Fname, Lname, Salary (DEP5_EMPS)
```
- **Method 2**: **nest** the operations into a single expression
```
π Fname, Lname, Salary ( σ Dno=5 (EMPLOYEE) )
```
→ Smith 30000, Wong 40000, Narayan 38000, English 25000

For complex queries it is **usually easier to break them into intermediate result relations** than to write one expression.

@lesson L6-3 | Set Operations, Cartesian Product | 6-1 p.17–22

## Union, intersection, difference {#ra-setops}

**Union R ∪ S**, **intersection R ∩ S**, **set difference R − S** (MINUS, EXCEPT). **Duplicates are eliminated** in the result.
- Applies only to **type compatible (union compatible)** relations: R(A₁…Aₙ) and S(B₁…Bₙ) have **the same number of attributes**, and **dom(Aᵢ) = dom(Bᵢ)** for all i
- Slide example: SSNs of all employees who either work in department 5 or directly supervise an employee who works in department 5
```
DEP5_EMPS ← σ Dno=5 (EMPLOYEE)
RESULT1   ← π Ssn (DEP5_EMPS)
RESULT2(Ssn) ← π Super_ssn (DEP5_EMPS)
RESULT    ← RESULT1 ∪ RESULT2
```
→ RESULT1 = {123456789, 333445555, 666884444, 453453453}, RESULT2 = {333445555, 888665555}, RESULT = 5 SSNs (333445555 only once)

**Properties**
- ∪ and ∩ are **commutative** (R ∪ S = S ∪ R) and **associative** (R ∪ (S ∪ T) = (R ∪ S) ∪ T)
- **− is not commutative**: R − S ≠ S − R (STUDENT − INSTRUCTOR differs from INSTRUCTOR − STUDENT)
- By convention, the result's attribute names are those of the **first relation**

## Cartesian product (×) {#ra-cartesian}

**R(A₁…Aₙ) × S(B₁…Bₘ) → Q(A₁…Aₙ, B₁…Bₘ)**: concatenates **every possible combination** of tuples from the two relations. Also called CROSS PRODUCT or CROSS JOIN.
- A binary set operation that applies **even when the relations are not type compatible**
- Number of attributes in the result = **n + m**, number of tuples = **|R| × |S|**
- Usually meaningless by itself → useful when **followed by a SELECT** that keeps only related tuples

Slide example: names of the dependents of female employees
```
FEMALE_EMPS       ← σ Sex='F' (EMPLOYEE)
EMPNAMES          ← π Fname, Lname, Ssn (FEMALE_EMPS)
EMP_DEPENDENTS    ← EMPNAMES × DEPENDENT              -- 3 × 7 = 21 rows (meaningless)
ACTUAL_DEPENDENTS ← σ Ssn=Essn (EMP_DEPENDENTS)
RESULT            ← π Fname, Lname, Dependent_name (ACTUAL_DEPENDENTS)
```
→ One row: Jennifer Wallace – Abner. **× followed by σ = JOIN** (next lesson).

@lesson L6-4 | JOIN, DIVISION, Complete Set | 6-1 p.24–34

## JOIN (⋈) {#ra-join}

**R ⋈<join condition> S**: combines **related tuples from two relations into single longer tuples**. The result Q(A₁…Aₙ, B₁…Bₘ) contains **only the combinations that satisfy the join condition**.
- e.g., the name of the manager of each department
```
DEPT_MGR ← DEPARTMENT ⋈ Mgr_ssn=Ssn EMPLOYEE
RESULT   ← π Dname, Lname, Fname (DEPT_MGR)
```
→ Research–Wong, Administration–Wallace, Headquarters–Borg
- **JOIN = Cartesian product + SELECT**: the two lines `EMP_DEPENDENTS ← EMPNAMES × DEPENDENT; ACTUAL ← σ Ssn=Essn (EMP_DEPENDENTS)` become the one line `ACTUAL ← EMPNAMES ⋈ Ssn=Essn DEPENDENT`

## Theta, equi and natural joins {#join-variants}

- **THETA JOIN**: a general join condition. `<condition> AND <condition> AND …`, each condition of the form **Aᵢ θ Bⱼ** (θ ∈ {=, <, ≤, >, ≥, ≠}). Only tuples satisfying all conditions
- **EQUIJOIN**: a join that uses **only =** as the comparison operator. The result has pairs of attributes with identical values (e.g., Mgr_ssn and Ssn) → one of each pair is superfluous
- **NATURAL JOIN (denoted *)**: an equijoin with **one of each pair of duplicate attributes removed**
  - The join attributes must **have the same name** in both relations. If not, **rename them first**
  - `DEPT_LOCS ← DEPARTMENT * DEPT_LOCATIONS` (Dnumber has the same name) → Dnumber appears once
  - `DEPT ← ρ (Dname, Dnum, Mgr_ssn, Mgr_start_date) (DEPARTMENT); PROJ_DEPT ← PROJECT * DEPT` (matched on Dnum)

> Trap: a natural join uses **all** attributes with the same name as join conditions. If some attributes accidentally share a name (e.g., both have Name), an unintended condition is added.

## Size of a join result {#join-size}

- **0 ≤ |R ⋈ S| ≤ |R| × |S|**
- Minimum: if no combination satisfies the join condition → an **empty relation**
- Maximum: if every combination satisfies the condition, or there is no condition → same as the **Cartesian product**
- **Join selectivity** = expected size of the join result / (|R| × |S|). Used in query optimization to estimate the cost of query plans

## DIVISION (÷) {#ra-division}

An operation for "… who do **all** …" queries. It can be expressed with basic operations but is defined separately.
- Form: **R(Z) ÷ S(X) = T(Y)**, where X ⊆ Z (the attributes of S are a subset of those of R) and **Y = Z − X**
- T contains only the Y values that **appear in R in combination with every value in S** (the denominator S restricts the numerator R)
- e.g., R(A, B) = {(a1,b1), (a2,b1), (a3,b1), (a4,b1), (a1,b2), (a3,b2), (a2,b3), (a3,b3), (a4,b3), (a1,b4), (a2,b4), (a3,b4)}, S(A) = {a1, a2, a3} → T(B) = {b1, b4}

Slide example: names of employees who work on **all** the projects that 'John Smith' works on
```
SMITH      ← σ Fname='John' AND Lname='Smith' (EMPLOYEE)
SMITH_PNOS ← π Pno (WORKS_ON ⋈ Essn=Ssn SMITH)            -- {1, 2}
SSN_PNOS   ← π Essn, Pno (WORKS_ON)
SSNS(Ssn)  ← SSN_PNOS ÷ SMITH_PNOS                         -- {123456789, 453453453}
RESULT     ← π Fname, Lname (SSNS * EMPLOYEE)
```
→ John Smith, Joyce English

> Exam point: the attribute order and names of the numerator R must line up. SSN_PNOS(Essn, Pno) ÷ SMITH_PNOS(Pno) → the remaining attribute is Essn. It was renamed to SSNS(Ssn) so the result can be natural-joined with EMPLOYEE.

## Complete set of relational algebra operations {#ra-complete}

The six operations **{σ, π, ∪, ρ, −, ×}** form a complete set. Every other (original) relational algebra operation can be expressed as a combination of these six.
- **Intersection**: R ∩ S ≡ (R ∪ S) − ((R − S) ∪ (S − R))
- **Join**: R ⋈<condition> S ≡ σ<condition>(R × S)
- **Natural join**: RENAME before a Cartesian product, then SELECT and PROJECT after it
- Strictly, ∩ and ⋈ are not needed, but they are kept as separate operations **because they are used so often**

@lesson L6-5 | Additional Operations: Aggregation, Grouping, Outer Joins | 6-1 p.36–43

## Aggregate functions and grouping (ℑ) {#ra-aggregate}

The basic operations cannot express **aggregates (SUM, AVERAGE, MAXIMUM, MINIMUM, COUNT)**, **aggregates per group**, or **outer joins** → additional operations **enhance the expressive power**.

**<grouping attributes> ℑ <function list> (R)** (ℑ = script F)
- Grouping attributes: attributes of R used to form groups (may be omitted)
- Function list: pairs (<function> <attribute>). Function = SUM, AVERAGE, MAXIMUM, MINIMUM, COUNT
- **Result**: the grouping attributes + one attribute per element of the function list

Example
```
ρ R(Dno, No_of_employees, Average_sal) ( Dno ℑ COUNT Ssn, AVERAGE Salary (EMPLOYEE) )
```
→ (5, 4, 33250), (4, 3, 31000), (1, 1, 55000)
- **Without renaming**: attribute names = `<function>_<attribute>` → Dno, Count_ssn, Average_salary
- **Without grouping attributes**: the functions apply to **all tuples** → the result is **a single tuple**: `ℑ COUNT Ssn, AVERAGE Salary (EMPLOYEE)` → (8, 35125)

## Properties of aggregation {#ra-agg-props}

- **Duplicates are not eliminated** when an aggregate function is applied (so that sums and averages of salaries come out right)
- **NULL values are not considered** in aggregation
- Relational algebra is a **closed mathematical system**: an aggregate result is also a **relation**, not a scalar number (even with one value in one tuple)

## Outer joins {#ra-outer}

EQUIJOIN and NATURAL JOIN (inner joins) keep **only tuples that satisfy the condition** and drop tuples without a match. Use an outer join **when you want to keep all tuples of one (or both) relations** even without a match.
- e.g., all employee names, plus the name of the department each one manages if they manage one (NULL if not)
```
TEMP   ← EMPLOYEE ⟕ Ssn=Mgr_ssn DEPARTMENT
RESULT ← π Fname, Minit, Lname, Dname (TEMP)
```
→ 8 rows. Wong–Research, Wallace–Administration, Borg–Headquarters; the other 5 have Dname = NULL
- Kinds: **LEFT OUTER JOIN ⟕** (all tuples on the left), **RIGHT OUTER JOIN ⟖** (all tuples on the right), **FULL OUTER JOIN ⟗** (both). Attributes of the unmatched side are **padded with NULL**

@lesson L6-6 | Relational Algebra Writing Practice | db-exercises Week 7 (p.55–59)

## Exercises 1–2: join paths {#ra-practice-join}

**Exercise 1**: the name and address of all employees who work for the 'Research' department
```
RESEARCH_DEPT ← σ Dname='Research' (DEPARTMENT)
RESEARCH_EMPS ← RESEARCH_DEPT ⋈ Dnumber=Dno EMPLOYEE
RESULT        ← π Fname, Lname, Address (RESEARCH_EMPS)
```
**Exercise 2**: for every project located in 'Stafford', the project number, the controlling department number, and the manager's last name, address and birth date
```
STAFFORD_PROJS ← σ Plocation='Stafford' (PROJECT)
CONTR_DEPTS    ← STAFFORD_PROJS ⋈ Dnum=Dnumber DEPARTMENT
PROJ_DEPT_MGRS ← CONTR_DEPTS ⋈ Mgr_ssn=Ssn EMPLOYEE
RESULT         ← π Pnumber, Dnum, Lname, Address, Bdate (PROJ_DEPT_MGRS)
```
→ (10, 4, Wallace, 291 Berry, Bellaire, TX, 1941-06-20), (30, 4, Wallace, …)

Tip: apply **σ first** to the relation that has the condition → follow FK–PK links with **⋈** → finish with **π**.

## Exercise 3: union {#ra-practice-union}

Project numbers of projects that involve an employee whose last name is 'Smith', either as a worker or as a manager of the department that controls the project
```
SMITHS(Essn)        ← π Ssn (σ Lname='Smith' (EMPLOYEE))
SMITH_WORKER_PROJS  ← π Pno (WORKS_ON * SMITHS)
MGRS                ← π Lname, Dnumber (EMPLOYEE ⋈ Ssn=Mgr_ssn DEPARTMENT)
SMITH_MANAGED_DEPTS(Dnum) ← π Dnumber (σ Lname='Smith' (MGRS))
SMITH_MGR_PROJS(Pno)      ← π Pnumber (SMITH_MANAGED_DEPTS * PROJECT)
RESULT              ← SMITH_WORKER_PROJS ∪ SMITH_MGR_PROJS
```
- The two results' attribute names are **both made Pno** so ∪ can be applied (type compatibility)
- Renaming to SMITHS(Essn) makes the **natural join** with WORKS_ON match on Essn

## Exercises 4–5: difference and intersection {#ra-practice-diff}

**Exercise 4**: names of employees who have **no** dependents
```
ALL_EMPS             ← π Ssn (EMPLOYEE)
EMPS_WITH_DEPS(Ssn)  ← π Essn (DEPENDENT)
EMPS_WITHOUT_DEPS    ← ALL_EMPS − EMPS_WITH_DEPS
RESULT               ← π Lname, Fname (EMPS_WITHOUT_DEPS * EMPLOYEE)
```
**Exercise 5**: names of **managers who have at least one dependent**
```
MGRS(Ssn)            ← π Mgr_ssn (DEPARTMENT)
EMPS_WITH_DEPS(Ssn)  ← π Essn (DEPENDENT)
MGRS_WITH_DEPS       ← MGRS ∩ EMPS_WITH_DEPS
RESULT               ← π Lname, Fname (MGRS_WITH_DEPS * EMPLOYEE)
```
→ Wong, Wallace

> Exam point: "has no …" = **difference (−)**, "A and also B" = **intersection (∩)**, "A or B" = **union (∪)**, "all …" = **division (÷)**. Memorize them as one-to-one counterparts of SQL's NOT EXISTS / EXISTS AND EXISTS / UNION / NOT EXISTS (EXCEPT).
