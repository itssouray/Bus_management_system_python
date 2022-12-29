create table journy_detail(
boarding_date date NOT NULL,
boarding_time varchar2(10) NOT NULL,
boarding_point varchar2(30) NOT NULL,
destination_time varchar2(10) NOT NULL,
destination_point varchar(30) NOT NULL,
bus_NO number NOT NULL,
FOREIGN KEY (bus_no) REFERENCES bus_detail(bus_no)
)