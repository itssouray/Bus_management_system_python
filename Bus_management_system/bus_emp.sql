create table bus_emp(
driver_id varchar(10) primary key,
driver_name varchar(20) NOT NULL,
contact_no number NOT NULL,
bus_no number NOT NULL,
FOREIGN KEY(bus_no) REFERENCES bus_detail(bus_no)
)
