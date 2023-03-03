![aura](https://user-images.githubusercontent.com/81994421/222477873-b62baf91-9968-45be-9537-3562b1a2ef4a.png)

Basic Discord bot showing server stats.

# ✨ Statistics
- [x] Server Name
- [x] Server Icon
- [x] Server Banner
- [x] Server Region
- [x] Server Verification Level
- [x] Server Default Notifications
- [x] Server Explicit Content Filter
- [x] Total Members
- [x] Online Members
- [x] Categories
- [x] Text Channels
- [x] Voice Channels
- [x] Bots
- [x] Roles
- [x] Emojis

# 🔘 Modes
Aura can send server statistics in two different modes:
  * embed
  * codeblock
  
# 📜 How to use
For now, the only way to use Aura is to host your own instance, which is described below as the *Hosting Method*.
## ✔ Hosting Method
  1. Go to the [Discord Developer Applications Page](https://discord.com/developers/applications).
  2. Create a new application using the button at the top-right corner, and choose a name.
  3. Go to the Bot section and click "Create Bot".
  4. Under the Privileged Gateway Intents section, check all of the three buttons (*Presence Intent*, *Server Members Intent* and *Messages Content Intent*)
  5. Go to the OAuth2 section, then "URL Generator".
  6. For the Scopes table, check "Bot". A new table called "Bot Permissions" should have appeared.
  7. For the Bot Permissions table, check the following:
  
    Manage Server
    Manage Roles
    Manage Channels
    Manage Emojis and Stickers
    Send Messages
    Read Message History
    
  8. Now, you have your invite link! Click "Copy" then paste it in another tab.
  9. Select the server in which you want Aura to be in, then invite it.
  10. Create a new folder on your computer, then open a command prompt in it.
  11. Execute the following: git clone https://github.com/CColdFox/aura.git (this will clone this repository into your newly created folder)
  12. If not installed yet, install Python and the following libraries:
    * discord.py library - "pip install discord.py"
    * pystyle library - "pip install pystyle"
  15. Edit the `conf.json` file:
  
    token: Enter your bot token which can be copied at the Discord Developer Applications Page,
    prefix: Enter the bot prefix. Default is "aura!",
    mode: Enter your preferred mode between "embed" and "codeblock". Default is "embed",
    
    then save and close the file.
  14. Run the `aura.py` file. Aura should be running! Try it using the ping command.
