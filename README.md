##iniciar
sudo systemctl start postgresql

##ver status
sudo systemctl status postgresql

##entrar a posgrest
sudo -u postgres psql

##cambiar contraseña
ALTER USER alejandro WITH PASSWORD 'nueva_contraseña';
