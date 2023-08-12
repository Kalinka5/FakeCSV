const pictureInput = document.getElementById('id_picture');
const imagePreview = document.getElementById('imagePreview');

pictureInput.addEventListener('change', function () {
    const file = pictureInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const image = document.createElement('img');
            image.src = e.target.result;
            image.alt = 'Profile picture';
            image.className = 'rounded-circle profile-picture float-end mb-3';
            image.style.width = '120px';
            imagePreview.innerHTML = ''; // Clear any previous previews
            imagePreview.appendChild(image);
        };
        reader.readAsDataURL(file);
    } else {
        imagePreview.innerHTML = '';
        pictureInput.style.display = 'block'; // Show the input field
    }
});