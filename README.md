### Purpose
The function of this script is to generate a secure, randomized password for the user. The password can be of two types: a general password or a custom password.\
\
##### General
When selected, the user will be asked for the length that they want the password to be. \
The program will use the 'strings' library to generate a full list of all characters and will randomly create a password using that list.\
\
##### Custom
When selected, the user will be asked how many of each type of character the user wants in their password. The four types are: upper-case, lower-case, numbers, and puncuation.\
The program will generate four lists, one for each character type, and randomly grab characters from each list the number of times specified. \
It will then add these characters to a new list, shuffle it, and outpt it as a string.\
\
### Security
This program is fully secure as it does not use the 'random' library, but the 'secrets' library instead.\
\
### Future expansion
I plan to implement a full GUI for easier use and eventually add this to a larger password manager program.}