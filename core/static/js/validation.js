// validation.js
function validateForm() {
    // Get all form fields
    var formFields = document.querySelectorAll('form input, form select, form textarea');

    // Check if any field is empty
    for (var i = 0; i < formFields.length; i++) {
        if (formFields[i].value === '') {
            alert('Please fill out all fields.');
            formFields[i].focus(); // Focus on the first empty field
            return false;
        }
    }

    // If all fields are filled, submit the form
    return true;
}