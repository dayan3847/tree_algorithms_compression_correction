#!/bin/sh

# fix owner for all files

#find . -user root -type d -exec chmod 0755 {} \;
#find . -user root -type f -exec chmod 0644 {} \;
find . -user root -type f -exec chmod 777 {} \;
#find . -user root -exec chown www-data:www-data {} \;
