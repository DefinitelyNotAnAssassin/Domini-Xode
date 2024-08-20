CREATE TABLE Models_announcements(
id INTEGER PRIMARY KEY,
title varchar(255)  NOT NULL,
content TEXT  NOT NULL,
date datetime  NOT NULL,
author_id bigint  NOT NULL,
thumbnail varchar(100)  NOT NULL
);


CREATE TABLE Models_account(
id INTEGER PRIMARY KEY,
password varchar(128)  NOT NULL,
last_login datetime  NOT NULL,
is_superuser bool  NOT NULL,
username varchar(150)  NOT NULL,
first_name varchar(150)  NOT NULL,
last_name varchar(150)  NOT NULL,
email varchar(254)  NOT NULL,
is_staff bool  NOT NULL,
is_active bool  NOT NULL,
date_joined datetime  NOT NULL,
role INTEGER  NOT NULL,
image_link varchar(555)  NOT NULL,
description varchar(255)  NOT NULL,
facebook_link varchar(555)  NOT NULL,
FOREIGN KEY (id) REFERENCES Models_announcements(author_id) ON DELETE NO ACTION ON UPDATE NO ACTION,
FOREIGN KEY (id) REFERENCES Models_announcements(author_id) ON DELETE NO ACTION ON UPDATE NO ACTION
);


CREATE TABLE Models_events(
id INTEGER PRIMARY KEY,
event_name varchar(64)  NOT NULL,
event_description varchar(1028)  NOT NULL,
event_start_date datetime  NOT NULL,
event_end_date datetime  NOT NULL,
event_location varchar(32)  NOT NULL,
event_registration_link varchar(256)  NOT NULL,
event_status varchar(32)  NOT NULL,
event_flyer varchar(100)  NOT NULL
);


CREATE TABLE Models_messages(
id INTEGER PRIMARY KEY,
email varchar(64)  NOT NULL,
full_name varchar(128)  NOT NULL,
phone_number varchar(16)  NOT NULL,
msg TEXT  NOT NULL
);


CREATE TABLE API_tts(
id INTEGER PRIMARY KEY,
audio_file varchar(100)  NOT NULL
);

