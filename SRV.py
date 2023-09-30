const .discord = require('discord.js')
const bot = new Discord.Client()
const mc = require('minecraft-protocol')

// Function to forward in-game messages to Discord
function forwardMessage(message) {
  // Replace 'YOUR_CHANNEL_ID' with your Discord channel ID
  const channel = bot.channels.cache.get('your channel id / leave blank');
  channel.send(message.toString('utf8'));
}

// Connect to Minecraft server
const client = mc.createClient({
  host: 'enter your server ip here',
  port: server port,
  username: 'your username'
})

// Listen to Minecraft chat events
client.on('chat', (packet) => {
  const jsonMsg = JSON.parse(packet.message);
  
  // Extract the in-game message from the chat packet
  const message = jsonMsg.extra.map((item) => item.text).join('');
  
  // Forward the in-game message to Discord
  forwardMessage(message);
})

// Discord bot ready event
bot.on('ready', () => {
  console.log('Discord bot is ready!');
})

// Discord bot message event
bot.on('message', (message) => {
  if (message.author.bot) return;
  
  // Replace 'YOUR_MINECRAFT_CHANNEL' with your Minecraft channel name
  if (message.channel.name === 'YOUR_MINECRAFT_CHANNEL') {
    // Send the Discord message to the Minecraft server
    client.write('chat', { message: message.content });
  }
})

// Replace 'YOUR_DISCORD_BOT_TOKEN' with your Discord bot token
bot.login('')