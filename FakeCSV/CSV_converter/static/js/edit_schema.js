let addColumnButton = document.querySelector('#add-column-button');
let columnFormsContainer = document.querySelector('#columns-container');

let formCount = document.querySelectorAll('.card-body').length;

addColumnButton.addEventListener('click', function() {
    formCount++;

    let columnForm = document.createElement('div');
    columnForm.className = 'card-body';

    let html = `
    <div class="container text-left">
        <div class="row">
        <div class="col">
            <label for="column_name${formCount}" class="form-label">Column name</label>
            <input type="text" id="column_name${formCount}" name="column_name" class="form-control">
        </div>
        <div class="col">
            <label for="column_separator${formCount}" class="form-label">Type</label>
            <select class="form-select" name="type" id="column_separator${formCount}" aria-label="Default select example">
            <option selected>Open this select menu</option>
            <option value="1">Full name</option>
            <option value="2">Job</option>
            <option value="3">Email</option>
            <option value="4">Integer</option>
            <option value="5">Date</option>
            </select>
        </div>
        <div class="col">
            <div id="integerFields${formCount}" class="integer-fields">
            <div class="container text-left">
                <div class="row">
                <div class="col">
                    <label for="from${formCount}" class="form-label">From</label>
                    <input id="from${formCount}" name="from[]" type="text" class="form-control">
                </div>
                <div class="col">
                    <label for="to${formCount}" class="form-label">To</label>
                    <input id="to${formCount}" name="to[]" type="text" class="form-control">
                </div>
                </div>
            </div>
            </div>
        </div>
        <div class="col">
            <label for="order${formCount}" class="form-label">Order</label>
            <input id="order${formCount}" type="text" class="form-control" name="order">
        </div>
        <div class="col">
        <button type="button" class="btn btn-outline-danger special">Delete</button>
        </div>
        </div>
    </div>
    <br>
    `;

    columnForm.innerHTML = html;
    columnFormsContainer.appendChild(columnForm);

    let typeSelect = columnForm.querySelector(`#column_separator${formCount}`);
    let integerFields = columnForm.querySelector(`#integerFields${formCount}`);

    // Hide the "From" and "To" fields initially
    integerFields.classList.add('hidden-fields');

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
    });
});

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
    });
});