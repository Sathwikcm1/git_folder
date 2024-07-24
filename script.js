const entryField = document.getElementById('entry-field');
const darkModeButton = document.getElementById('dark-mode');
const lightModeButton = document.getElementById('light-mode');
const calculator = document.querySelector('.calculator');

darkModeButton.addEventListener('click', () => {
    calculator.classList.add('dark-mode');
});

lightModeButton.addEventListener('click', () => {
    calculator.classList.remove('dark-mode');
});

function appendValue(value) {
    const entryFieldValue = entryField.value;
    entryField.value = entryFieldValue + value;
}

function calculateResult() {
    const entryFieldValue = entryField.value;
    try {
        const result = eval(entryFieldValue);
        entryField.value = result;
    } catch (error) {
        entryField.value = 'Error';
    }
}

function clearEntryField() {
    entryField.value = '';
}

// Add animations
entryField.addEventListener('focus', () => {
    entryField.classList.add('focus');
});

entryField.addEventListener('blur', () => {
    entryField.classList.remove('focus');
});

document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', () => {
        button.classList.add('active');
        setTimeout(() => {
            button.classList.remove('active');
        }, 100);
    });
});
