CREATE TABLE lyfter_car_rental.users(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL,
        birthday TEXT NOT NULL,
        status VARCHAR(50) NOT NULL
        );


CREATE TABLE lyfter_car_rental.vehicles(
        id SERIAL PRIMARY KEY,
        make VARCHAR(50) NOT NULL,
        model VARCHAR(50) NOT NULL,
        manufacture_year TEXT NOT NULL,
        status VARCHAR(50) NOT NULL
        );


CREATE TABLE lyfter_car_rental.users_vehicles(
        id SERIAL PRIMARY KEY,
        user_id INT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES lyfter_car_rental.users(id),
        vehicle_id INT NOT NULL,
        FOREIGN KEY (vehicle_id) REFERENCES lyfter_car_rental.vehicles(id),
        rent_date DATE DEFAULT CURRENT_DATE,
        rent_status VARCHAR(50) NOT NULL
        );


insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (1, 'Sarina Peto', 'speto0@china.com.cn', 'speto0', 'gS3/"?1=4I', '4/25/2023', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (2, 'Miran Yakobowitch', 'myakobowitch1@cnbc.com', 'myakobowitch1', 'bK7<E*\8E''q', '7/10/2021', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (3, 'Emeline Sturmey', 'esturmey2@archive.org', 'esturmey2', 'sG8/|O7v$<W', '6/21/1991', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (4, 'Bird Kondratovich', 'bkondratovich3@miitbeian.gov.cn', 'bkondratovich3', 'xB1/!Le*qxRU9lr', '4/30/1999', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (5, 'Sib Baitman', 'sbaitman4@cmu.edu', 'sbaitman4', 'kB1*y@m1KDR$.', '9/25/2007', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (6, 'Ellette Lackeye', 'elackeye5@unc.edu', 'elackeye5', 'sM8\{Ky{l9sFc+&', '7/29/2020', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (7, 'Hillery Escalante', 'hescalante6@networkadvertising.org', 'hescalante6', 'jL5@@q~Bi_FccZ.', '7/17/1991', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (8, 'Skelly Keslake', 'skeslake7@archive.org', 'skeslake7', 'pL5_+a9<z', '7/26/2011', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (9, 'Shantee Winscum', 'swinscum8@accuweather.com', 'swinscum8', 'tQ9+}|Bn?947', '6/25/2010', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (10, 'Brinn Shoutt', 'bshoutt9@51.la', 'bshoutt9', 'nM6&dlfU?_J8,m!', '12/13/2022', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (11, 'Bekki Tomkys', 'btomkysa@springer.com', 'btomkysa', 'jJ0?Ev.k=JZqVLWc', '1/21/2012', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (12, 'Marabel Houseago', 'mhouseagob@illinois.edu', 'mhouseagob', 'yP1`CV=klM"w!y', '4/13/2001', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (13, 'Tarrah Mayall', 'tmayallc@ca.gov', 'tmayallc', 'lS7!0d?q', '4/24/2003', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (14, 'Conant Blanque', 'cblanqued@webs.com', 'cblanqued', 'dX1/v!.w?kYQWyf', '11/27/1996', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (15, 'Jacynth Howroyd', 'jhowroyde@issuu.com', 'jhowroyde', 'rV6%f{bl%m{~.$', '7/1/2000', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (16, 'Jone Craigs', 'jcraigsf@163.com', 'jcraigsf', 'fW9+}"z"GtSzU2Q', '8/1/2011', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (17, 'Georgette Assaf', 'gassafg@foxnews.com', 'gassafg', 'gW3!I*#<', '5/15/2020', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (18, 'Blair Berthomieu', 'bberthomieuh@newsvine.com', 'bberthomieuh', 'sK4?B1UYxW}', '4/28/2025', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (19, 'Goldarina Fairest', 'gfairesti@cbc.ca', 'gfairesti', 'wJ8*N_)d_t5*H', '6/30/1997', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (20, 'Latashia Maseres', 'lmaseresj@wikia.com', 'lmaseresj', 'uV9{nEW&FTJ~J5', '7/10/2001', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (21, 'Jonah Janiak', 'jjaniakk@lulu.com', 'jjaniakk', 'oC3+8N3$WZ"', '2/8/2020', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (22, 'Beck Tratton', 'btrattonl@geocities.com', 'btrattonl', 'wP7(16mr|d*', '10/17/2021', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (23, 'Ainslee Laweles', 'alawelesm@slashdot.org', 'alawelesm', 'lG6,J<m8s~CXc}i', '1/19/2008', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (24, 'Martie Jarmain', 'mjarmainn@imgur.com', 'mjarmainn', 'xW4*/%IR1n0F', '7/19/1996', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (25, 'Berkly Neggrini', 'bneggrinio@phoca.cz', 'bneggrinio', 'aS2&"V.hPTG', '5/28/1995', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (26, 'Wendeline Swansborough', 'wswansboroughp@i2i.jp', 'wswansboroughp', 'xT3?1|((@', '6/9/2024', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (27, 'Calypso Rampling', 'cramplingq@fotki.com', 'cramplingq', 'mA7|G\c`obqr~h`Y', '12/28/1999', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (28, 'Teriann Byneth', 'tbynethr@ovh.net', 'tbynethr', 'vD1>JAUtb!jF}@I', '6/17/1991', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (29, 'Kamilah Gaythor', 'kgaythors@cbsnews.com', 'kgaythors', 'rK8=?tjH$U', '4/8/2025', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (30, 'Artemas Ismail', 'aismailt@diigo.com', 'aismailt', 'cI5(''$!}eY', '1/31/1992', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (31, 'Galina Ogles', 'goglesu@ask.com', 'goglesu', 'gQ2)78nk', '10/16/2017', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (32, 'Barron Yeandel', 'byeandelv@nhs.uk', 'byeandelv', 'eK7)*lE}kiu', '8/6/2020', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (33, 'Allin Choak', 'achoakw@tinyurl.com', 'achoakw', 'wG4~}/#(y87<yry', '11/8/2017', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (34, 'Wyn Dallow', 'wdallowx@sbwire.com', 'wdallowx', 'cU3{<HOGE.g6', '2/25/2001', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (35, 'Leela Girardoni', 'lgirardoniy@icio.us', 'lgirardoniy', 'gY0\+`V`K$', '11/16/2017', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (36, 'Isabel Worlidge', 'iworlidgez@reference.com', 'iworlidgez', 'oD4|HDU&>#g",=', '9/10/2000', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (37, 'Indira Krojn', 'ikrojn10@eventbrite.com', 'ikrojn10', 'yZ4(ev9+mRQG{', '5/30/1990', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (38, 'Granville Fisby', 'gfisby11@reddit.com', 'gfisby11', 'hM0@%gZ9bcvY$?', '11/2/2025', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (39, 'Philippine Point', 'ppoint12@com.com', 'ppoint12', 'xO1>fSFtS`h', '11/1/2010', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (40, 'Clara Giraux', 'cgiraux13@independent.co.uk', 'cgiraux13', 'nB5~no.qF=rD}Z', '5/18/1997', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (41, 'Adler Liverock', 'aliverock14@edublogs.org', 'aliverock14', 'dJ9~=ur32cL', '5/25/1991', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (42, 'Chantal Juleff', 'cjuleff15@ted.com', 'cjuleff15', 'dH5$o*6XG/zh5f''', '4/11/2001', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (43, 'Ayn Gomes', 'agomes16@behance.net', 'agomes16', 'hZ1,DIJ|N+*`&K|+', '3/14/2020', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (44, 'Glenna Goullee', 'ggoullee17@cbsnews.com', 'ggoullee17', 'vU5!}!3S', '4/22/2006', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (45, 'Codie Dalziel', 'cdalziel18@blog.com', 'cdalziel18', 'uY3`f{\g>\.D8W', '6/20/2011', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (46, 'Kamilah Sandom', 'ksandom19@bing.com', 'ksandom19', 'qF2/l{RvJ', '4/17/2010', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (47, 'Marsha Cressor', 'mcressor1a@wired.com', 'mcressor1a', 'rS4(s*ffFh', '1/10/1992', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (48, 'Louisa Middleton', 'lmiddleton1b@free.fr', 'lmiddleton1b', 'lU8!cUz{Wb_dBD0E', '10/23/2014', true);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (49, 'Paulie Dicke', 'pdicke1c@woothemes.com', 'pdicke1c', 'nY4%iE>pC0j)T1', '3/9/1998', false);
insert into lyfter_car_rental.users (id, name, email, username, password, birthday, status) values (50, 'Fidole Mapston', 'fmapston1d@storify.com', 'fmapston1d', 'sK8>"#4P!`wx\2', '12/18/2020', false);


insert into lyfter_car_rental.vehicles (id, make, model, manufacture_year, status) values (1, 'Dodge', 'Ram Van 2500', '2/9/2012', true);
insert into lyfter_car_rental.vehicles (id, make, model, manufacture_year, status) values (2, 'Volkswagen', 'Rabbit', '3/22/2011', false);
insert into lyfter_car_rental.vehicles (id, make, model, manufacture_year, status) values (3, 'Geo', 'Tracker', '2/13/1999', true);
insert into lyfter_car_rental.vehicles (id, make, model, manufacture_year, status) values (4, 'Volvo', 'S70', '2/6/2011', false);
insert into lyfter_car_rental.vehicles (id, make, model, manufacture_year, status) values (5, 'Acura', 'TL', '3/14/2024', false);
insert into lyfter_car_rental.vehicles (id, make, model, manufacture_year, status) values (6, 'Suzuki', 'SX4', '3/5/2004', true);
insert into lyfter_car_rental.vehicles (id, make, model, manufacture_year, status) values (7, 'Rolls-Royce', 'Phantom', '6/16/2007', false);
insert into lyfter_car_rental.vehicles (id, make, model, manufacture_year, status) values (8, 'Mazda', 'B-Series', '12/8/2015', false);
insert into lyfter_car_rental.vehicles (id, make, model, manufacture_year, status) values (9, 'Chevrolet', 'Impala', '6/21/1991', true);
insert into lyfter_car_rental.vehicles (id, make, model, manufacture_year, status) values (10, 'Porsche', 'Boxster', '2/7/1998', true);