# MySQL Installation Steps

## Connect to the Debian Linux

1. Update package index:
    ```
    sudo apt update
    ```

2. Upgrade installed packages:
    ```
    sudo apt upgrade
    ```

3. Install MariaDB server:
    ```
    sudo apt install mariadb-server
    ```

4. Secure MariaDB installation:
    ```
    sudo mysql_secure_installation
    ```

## Start and Enable the Server

1. Start MariaDB server:
    ```
    sudo systemctl start mariadb
    ```

2. Enable MariaDB to start on boot:
    ```
    sudo systemctl enable mariadb
    ```

## Verify the Server

1. Check the status of MariaDB server:
    ```
    sudo systemctl status mariadb
    ```

## Login to the Root and Change the Password

1. Login to MariaDB as root user:
    ```
    sudo mysql -u root -p
    ```

## Create Table

1. Execute the following SQL command to create the "time_series" table:
    ```sql
    CREATE TABLE time_series (
        tag_name VARCHAR(256), 
        date_time TIMESTAMP, 
        value DOUBLE, 
        quality BOOLEAN
    );
    ```

## Install pip

1. Install pip for Python 3:
    ```
    sudo apt-get install python3-pip
    ```

2. Install pip:
    ```
    python get-pip.py
    pip --version
    ```

## Create a Database User

1. Create a new database user named 'admin':
    ```sql
    CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';
    ```

2. Grant all privileges to the 'admin' user:
    ```sql
    GRANT ALL ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
    ```
3. To List the Databases:
    ```sql
    SHOW DATABASES;
    ```
4. To List the Tables:
    ```sql
    SHOW TABLES;
    ```
5. To Switch to a Database:
    ```sql
    USE Db_name;
    ```
5. To Login to a user:
    ```sql
    sudo mysql -u user_name;
    ```
