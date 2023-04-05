CREATE TABLE Student(
    Account VARCHAR(128),
    Password VARCHAR(128),
    sId VARCHAR(128),
    sName VARCHAR(128),
    sGrade INTEGER,
    sEmail VARCHAR(128),
    identity VARCHAR(128),
    PRIMARY KEY (Account)
);
alter table Student modify sGrade varchar(38);
CREATE TABLE Course(
    cID VARCHAR(128),
    cName VARCHAR(128),
    department VARCHAR(128),
    tId VARCHAR(128),
    PRIMARY KEY (cID)
);

CREATE TABLE Teacher(
    tId VARCHAR(128),
    tName VARCHAR(128),
    PRIMARY KEY (tId)
);


# make foreign key from table course to Teacher.tId
ALTER TABLE Course ADD FOREIGN KEY (tId) REFERENCES Teacher(tId);

CREATE TABLE SeleRecord(
    Account VARCHAR(128),
    cID VARCHAR(128),
    PRIMARY KEY (Account, cID),
    FOREIGN KEY (Account) REFERENCES Student(Account),
    FOREIGN KEY (cID) REFERENCES Course(cID)
);

INSERT INTO TEACHER VALUES('T003', '楊大明');
INSERT INTO TEACHER VALUES('T004', '陳小明');
INSERT INTO TEACHER VALUES('T001', '林大章');
INSERT INTO TEACHER VALUES('T012', '張恩普');

INSERT INTO COURSE 
    VALUES('CS102', '離散數學', '資訊工程學系', 'T003');
INSERT INTO COURSE
    VALUES('CS103', '資料結構', '資訊工程學系', 'T003');
INSERT INTO COURSE
    VALUES('EE111', '電子學', '電機工程學系', 'T004');
INSERT INTO COURSE
    VALUES('EE112', '電路學', '電機工程學系', 'T004');
INSERT INTO COURSE
    VALUES('AA105', '會計學', '會計學系', 'T012');    
