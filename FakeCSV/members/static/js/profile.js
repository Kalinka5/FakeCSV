document.addEventListener('DOMContentLoaded', function () {
    const profileImage = document.getElementById('profile-image');
    const fileInput = document.createElement('input');
    fileInput.setAttribute('type', 'file');
    fileInput.style.display = 'none';
  
    profileImage.addEventListener('click', function () {
      fileInput.click();
    });
  
    fileInput.addEventListener('change', function () {
      if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();
  
        reader.onload = function (e) {
          profileImage.src = e.target.result;
        };
  
        reader.readAsDataURL(fileInput.files[0]);
      }
    });
  });