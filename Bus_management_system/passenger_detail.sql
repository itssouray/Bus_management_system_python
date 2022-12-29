create table passenger_detail(
passenger_id varchar2(5) primary key,
passenger_name varchar2(30) NOT NULL,
passenger_age number NOT NULL,
gender varchar2(6) NOT NULL,
passenger_contact number(12) NOT NULL,
bus_no number NOT NULL,
ticket_no number NOT NULL,
FOREIGN KEY(bus_no) REFERENCES bus_detail(bus_no),
FOREIGN KEY(ticket_no) REFERENCES ticket_detail(ticket_no)
)