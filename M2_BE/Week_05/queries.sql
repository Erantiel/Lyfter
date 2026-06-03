-- Tarea 1: Crear y popular la DB
CREATE TABLE lyfter_car_rental.users(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL,
        birthday TEXT NOT NULL,
        overdue BOOLEAN DEFAULT false,
        status VARCHAR(50) DEFAULT 'active'
        );


CREATE TABLE lyfter_car_rental.vehicles(
        id SERIAL PRIMARY KEY,
        make VARCHAR(50) NOT NULL,
        model VARCHAR(50) NOT NULL,
        manufacture_year TEXT NOT NULL,
        status VARCHAR(50) DEFAULT 'active'
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
        status VARCHAR(50) DEFAULT 'rented'
        );


insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Herbie Drakeford', 'hdrakeford0@about.me', 'hdrakeford0', 'zF0)02`V@zS7Pz', '3/31/2025', false);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Allison Gashion', 'agashion1@comcast.net', 'agashion1', 'nV2\A"zo7', '1/31/2014', false);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Conan Kubatsch', 'ckubatsch2@cisco.com', 'ckubatsch2', 'tO8$\,(OU<mN', '1/29/2017', false, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Quinlan Draye', 'qdraye3@4shared.com', 'qdraye3', 'aV0=Ygey', '6/9/1997', true);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Perri Lott', 'plott4@blogger.com', 'plott4', 'uU3|5t#v+iT', '8/18/2018', true, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Suellen Whiteside', 'swhiteside5@blog.com', 'swhiteside5', 'xE0"M5v~!GRBy', '5/19/1994', false);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Lainey Kemston', 'lkemston6@mozilla.com', 'lkemston6', 'lX3?>w?%,7C}&B', '10/3/1998', false, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Yvon Laterza', 'ylaterza7@cargocollective.com', 'ylaterza7', 'mJ1"Oj*W=oCCrTJG', '1/31/2007', true, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Stanwood Schinetti', 'sschinetti8@ustream.tv', 'sschinetti8', 'dO8/Obx?', '9/6/2005', false, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Alla Rudinger', 'arudinger9@walmart.com', 'arudinger9', 'fJ3(BB''JJ@m_/7rC', '9/16/1999', false, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Clarita McOrkill', 'cmcorkilla@globo.com', 'cmcorkilla', 'nF4_R)Pt8h', '10/20/1993', true, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Thaxter Moyer', 'tmoyerb@dot.gov', 'tmoyerb', 'mV0+@Gx`&lVr/OF`', '6/27/2015', true);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Tamera Glacken', 'tglackenc@blogspot.com', 'tglackenc', 'lS2+~W)p~`E3Pn', '9/17/2021', false);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Bryce Roseborough', 'broseboroughd@marriott.com', 'broseboroughd', 'eQ5(.E6s`', '5/17/2023', false);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Odell Dunlop', 'odunlope@virginia.edu', 'odunlope', 'jG8%A$vB%?T&Q', '4/4/2003', false);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Zia Belbin', 'zbelbinf@techcrunch.com', 'zbelbinf', 'tM3$/gR_a$W`+H', '12/6/2000', true);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Eleni Gettone', 'egettoneg@nbcnews.com', 'egettoneg', 'dZ5\u?MK{2Rg)~', '6/14/2013', true);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Pearce Ferran', 'pferranh@japanpost.jp', 'pferranh', 'kU8''U+IY4wvBFwJ', '2/20/2009', true);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Maurine Skeermor', 'mskeermori@netvibes.com', 'mskeermori', 'zN3''~<_`y', '9/2/1993', true);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Tootsie McEneny', 'tmcenenyj@netscape.com', 'tmcenenyj', 'nM4'',Vrb', '2/12/2007', true, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Philis Conrart', 'pconrartk@berkeley.edu', 'pconrartk', 'aQ8.IL*H$Cs%1W', '1/29/2009', false);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Desmond Eayres', 'deayresl@privacy.gov.au', 'deayresl', 'qZ1#`XN$m*n_/', '9/30/1990', false);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Claudette Galiero', 'cgalierom@youtube.com', 'cgalierom', 'bT9~WpbO', '10/9/2020', false);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Margy Drewitt', 'mdrewittn@friendfeed.com', 'mdrewittn', 'qZ0%G?_g(?g4', '8/1/2015', true, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Abigael Janz', 'ajanzo@xinhuanet.com', 'ajanzo', 'aX1%DY=K}C@?', '1/14/2008', false);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Bryant Gurnay', 'bgurnayp@utexas.edu', 'bgurnayp', 'oL8{s(h34!,oMYyn', '6/2/2006', false, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Vicki Coast', 'vcoastq@php.net', 'vcoastq', 'lZ2@!Vyho''H7', '7/22/1995', true);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Darleen Schowenburg', 'dschowenburgr@macromedia.com', 'dschowenburgr', 'bK9!24Sz_ai', '1/11/1994', false, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Beitris Trevarthen', 'btrevarthens@springer.com', 'btrevarthens', 'mH9{E8)BHl.*', '7/5/2021', true, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Valentina Dany', 'vdanyt@google.es', 'vdanyt', 'lT9"T1~8Ht7%#', '9/9/2017', true);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Stanislas Geke', 'sgekeu@desdev.cn', 'sgekeu', 'iZ4\J|)SzY%~\', '10/9/1991', false);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Dmitri Avrahamoff', 'davrahamoffv@icio.us', 'davrahamoffv', 'oB1%&w=''0s', '12/13/2001', true);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Almire Rowlatt', 'arowlattw@sciencedirect.com', 'arowlattw', 'aH5|H>(QzD(8hMW', '1/28/1996', false);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Hussein Redborn', 'hredbornx@timesonline.co.uk', 'hredbornx', 'jH9$2dhR', '4/23/2020', false);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Sybyl Hussey', 'shusseyy@europa.eu', 'shusseyy', 'mN5!A}K*aJ|FiT', '5/17/2025', true, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Boigie De Gowe', 'bdez@mashable.com', 'bdez', 'tL2&t|35', '1/25/2009', true);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Zelda Sexstone', 'zsexstone10@cdc.gov', 'zsexstone10', 'dF8*qrNw41Zh9k@O', '10/4/2015', true);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Jackie Spellesy', 'jspellesy11@harvard.edu', 'jspellesy11', 'rP8{|hf>a4@?RDC', '12/30/2002', false, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Bayard Goggan', 'bgoggan12@latimes.com', 'bgoggan12', 'oN6,vu?+yBxpa&', '11/8/2012', false, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Janaye Czajkowski', 'jczajkowski13@hao123.com', 'jczajkowski13', 'sF2|/zE1>rg.X', '9/26/2021', true, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Alfy Brownsworth', 'abrownsworth14@naver.com', 'abrownsworth14', 'xZ9(qJY+N', '11/23/2006', false, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Ailis Mence', 'amence15@artisteer.com', 'amence15', 'yS5''wxX1H?', '4/11/2010', true);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Marsh Davley', 'mdavley16@nifty.com', 'mdavley16', 'jJ1!Z(Rg,7(TMBW', '10/1/2004', true);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Erroll Blemings', 'eblemings17@google.ru', 'eblemings17', 'mO7)34<`etA', '3/1/2018', true);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Adda Drinkel', 'adrinkel18@census.gov', 'adrinkel18', 'lW2''*u,y=)s=XD5/', '5/17/2010', true, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Domeniga McCard', 'dmccard19@youku.com', 'dmccard19', 'cA9~I,M#Hb', '11/21/1998', true, 'disabled');
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Breena Standen', 'bstanden1a@sogou.com', 'bstanden1a', 'xX9%4S}as,}', '12/23/1991', true);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Aaren Addeycott', 'aaddeycott1b@spiegel.de', 'aaddeycott1b', 'hE8#9+y1wD>0|{s', '11/3/2007', false);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue) values ('Ulick McGerr', 'umcgerr1c@usda.gov', 'umcgerr1c', 'tW5)l.aeqn', '6/6/2004', false);
insert into lyfter_car_rental.users (name, email, username, password, birthday, overdue, status) values ('Tobi Tommis', 'ttommis1d@nih.gov', 'ttommis1d', 'mX4)WiiTxbZmx@9', '12/11/2012', true, 'disabled');


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