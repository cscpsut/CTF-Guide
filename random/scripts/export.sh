#!/bin/bash
/usr/bin/curl https://cscpsut.com/admin/export --header "Authorization: Token b164513b62b2358612eaa1cdeb662692cd252b6e643dbe513800b5cff7113ed2" --header "Content-Type: application/json" --http2 --output "/home/silver/CTFd_Exports/backup$(/usr/bin/date).zip"