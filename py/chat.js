async function rocketChatLogin(username, password) {
    const response = await fetch('https://rocketchat.vasyerp.in/api/v1/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ user: username, password: password }),
    });
  
    if (!response.ok) {
      throw new Error('Rocket.Chat login failed');
    }
  
    const data = await response.json();
    return data.data;
  }
  
  async function createDirectMessage(authToken, userId, recipientUsername) {
    const response = await fetch('https://rocketchat.vasyerp.in/api/v1/im.create', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Auth-Token': authToken,
        'X-User-Id': userId,
      },
      body: JSON.stringify({ username: recipientUsername }),
    });
  
    if (!response.ok) {
      throw new Error('Failed to create direct message');
    }
  
    const data = await response.json();
    return data;
  }
  
  async function initChat(username, password, recipientUsername) {
    try {
      const { authToken, userId } = await rocketChatLogin(username, password);
      const directMessage = await createDirectMessage(authToken, userId, recipientUsername);
  
      const ddpClient = new DDPClient({
        endpoint: 'wss://rocketchat.vasyerp.in/websocket',
        SocketConstructor: WebSocket,
      });
  
      ddpClient.connect();
  
      ddpClient.on('connected', () => {
        console.log('Connected to Rocket.Chat WebSocket');
  
        ddpClient.call('login', [{ resume: authToken }], (err, res) => {
          if (err) {
            console.error('Login error:', err);
          } else {
            console.log('Logged in:', res);
  
            ddpClient.subscribe('stream-room-messages', [directMessage.room.rid, false], (err) => {
              if (err) {
                console.error('Subscription error:', err);
              }
            });
          }
        });
      });
  
      ddpClient.on('message', (msg) => {
        const data = JSON.parse(msg);
        if (data.msg === 'changed' && data.collection === 'stream-room-messages') {
          const message = data.fields.args[0];
          displayMessage(message);
        }
      });
  
      document.getElementById('message-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const messageInput = document.getElementById('message-input');
        const message = messageInput.value.trim();
        if (message !== '') {
          ddpClient.call('sendMessage', [{
            rid: directMessage.room.rid,
            msg: message
          }], (err, res) => {
            if (err) {
              console.error('Message sending error:', err);
            } else {
              messageInput.value = '';
            }
          });
        }
      });
  
    } catch (error) {
      console.error('Rocket.Chat initialization failed', error);
    }
  }
  
  function displayMessage(message) {
    const messagesContainer = document.getElementById('messages');
    const messageElement = document.createElement('div');
    messageElement.textContent = `${message.u.username}: ${message.msg}`;
    messagesContainer.appendChild(messageElement);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }
  
  // Assuming you have the user's credentials from the ERP session
  const username = 'dhruvilsheth@vasyerp.com';
  const password = 'Dhruvil@804';
  const recipientUsername = 'cloud'; // Replace with actual recipient's username
    initChat(username, password, recipientUsername);
  