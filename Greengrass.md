# Greengrass Installation Steps

1. **Open command prompt/terminal and SSH into the AWS Lightsail instance:**
    ```bash
    Download pem file from AWS Console
    chmod 400 xxx.pem
    ssh -i LightsailDefaultKey-us-east-1.pem user@Ip_address
    ```
2. **Setup environment: Installing Java JDK 17**
    ```bash
    sudo apt upgrade
    sudo apt install default-jdk
    java --version
    sudo apt install unzip
    ```
3. **Install the AWS IoT Greengrass Core software (console):**
    ```bash
    export AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXXXXXX
    export AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    ```
    **Note:** Replace the access key ID and secret access key with your own credentials.
4. **Install the AWS IoT Greengrass Core software (CLI):**
    ```bash
    cd ~
    curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip > greengrass-nucleus-latest.zip
    unzip greengrass-nucleus-latest.zip -d GreengrassInstaller && rm greengrass-nucleus-latest.zip

    sudo -E java -Droot="/greengrass/v2" -Dlog.store=FILE \
    -jar ./GreengrassInstaller/lib/Greengrass.jar \
    --aws-region us-east-1 \
    --thing-name DDIGreengrassCore \ 
    --thing-group-name DDIGreengrassCoreGroup \
    --thing-policy-name GreengrassV2IoTThingPolicy \
    --tes-role-name GreengrassV2TokenExchangeRole \
    --tes-role-alias-name GreengrassCoreTokenExchangeRoleAlias \
    --component-default-user ggc_user:ggc_group \
    --provision true \
    --setup-system-service true \
    --deploy-dev-tools true
    ```
6. **Open VS Code and open a terminal:**
   - Navigate to any folder, preferably Documents.
   - Create a project folder:
     ```bash
     mkdir project
     cd project
     ```
   - Create a Greengrass folder:
     ```bash
     mkdir greengrass
     cd greengrass
     ```
   - Install Greengrass Development Kit (GDK) CLI:
     ```bash
     python3 -m pip install -U git+https://github.com/aws-greengrass/aws-greengrass-gdk-cli.git@v1.6.2
     ```
     Verify the installation:
     ```bash
     gdk --version
     ```
7. **Validate the credentials:**
    ```bash
    echo %AWS_ACCESS_KEY_ID%
    echo %AWS_SECRET_ACCESS_KEY%
    ```
    If it doesn't recognize the credentials, set them using:
    ```bash
    export AWS_ACCESS_KEY_ID="XXXXXXXXXXXXXXXXX"
    export AWS_SECRET_ACCESS_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ```
    **Note:** Replace the access key ID and secret access key with your own credentials.
