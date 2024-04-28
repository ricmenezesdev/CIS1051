function fetchWord() {
    fetch('http://127.0.0.1:5000/word')
    .then(response => response.json())
    .then(data => {
        console.log(data); 
        displayWord(data.word);
    })
    .catch(error => console.error('Error:', error));
}


function displayWord(word) {
    var outputBox = document.getElementById("outputBox");
    outputBox.textContent = word;
}

window.onload = fetchWord;