# 교재(Elmasri 7판) COMPANY 그림 5.6 · UNIVERSITY 그림 1.2 상태를 SQLite로 올려서 SQL 정답을 실제로 돌려본다.
import sqlite3

COMPANY_DDL = """
CREATE TABLE EMPLOYEE (Fname TEXT, Minit TEXT, Lname TEXT, Ssn TEXT PRIMARY KEY, Bdate TEXT, Address TEXT,
  Sex TEXT, Salary INT, Super_ssn TEXT, Dno INT);
CREATE TABLE DEPARTMENT (Dname TEXT UNIQUE, Dnumber INT PRIMARY KEY, Mgr_ssn TEXT, Mgr_start_date TEXT);
CREATE TABLE DEPT_LOCATIONS (Dnumber INT, Dlocation TEXT, PRIMARY KEY (Dnumber, Dlocation));
CREATE TABLE PROJECT (Pname TEXT UNIQUE, Pnumber INT PRIMARY KEY, Plocation TEXT, Dnum INT);
CREATE TABLE WORKS_ON (Essn TEXT, Pno INT, Hours REAL, PRIMARY KEY (Essn, Pno));
CREATE TABLE DEPENDENT (Essn TEXT, Dependent_name TEXT, Sex TEXT, Bdate TEXT, Relationship TEXT,
  PRIMARY KEY (Essn, Dependent_name));
"""
EMPLOYEE = [
 ("John","B","Smith","123456789","1965-01-09","731 Fondren, Houston, TX","M",30000,"333445555",5),
 ("Franklin","T","Wong","333445555","1955-12-08","638 Voss, Houston, TX","M",40000,"888665555",5),
 ("Alicia","J","Zelaya","999887777","1968-01-19","3321 Castle, Spring, TX","F",25000,"987654321",4),
 ("Jennifer","S","Wallace","987654321","1941-06-20","291 Berry, Bellaire, TX","F",43000,"888665555",4),
 ("Ramesh","K","Narayan","666884444","1962-09-15","975 Fire Oak, Humble, TX","M",38000,"333445555",5),
 ("Joyce","A","English","453453453","1972-07-31","5631 Rice, Houston, TX","F",25000,"333445555",5),
 ("Ahmad","V","Jabbar","987987987","1969-03-29","980 Dallas, Houston, TX","M",25000,"987654321",4),
 ("James","E","Borg","888665555","1937-11-10","450 Stone, Houston, TX","M",55000,None,1),
]
DEPARTMENT = [("Research",5,"333445555","1988-05-22"),("Administration",4,"987654321","1995-01-01"),
 ("Headquarters",1,"888665555","1981-06-19")]
DEPT_LOCATIONS = [(1,"Houston"),(4,"Stafford"),(5,"Bellaire"),(5,"Sugarland"),(5,"Houston")]
PROJECT = [("ProductX",1,"Bellaire",5),("ProductY",2,"Sugarland",5),("ProductZ",3,"Houston",5),
 ("Computerization",10,"Stafford",4),("Reorganization",20,"Houston",1),("Newbenefits",30,"Stafford",4)]
WORKS_ON = [("123456789",1,32.5),("123456789",2,7.5),("666884444",3,40.0),("453453453",1,20.0),("453453453",2,20.0),
 ("333445555",2,10.0),("333445555",3,10.0),("333445555",10,10.0),("333445555",20,10.0),("999887777",30,30.0),
 ("999887777",10,10.0),("987987987",10,35.0),("987987987",30,5.0),("987654321",30,20.0),("987654321",20,15.0),
 ("888665555",20,None)]
DEPENDENT = [("333445555","Alice","F","1986-04-05","Daughter"),("333445555","Theodore","M","1983-10-25","Son"),
 ("333445555","Joy","F","1958-05-03","Spouse"),("987654321","Abner","M","1942-02-28","Spouse"),
 ("123456789","Michael","M","1988-01-04","Son"),("123456789","Alice","F","1988-12-30","Daughter"),
 ("123456789","Elizabeth","F","1967-05-05","Spouse")]

UNIV_DDL = """
CREATE TABLE STUDENT (Name TEXT, Student_number INT PRIMARY KEY, Class INT, Major TEXT);
CREATE TABLE COURSE (Course_name TEXT, Course_number TEXT PRIMARY KEY, Credit_hours INT, Department TEXT);
CREATE TABLE SECTION (Section_identifier INT PRIMARY KEY, Course_number TEXT, Semester TEXT, Year TEXT, Instructor TEXT);
CREATE TABLE GRADE_REPORT (Student_number INT, Section_identifier INT, Grade TEXT, PRIMARY KEY (Student_number, Section_identifier));
CREATE TABLE PREREQUISITE (Course_number TEXT, Prerequisite_number TEXT, PRIMARY KEY (Course_number, Prerequisite_number));
"""
STUDENT = [("Smith",17,1,"CS"),("Brown",8,2,"CS")]
COURSE = [("Intro to Computer Science","CS1310",4,"CS"),("Data Structures","CS3320",4,"CS"),
 ("Discrete Mathematics","MATH2410",3,"MATH"),("Database","CS3380",3,"CS")]
SECTION = [(85,"MATH2410","Fall","07","King"),(92,"CS1310","Fall","07","Anderson"),(102,"CS3320","Spring","08","Knuth"),
 (112,"MATH2410","Fall","08","Chang"),(119,"CS1310","Fall","08","Anderson"),(135,"CS3380","Fall","08","Stone")]
GRADE_REPORT = [(17,112,"B"),(17,119,"C"),(8,85,"A"),(8,92,"A"),(8,102,"B"),(8,135,"A")]
PREREQUISITE = [("CS3380","CS3320"),("CS3380","MATH2410"),("CS3320","CS1310")]

def _load(con, ddl, tables):
    con.executescript(ddl)
    for name, rows in tables.items():
        con.executemany(f"INSERT INTO {name} VALUES ({','.join('?'*len(rows[0]))})", rows)

def company():
    con = sqlite3.connect(":memory:")
    _load(con, COMPANY_DDL, dict(EMPLOYEE=EMPLOYEE, DEPARTMENT=DEPARTMENT, DEPT_LOCATIONS=DEPT_LOCATIONS,
        PROJECT=PROJECT, WORKS_ON=WORKS_ON, DEPENDENT=DEPENDENT))
    return con

def university():
    con = sqlite3.connect(":memory:")
    _load(con, UNIV_DDL, dict(STUDENT=STUDENT, COURSE=COURSE, SECTION=SECTION, GRADE_REPORT=GRADE_REPORT,
        PREREQUISITE=PREREQUISITE))
    return con

def run(sql, db="company"):
    con = company() if db == "company" else university()
    cur = con.execute(sql)
    cols = [d[0] for d in cur.description]
    return cols, cur.fetchall()

def fmt(cols, rows):
    """결과를 짧은 표 텍스트로"""
    def v(x):
        if x is None: return "NULL"
        if isinstance(x, float) and x == int(x): return str(int(x))
        if isinstance(x, float): return f"{x:.2f}".rstrip("0").rstrip(".")
        return str(x)
    out = [" | ".join(cols)] + [" | ".join(v(x) for x in r) for r in rows]
    return "\n".join(out)

# 문제에 붙이는 스키마 요약
COMPANY_SCHEMA = """EMPLOYEE(Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno)
DEPARTMENT(Dname, Dnumber, Mgr_ssn, Mgr_start_date)
DEPT_LOCATIONS(Dnumber, Dlocation)
PROJECT(Pname, Pnumber, Plocation, Dnum)
WORKS_ON(Essn, Pno, Hours)
DEPENDENT(Essn, Dependent_name, Sex, Bdate, Relationship)
PK: Ssn / Dnumber / (Dnumber, Dlocation) / Pnumber / (Essn, Pno) / (Essn, Dependent_name)
FK: Super_ssn→EMPLOYEE, Dno→DEPARTMENT, Mgr_ssn→EMPLOYEE, Dnum→DEPARTMENT,
    WORKS_ON.Essn→EMPLOYEE, Pno→PROJECT, DEPENDENT.Essn→EMPLOYEE"""
UNIV_SCHEMA = """STUDENT(Name, Student_number, Class, Major)
COURSE(Course_name, Course_number, Credit_hours, Department)
SECTION(Section_identifier, Course_number, Semester, Year, Instructor)
GRADE_REPORT(Student_number, Section_identifier, Grade)
PREREQUISITE(Course_number, Prerequisite_number)"""

if __name__ == "__main__":
    print(fmt(*run("SELECT COUNT(DISTINCT Salary) FROM EMPLOYEE")))
    print(fmt(*run("SELECT COUNT(*) FROM EMPLOYEE E, DEPARTMENT D WHERE E.Dno=D.Dnumber AND D.Dname='Research'")))
