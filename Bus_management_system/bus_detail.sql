create table bus_detail(
bus_no number primary key,
bus_name varchar2(30) NOT NULL ,
bus_type varchar2(10) NOT NULL ,
total_seat number NOT NULL ,
avalable_seat number NOT NULL 
)