-- Tarea 1: Crear y popular la DB
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
        rent_end_date DATE DEFAULT CURRENT_DATE + INTERVAL '1 month',
        rent_devolution_date DATE DEFAULT NULL,
        rent_status VARCHAR(50) NOT NULL
        );


insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Sarina Peto', 'speto0@china.com.cn', 'speto0', 'gS3/"?1=4I', '4/25/2023', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Miran Yakobowitch', 'myakobowitch1@cnbc.com', 'myakobowitch1', 'bK7<E*\8Eq', '7/10/2021', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Emeline Sturmey', 'esturmey2@archive.org', 'esturmey2', 'sG8/|O7v$<W', '6/21/1991', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Bird Kondratovich', 'bkondratovich3@miitbeian.gov.cn', 'bkondratovich3', 'xB1/!Le*qxRU9lr', '4/30/1999', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Sib Baitman', 'sbaitman4@cmu.edu', 'sbaitman4', 'kB1*y@m1KDR$.', '9/25/2007', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Ellette Lackeye', 'elackeye5@unc.edu', 'elackeye5', 'sM8\{Ky{l9sFc+&', '7/29/2020', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Hillery Escalante', 'hescalante6@networkadvertising.org', 'hescalante6', 'jL5@@q~Bi_FccZ.', '7/17/1991', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Skelly Keslake', 'skeslake7@archive.org', 'skeslake7', 'pL5_+a9<z', '7/26/2011', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Shantee Winscum', 'swinscum8@accuweather.com', 'swinscum8', 'tQ9+}|Bn?947', '6/25/2010', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Brinn Shoutt', 'bshoutt9@51.la', 'bshoutt9', 'nM6&dlfU?_J8,m!', '12/13/2022', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Bekki Tomkys', 'btomkysa@springer.com', 'btomkysa', 'jJ0?Ev.k=JZqVLWc', '1/21/2012', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Marabel Houseago', 'mhouseagob@illinois.edu', 'mhouseagob', 'yP1`CV=klM"w!y', '4/13/2001', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Tarrah Mayall', 'tmayallc@ca.gov', 'tmayallc', 'lS7!0d?q', '4/24/2003', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Conant Blanque', 'cblanqued@webs.com', 'cblanqued', 'dX1/v!.w?kYQWyf', '11/27/1996', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Jacynth Howroyd', 'jhowroyde@issuu.com', 'jhowroyde', 'rV6%f{bl%m{~.$', '7/1/2000', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Jone Craigs', 'jcraigsf@163.com', 'jcraigsf', 'fW9+}"z"GtSzU2Q', '8/1/2011', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Georgette Assaf', 'gassafg@foxnews.com', 'gassafg', 'gW3!I*#<', '5/15/2020', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Blair Berthomieu', 'bberthomieuh@newsvine.com', 'bberthomieuh', 'sK4?B1UYxW}', '4/28/2025', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Goldarina Fairest', 'gfairesti@cbc.ca', 'gfairesti', 'wJ8*N_)d_t5*H', '6/30/1997', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Latashia Maseres', 'lmaseresj@wikia.com', 'lmaseresj', 'uV9{nEW&FTJ~J5', '7/10/2001', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Jonah Janiak', 'jjaniakk@lulu.com', 'jjaniakk', 'oC3+8N3$WZ"', '2/8/2020', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Beck Tratton', 'btrattonl@geocities.com', 'btrattonl', 'wP7(16mr|d*', '10/17/2021', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Ainslee Laweles', 'alawelesm@slashdot.org', 'alawelesm', 'lG6,J<m8s~CXc}i', '1/19/2008', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Martie Jarmain', 'mjarmainn@imgur.com', 'mjarmainn', 'xW4*/%IR1n0F', '7/19/1996', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Berkly Neggrini', 'bneggrinio@phoca.cz', 'bneggrinio', 'aS2&"V.hPTG', '5/28/1995', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Wendeline Swansborough', 'wswansboroughp@i2i.jp', 'wswansboroughp', 'xT3?1|((@', '6/9/2024', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Calypso Rampling', 'cramplingq@fotki.com', 'cramplingq', 'mA7|G\c`obqr~h`Y', '12/28/1999', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Teriann Byneth', 'tbynethr@ovh.net', 'tbynethr', 'vD1>JAUtb!jF}@I', '6/17/1991', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Kamilah Gaythor', 'kgaythors@cbsnews.com', 'kgaythors', 'rK8=?tjH$U', '4/8/2025', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Artemas Ismail', 'aismailt@diigo.com', 'aismailt', 'cI5($!}eY', '1/31/1992', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Galina Ogles', 'goglesu@ask.com', 'goglesu', 'gQ2)78nk', '10/16/2017', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Barron Yeandel', 'byeandelv@nhs.uk', 'byeandelv', 'eK7)*lE}kiu', '8/6/2020', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Allin Choak', 'achoakw@tinyurl.com', 'achoakw', 'wG4~}/#(y87<yry', '11/8/2017', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Wyn Dallow', 'wdallowx@sbwire.com', 'wdallowx', 'cU3{<HOGE.g6', '2/25/2001', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Leela Girardoni', 'lgirardoniy@icio.us', 'lgirardoniy', 'gY0\+`V`K$', '11/16/2017', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Isabel Worlidge', 'iworlidgez@reference.com', 'iworlidgez', 'oD4|HDU&>#g",=', '9/10/2000', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Indira Krojn', 'ikrojn10@eventbrite.com', 'ikrojn10', 'yZ4(ev9+mRQG{', '5/30/1990', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Granville Fisby', 'gfisby11@reddit.com', 'gfisby11', 'hM0@%gZ9bcvY$?', '11/2/2025', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Philippine Point', 'ppoint12@com.com', 'ppoint12', 'xO1>fSFtS`h', '11/1/2010', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Clara Giraux', 'cgiraux13@independent.co.uk', 'cgiraux13', 'nB5~no.qF=rD}Z', '5/18/1997', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Adler Liverock', 'aliverock14@edublogs.org', 'aliverock14', 'dJ9~=ur32cL', '5/25/1991', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Chantal Juleff', 'cjuleff15@ted.com', 'cjuleff15', 'dH5$o*6XG/zh5f', '4/11/2001', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Ayn Gomes', 'agomes16@behance.net', 'agomes16', 'hZ1,DIJ|N+*`&K|+', '3/14/2020', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Glenna Goullee', 'ggoullee17@cbsnews.com', 'ggoullee17', 'vU5!}!3S', '4/22/2006', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Codie Dalziel', 'cdalziel18@blog.com', 'cdalziel18', 'uY3`f{\g>\.D8W', '6/20/2011', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Kamilah Sandom', 'ksandom19@bing.com', 'ksandom19', 'qF2/l{RvJ', '4/17/2010', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Marsha Cressor', 'mcressor1a@wired.com', 'mcressor1a', 'rS4(s*ffFh', '1/10/1992', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Louisa Middleton', 'lmiddleton1b@free.fr', 'lmiddleton1b', 'lU8!cUz{Wb_dBD0E', '10/23/2014', 'active');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Paulie Dicke', 'pdicke1c@woothemes.com', 'pdicke1c', 'nY4%iE>pC0j)T1', '3/9/1998', 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, status) values ('Fidole Mapston', 'fmapston1d@storify.com', 'fmapston1d', 'sK8>"#4P!`wx\2', '12/18/2020', 'disabled');


insert into lyfter_car_rental.vehicles (make, model, manufacture_year, status) values ('Dodge', 'Ram Van 2500', '2/9/2012', 'available');
insert into lyfter_car_rental.vehicles (make, model, manufacture_year, status) values ('Volkswagen', 'Rabbit', '3/22/2011', 'not available');
insert into lyfter_car_rental.vehicles (make, model, manufacture_year, status) values ('Geo', 'Tracker', '2/13/1999', 'available');
insert into lyfter_car_rental.vehicles (make, model, manufacture_year, status) values ('Volvo', 'S70', '2/6/2011', 'not available');
insert into lyfter_car_rental.vehicles (make, model, manufacture_year, status) values ('Acura', 'TL', '3/14/2024', 'not available');
insert into lyfter_car_rental.vehicles (make, model, manufacture_year, status) values ('Suzuki', 'SX4', '3/5/2004', 'available');
insert into lyfter_car_rental.vehicles (make, model, manufacture_year, status) values ('Rolls-Royce', 'Phantom', '6/16/2007', 'not available');
insert into lyfter_car_rental.vehicles (make, model, manufacture_year, status) values ('Mazda', 'B-Series', '12/8/2015', 'not available');
insert into lyfter_car_rental.vehicles (make, model, manufacture_year, status) values ('Chevrolet', 'Impala', '6/21/1991', 'available');
insert into lyfter_car_rental.vehicles (make, model, manufacture_year, status) values ('Porsche', 'Boxster', '2/7/1998', 'not available');