
from color import *
from log import *
import os
import subprocess

def write_over(over_write, text_write, append_or_overwrite):
    file = open(over_write, append_or_overwrite
    file.write(text_write)
    file.close()
    
print("show me your project")
project_name = input()   
print("project's name",  project_name)
project_folder = "/home/ribeiro/Bureau/", + project_name
print("The folder of the project", project_folder)
apache_conf_file = "/etc/apache2/sites-available/" + project_name + ".conf"             

add_host = "127.0.0.1" + project_name + ".local"

VirtualHostTemplate = "<VirtualHost 127.0.0.1:80>\r\n" \
    "   ServerName " + project_name + ".local\r\n" \
    "   DocumentRoot " + project_folder + "\r\n" \
    "   <Directory " + project_folder + ">\r\n" \
    "       Options FollowSymLinks\r\n" \
    "       AllowOverride ALL\r\n" \
    "       Require all granted\r\n" \
    "   </Directory>\r\n" \
"</VirtualHost>"

os.mkdir(project_folder)
write_over(project_folder + "/index.html", htmlTemplate, "w")
subprocess.call(['chmod', '-R' ,'777', project_folder ])
write_over(apache_conf_file, VirtualHostTemplate, "w")
write_over("/etc/hosts", add_host, "a")

subprocess.call(["a2ensite", project_name + ".conf"])
subprocess.call(["apache2ctl", "configtest"])
