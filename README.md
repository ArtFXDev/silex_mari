# Silex DCCs
****
###### A guide for connecting DCCs into Silex

****
# Steps

### 1:
Create **Silex_ _dcc-name_** rez package directory

### 2:
Enter the directory and create two new directories
- beta.0.1.0
- prod.0.1.0

These are neccessary for Silex to create the correct environment
When Silex opens any dcc, an environment command is run: 

Rez Environments | Scene Command |
:---: | :---: |
Prod | rez env silex_dcc-**prod** production_name -- silex launch *dcc* --task-id ...|
Beta | rez env silex_dcc-**beta** production_name -- silex launch *dcc* --task-id ...
_We will work in the **beta** directory and use **prod** as expected_

### 3:
Enter the beta directory
Create another three directories
- script
- silex_ _dcc-name_
- startup

A rez `package.py` will also be created here
The package will list the requirements for the DCC and set the environment paths

***Script:***
Contains a `build.py` file which is no longer used
***Silex_ _dcc-name_:***
Another three directories inside
- *commands*
  -  python functions using CommandBase that the dcc will use to run actions
- *config*
    -  action
        - yaml configuration files for standard actions
    - conform
        - yaml configuration files for conform actions
    - publish
        - yaml configuration files for publishing actions 
- *utils*
    - Utility files the dcc may require

***Startup***
Startup files for the dcc, these files initialize the tool's shelves
*More importantly* the startup file needs a function call: `Context.get().start_services()` - this starts the connection between Silex and the DCC.

### 4: 
Locate the directory: ...\silex_rez\packages\dcc\
Here we will see all of the currently supported softwares. Create a new directory of the desired dcc

Inside this folder we will create a folder for the software version. In the case of Maya the version we use is `2022.0` however a `2019.3` folder is available for artists working with an older build.

In the version folder we create a rez package file and a platform folder. 
- In the platform folder we create a `dcc-name + env` file : eg. `mayaenv.py`
- We set the install paths and append the neccessary libraries here

The `package.py` rez file sets the requirements for the software. Here we can also set the desired tools for each dcc. 

### 5: 
##### Adding the DCC to the Silex App
To begin, clone [silex-front](https://github.com/ArtFXDev/silex-front) to your local machine. 
Navigate to the location in an open terminal. Make sure `yarn` is installed. 
- If `yarn` is not installed
- Running `npm install -g yarn` will install it globally on your machine

In the open terminal run `yarn`

**To add your DCC to the front end:**
Find and add the DCC's svg logo to the logo folder: `\src\assets\images\logos`
We need to edit two files; `TaskModal\FileExplorer.tsx`, `FileIcon\FileIcon.tsx`
**FileExplorer.tsx**
- Locate `dccButtonsData [...]`
- Add the dcc to the list
- Setting `disabled: true` will display the DCC on the front but keep users from interacting with it
- By default `disabled` is set to false

**FileIcon.tsx**
- Import the logo from the logo directory
- Add it to the dictionary of DCCs

**Back in the terminal**
Run `yarn lint:fix` to format your changes. This is to prevent Silex from throwing an error

### 6:
##### Adding the DCC to the database
Open a new terminal
We need to connect to [cgwire](https://www.cg-wire.com/) with [gazu](https://gazu.cg-wire.com/) 
- **If gazu is not installed**
    - Install it: `pip install gazu`
- Start python 
- `import gazu`
- `gazu.set_host("database_address")`
    - In the case for ArtFx we use our silex kitsu address
    - http://kitsu.prod.silex.artfx.fr/api
- `gazu.log_in("email@address", "password")`
    - The cgwire login needs to be a **studio manager** to have access 
- `gazu.files.new_software("SoftwareName", "ShortName", "AppExtension")`
    - An example for Blender would be:
        - `gazu.files.new_software("Blender", "blender", "blend")`
    - You can find a script to automatically add new softwares here:
        - [create_softwares.py](https://github.com/ArtFXDev/zou-deploy/blob/main/src/create_softwares.py)

- We can check if this worked by calling `.{softwares {name}}.` in graphQL
### 7:
##### Running Silex and Testing the software
In our `silex-front` terminal we run `yarn start` 
We need to move Silex into the `dev Python Mode` which can be found in the advanced settings of silex on the taskbar
