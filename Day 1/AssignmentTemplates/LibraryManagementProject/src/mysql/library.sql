use studentworks;

--  you can use another table name if required
create table librarybook(
    _id varchar(10) primary key not null,
    _title varchar(500),
    _author varchar(100),
    _status bool,
    _borrowedby varchar(100),
    _borroweddate date
);
