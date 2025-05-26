# discord-phrase-bot
A highly flexible and customisable Discord bot built in Python that provides responses to detected phrases from certain users. This isn't drop-and-go — it's designed to be customised to your needs and is best designed for fun with friends.

## Customisation
Before implementing the phrase bot, the customisable lists need to be populated with specific strings for your needs. The `selected_phrases` list should be populated with specific words or phrases that will trigger a response from the bot if found within the message content (e.g. 'christmas' may trigger the bot to recite a Christmas carol). The `response_options` list should be populated with a list of response phrases to be selected from at random if a trigger phrase is found. Targeting a specific user can be disabled as per instructions in `bot.py`.

## Registering Your Bot
To connect your bot to Discord, you'll first have to register a new application through the Discord Developer Portal.
1) On the **Discord Developer Portal** (https://discordapp.com/developers/applications), select **New Application**, enter a name for your bot, and click **Create**.
2) On the application dashboard you'll be taken to, select the **Bot** page along the left-hand menu and then press **Add Bot**.
3) Customise the username and icon of the bot as desired, then scroll down and toggle on **Message Content Intent**.
4) Copy the **bot token** - you'll need this later on.
5) Switch to the **OAuth2** tab on the left-hand menu, scroll down to **OAuth2 URL Generator** and select the **bot** scope.
6) In the **Bot Permissions** section created below, select the permissions to **View Channels**, **Send Messages** and **Send Messages in Threads**.
7) Scroll down and copy the **Generated URL**.
8) Open this URL in a new tab, select a server (in which you have administrator permissions) to add the bot to and click **Authorize**.

## Running Your Bot
1) Customise `bot.py` for your needs, keeping the key commented sections intact.
2) Create a **.env** file and set it out as below. For **DISCORD_TOKEN** should use the bot token you previously copied (no quotation marks needed). If your bot targets a particular user, you can find this by turning on **DevTools** in your Discord app and then right-clicking on the target's username and selecting **Copy User ID**. Then set **TARGET_ID** to this value (no quotation marks needed).
    ```
    DISCORD_TOKEN=COPIED_BOT_TOKEN_HERE
    TARGET_ID=TARGET_USER_ID_HERE
    ```
3) If you don't require the bot to be active 24/7, one option is to host the bot from your own machine. To achieve this, you can run the bot with the command `python3 bot.py` (depending on your version of Python). The command line should indicate when the bot has been successfully connected to Discord, and the bot should appear as Active in any servers it has been added to. Killing the command will take the bot offline. 
