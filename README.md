# whatsapp_group_parser
Just a fun little side project for whatsapp group admins who are tired of inactive members taking valuable slot in the miniscule 256 member limit implemented by WhatsApp. Dumps every information you need to see who're most and least active users in the group.
### Only tested on Android, with chat exported from WhatsApp 2.19.17.
### Not a click to go tool, highly unstable, will need some manual tweaking according to your chat export. See sample files attached for the right format for this to work without any tweaking.

## Requirements:
* WhatsApp Chat Export in .txt format (Group --> Hamburger Menu --> More --> Export Chat)
* all_contacts.txt (A dump of all contact number in a group in a text file)

## Features:
* Gives total number of messages by each user in the group
* Tells all the active users, inactive users, or those who have posted just one message since they joined the group
* Dumps the messages posted by users with 1 message count
* Feature to dump the message count since any date. (Configurable in the script)
