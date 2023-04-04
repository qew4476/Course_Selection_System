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

INSERT INTO TEACHER
    VALUES('T008','王大聰');

INSERT INTO COURSE
    VALUES('AA108','財務管理','會計學系','T008');

INSERT INTO COURSE
    VALUES('AA144','高等會計學','會計學系','T008');

INSERT INTO COURSE
    VALUES('AA145','金融倫理','會計學系','T008');
INSERT INTO COURSE
    VALUES('AB102','貨幣銀行學','財務金融學系','T008');
