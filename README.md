# NRICTest

An experiment to validate NRIC/FIN numbers using Telegram as the interface.

Run the command below to install the library in the folder with the rest of the files.

pip install python-telegram-bot

Run main.py
Once the bot is running, the bot can be contacted on telegram at @NRICTesterBot

Commits to this repo will notify me on Telegram as well.

The checking function checks the validity of the NRIC and spits back the last letter that would make the NRIC/FIN valid.
A valid NRIC/FIN doesn't actually mean its in use. Its valid but may not be issued.
The implication of that is you can actually create hypothetical NRIC/FIN of someone born in 2030.

Have fun with it. Stay safe.

v1.0 - First commit
v1.01 - Minor improvements
v1.1 - added code for Telegram bot API
v1.11 - Minor improvements
v1.12 - Minor updates in an attempt to get code working
v1.a - Branched the main code to try a different method for calling the Telegram Bot API
v1.2 - Updates
v.1.13 - Can't remember what I did
v2 - First Working Version on the main branch
v2.01 - Added arguments for format of text Bot will process in the checking function
v2.02 Comments added to notate what each chunk of code does, updates to Readme as well.