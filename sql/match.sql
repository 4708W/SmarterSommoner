create table idx (
    date date,
    puuid text,
    mid text primary key
);
-- consier create index

create table match(
    mid text primary key,
    puuid text,
    win bool
);

create table player(
    puuid text primary key,
    username text
);

-- one time insertion
insert into player (username, puuid)
values
    ('SchroDog2', 'HYPlbJR5hooJDwDwjqcQPaLSDlPAa-ZFbbfzaEt5NIpsQvV8RIgp9WlMltxreGrp5cK-eWNwGaTn-g'),
    ('SchroDog0', 'J7WSv-RlRnmj0Ch5B7iP4GzIYinMH9TX3voHayXAdATnEbCJ8s0E69HW9_mLfaaMitJY1PbtHAhGEg'),
    ('zhizhiya', '-8vWm4cLAc0lp7ogJwMQ-smWvwdz72EbQcjXcugbnqEjHQihCWD_usYI7pKjjK017jo1wE4ehykUsA'),
    ('n00bsucker', 'HkNb3Q8q_zl0yBsF0YDN2eP5tF3vIiHIn7RIqPqOZ4Y5BQpqAvtMl7pJKZ1TDDqjJcQ_qlHVmpzD2A'),
    ('ZDark Laps', 'ahD3PvDw2LL0bm9dQ13wQpgzl0AIiN7_zhGGjyN6hDySeHvg_lE1Tu2IuN093wPBnEarE-iiq3JXsw'),
    ('MeiYangYangg', 'bYcBZ6DSY0vAUpBUlZEiESjxNgYl18kLvcz8njbjdLy5Uvw6qWLrLfqYkmKlHqalqUVjk9yS0dUUOg'),
    ('futehanmu', 'WOPUPIK4Y-aWULbDSwYf05RfMU1mL1xvDrbRj5p-LQidAi6RshaEEpUfkZZF53P1hrbjj0EDuz7BUA'),
    ('Savertonight', 's2RHeDx2xJTfyOEr64Jol5ag5bw_zjjIGXRPQa5i-JqFVz7QE09QFKUJPD7_KbwUQJapwxHWXsh9vQ'),
    ('YouShould NoMe', 'thqoK1jBnX3sPKrDRcPfcXhvWH8SsDUKhojfxOZ5s1K3l6hLxVfG78V_2qEpma-D83_yzRBr888byg'),
    ('SchroDog1', 'tGJJAFMJcwwqhyFvgSAi6u3vgB7SUdyQcutd9WIFAQ4az3sBkufI9yYzoikii3fdIC6dcUuURTKKsA')
;
