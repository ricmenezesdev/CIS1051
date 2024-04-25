function displayWord(word) {
    var outputBox = document.getElementById("outputBox");
    outputBox.textContent = word;
}
function fetchWord() {
    fetch('logic.py')
    .then(response => response.text())
    .then(word => {
        displayWord(word);
        console.log(word);
    })
    .catch(error => console.error('Error:', error));
}
window.onload = fetchWord;
