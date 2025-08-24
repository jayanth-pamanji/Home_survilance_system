function sendMessage() {
    let userInput = document.getElementById("user-input").value.trim();
    if (userInput === "") return;

    // Display user's message
    appendMessage(userInput, "user-message");

    // Get bot response
    getBotResponse(userInput);

    // Clear input field
    document.getElementById("user-input").value = "";
}

// Function to handle Enter key press
function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

// Function to append messages to chat box
function appendMessage(message, className) {
    let chatBox = document.getElementById("chat-box");
    let messageElement = document.createElement("div");
    messageElement.className = className;
    messageElement.innerHTML = message;
    chatBox.appendChild(messageElement);

    // Auto-scroll to the bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}

function botMessage(message, className) {
    let chatBox = document.getElementById("chat-box");
    let messageElement = document.createElement("img");
    messageElement.className = className;
    messageElement.src = "data:image/jpeg;base64,"+message;
    console.log(message)
    messageElement.alt="no past records"
    chatBox.appendChild(messageElement);

    // Auto-scroll to the bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}

function botTextMessage(message, className) {
    let chatBox = document.getElementById("chat-box");
    let messageElement = document.createElement("div");
    messageElement.className = className;
    messageElement.innerHTML = message;
    chatBox.appendChild(messageElement);

    // Auto-scroll to the bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Function to generate bot responses
function getBotResponse(input) {
    
    fetch('http://127.0.0.1:5000/object', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input })
    })
    .then(response => response.json())
    .then(data => {
        if(data["response"]=="image found")
        {
            setTimeout(() => {
                botMessage(data.image, "bot-message-image");
            }, 500);
        }
        else if(data.response=="image not found")
        {
            setTimeout(() => {
                botTextMessage("no past records","bot-message-text");
            }, 500);
        }
        else{
            setTimeout(() => {
                botTextMessage(data.response,"bot-message-text");
            }, 500);
        }

    });
    
}

function startVoiceInput() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.onstart = function() {
        console.log("Voice recognition started.");
    };
    
    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        document.getElementById("user-input").value = transcript;
        console.log(event)

    };
    recognition.start();
    
}