#!/bin/bash 

mariadb -uroot -pAVeryComplicatedPassword
CREATE USER 'leaderboard'@'localhost' IDENTIFIED BY 'AVeryComplicatedPassword';
GRANT ALL PRIVILEGES ON leaderboard.* TO leaderboard@'localhost';
FLUSH PRIVILEGES;
exit