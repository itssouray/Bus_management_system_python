create table ticket_detail(
ticket_no number primary key,
seat_no number NOT NULL,
seat_type varchar2(10) NOT NULL,
price number NOT NULL
)