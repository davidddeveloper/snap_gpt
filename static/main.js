let chats_container = document.querySelector('.chats')
let prompt_form = document.querySelector('.chat-form')
let submitBtn = document.querySelector('.submit-btn')

const request_obj = new XMLHttpRequest()

const displayMessage = (text, isUser=true, loadingMsg=false) => {
    if (loadingMsg == true)
    {
        let msg = document.createElement('div')
        msg.classList.add('loading-msg')
        chats_container.appendChild(msg)
        return;
    }
    let el = document.createElement('div')
    let eltext = document.createElement('span')
    el.classList.add('chat')
    eltext.textContent = text
    el.appendChild(eltext)
    chats_container.appendChild(el)
    
    el_name = document.createElement('span')
    if (isUser == true)
    {
        el_name.textContent = 'David'
        el_name.classList.add(".user-name")
    }
    else
    {
        el_name.textContent = 'SnapGPT'
        el_name.classList.add(".snap-gpt")
    }
    el.appendChild(el_name)

    
};

prompt_form.addEventListener('submit', (e) => {
    e.preventDefault()
    submitBtn.disabled = true

    let userPrompt = document.querySelector('.user_prompt').value.trim()
    const gptGreetMsg = document.querySelector('.gpt-greet-msg')
    console.log(gptGreetMsg)
    console.log(chats_container)
    if (gptGreetMsg) {
        chats_container.removeChild(gptGreetMsg)
        
    }
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    console.log(userPrompt)
    request_obj.open('POST', '/chatbot')
    request_obj.setRequestHeader("Content-Type", 'application/json')

    request_obj.setRequestHeader("X-CSRFToken", csrftoken);

    displayMessage(userPrompt, true)
    displayMessage("Loading response...", false, true)
    loadingMsg = document.querySelector('.loading-msg')
    request_obj.onload = () => { /* process the response received */
        chats_container.removeChild(loadingMsg)
        if (request_obj.status == 200)
        {
            const response = JSON.parse(request_obj.responseText)
            console.log("This is the response", response.response)
           
            displayMessage(response.response, false)
        }
        else if (request_obj.status == 500)
        {
            displayMessage("There's an error with the server!", false)
            displayMessage("Try refreshing your browser", false)
        }
        else
        {
            displayMessage("Looks like you have no internet connection!", false)
            displayMessage("Connect to the internet and try again.", false)
        }

        submitBtn.disabled = false
    }

    request_obj.send(JSON.stringify({user_prompt: userPrompt}))
});