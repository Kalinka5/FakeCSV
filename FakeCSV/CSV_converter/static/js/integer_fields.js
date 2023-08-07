let typeSelect = document.querySelector('#type');
let integerFields = document.querySelector('#integerFields');

integerFields.classList.add('hidden-fields');

typeSelect.addEventListener('change', function() {
    if (typeSelect.value === '4') {
        integerFields.classList.remove('hidden-fields');
    } else {
        integerFields.classList.add('hidden-fields');
    }
});