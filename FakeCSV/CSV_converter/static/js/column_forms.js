// Handle the existing column forms
let columnForms = document.querySelectorAll('.card-body');

columnForms.forEach(function(columnForm) {
    let typeSelect = columnForm.querySelector('select[name="type"]');
    let integerFields = columnForm.querySelector('.integer-fields');

    // Hide the "From" and "To" fields initially if the type is not "Integer"
    if (typeSelect.value !== '4') {
        integerFields.classList.add('hidden-fields');
    }

    typeSelect.addEventListener('change', function() {
        if (typeSelect.value === '4') {
            integerFields.classList.remove('hidden-fields');
        } else {
            integerFields.classList.add('hidden-fields');
        }
    });

    let deleteButton = columnForm.querySelector('.btn-outline-danger');
    deleteButton.addEventListener('click', function() {
        columnForm.remove();
        formCount--;
    });
});