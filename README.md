Building the SSDQ image
The build is carried out in accordance with the dockerfile.
To build, run the command (required with a dot at the end):
docker build -t ssdq_server:latest .

Raising a docker container with an SSDQ application
1. In the config folder, edit the configuration files (config.yaml). At the same time, if the database is planned to be launched in one docker compose, then the connection parameters to the dqServer and flaskDb database do not need to be changed (except for the login and password).
If necessary, configure log configurations (logging.conf).
2. In the config folder, specify the parameters for connecting to KeyCloak.
3. When starting with the https protocol, place the certificates in the cert folder. And also in the docker-compose-ssdq.yaml file for the ssdq_server service, uncomment the line ./cert:/app/dqflask/cert.
4. In the docker-compose-ssdq.yaml file, edit POSTGRES_USER and POSTGRES_PASSWORD. Align the configuration file (config.yaml).
5. Run with the command: docker-compose –f docker-compose-ssdq.yaml up –d
