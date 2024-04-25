function displayWord(word) {
    var outputBox = document.getElementById("outputBox");
    outputBox.textContent = word;
}

function fetchWord() {
    fetch('logic.py')
    .then(response => response.text())
    .then(word => {
        // Call the displayWord function to display the word
        displayWord(word);
        // Print the word to the console
        console.log(word);
    })
    .catch(error => console.error('Error:', error));
}

// Call the fetchWord function when the window loads
window.onload = fetchWord;
