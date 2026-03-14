// activate the hidden template field
function activateTemplateField(formId, templateId = 'hiddenTemplate') {
    const template = document.getElementById(templateId);
    if (!template) {
        console.error('Template container not found:', template);
        return;
    }
    const clone = template.content.cloneNode(true);
    const input = clone.querySelector('input');
    // append it to the form, making it part of the DOM
    document.getElementById(formId).appendChild(input);
    return input; // return the newly inserted input element
}

// clear form data
function returnToIndex() {
        window.location.href = '../index.html';
    }

function onRefresh() {
    const baseUrl = window.location.origin + window.location.pathname;
    window.location.replace(baseUrl);
}

// display test results
function displayTestResults(containerId = 'resultsContent', title, resultMessage, resultColor) {
    const container = document.getElementById(containerId);
    if (!container) {
        console.error('Test results container not found:', containerId);
        return;
    }
    const contentDiv = container.querySelector('#resultsContent') || container;
    contentDiv.innerHTML = resultMessage;
    container.style.backgroundColor = resultColor;
    container.style.display = 'block';
    container.scrollIntoView({behavior: 'smooth'});
}