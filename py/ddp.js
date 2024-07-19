const ddp = new DDP({
    endpoint: "wss://rocketchat.vasyerp.in/websocket",
    SocketConstructor: WebSocket,
  });
  
  ddp.connect();
  
  ddp.on("connected", () => {
    console.log("Connected to Rocket.Chat WebSocket");
  
    ddp.method("login", [{ resume: authToken }], (err, res) => {
      if (err) {
        console.error("Login error:", err);
      } else {
        console.log("Logged in:", res);
        
        ddp.subscribe("stream-room-messages", [roomId, false], (err) => {
          if (err) {
            console.error("Subscription error:", err);
          }
        });
      }
    });
  });
  
  ddp.on("message", (msg) => {
    console.log("New message:", msg);
  });
  