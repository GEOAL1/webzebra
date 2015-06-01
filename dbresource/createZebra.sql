/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2015/6/1 20:45:38                            */
/*==============================================================*/


drop table if exists b_bike_common;

drop table if exists b_bike_dynamic;

drop table if exists sys_user;

/*==============================================================*/
/* Table: b_bike_common                                         */
/*==============================================================*/
create table b_bike_common
(
   bike_id              int(11) not null,
   bike_type            varchar(64) not null,
   price                double not null,
   register_time        timestamp not null,
   power_type           varchar(64),
   motor_type           varchar(64),
   images               varchar(64),
   note                 varchar(256),
   primary key (bike_id)
);

/*==============================================================*/
/* Table: b_bike_dynamic                                        */
/*==============================================================*/
create table b_bike_dynamic
(
   bike_id              int(11) not null,
   cur_power            int(11),
   throttle_state       varchar(20),
   brake_state          varchar(20),
   motor_state          varchar(20),
   lock_state           varchar(20),
   indicator_state      varchar(20),
   longitude            decimal(10,7),
   latitude             decimal(10,7),
   speed                double,
   time_samp            timestamp,
   primary key (bike_id)
);

/*==============================================================*/
/* Table: sys_user                                              */
/*==============================================================*/
create table sys_user
(
   phone_num            varchar(128) not null,
   password             varchar(128) not null,
   username             varchar(128),
   balance              double default 0,
   integral             int(11) default 0,
   user_sex             varchar(16),
   user_age             int(11),
   occupation           varchar(16),
   create_time          timestamp,
   edit_time            timestamp,
   primary key (phone_num)
);

