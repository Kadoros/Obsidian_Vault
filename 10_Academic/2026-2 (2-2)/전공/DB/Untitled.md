---
tags:
  - note
parent_concept:
---
COLLAGE(CName=pk, COffice, CPhone, Id=fk)
INSTRUCTOR(Id=pk, Rank, IName, IOffice, IPhone, DName=cfk,DCode=cfk)
DEPT(DName=cpk,DCode=cpk, DOffice, DPhone, CName=fk, Id=fk,CStartDay)
STUDENT(Sid=pk, DOB, FName, MName, LName, Addr, Phone, Major,Dname=cfk,Dcode=cfk)
COURSE(CCode=cpk, CoName=cpk, Credits, CDesc, Level, Dname=cfk,DCode=cfk)
SECTION(SecId=pk, SecNo,Sem, Year, Bidg, RoomNo,DaysTime, Id=fk, CCode=cfk, CoName=cfk)

TAKES(Sid=cpk,cfk, SecId=cpk,cfk ,GRADE)
