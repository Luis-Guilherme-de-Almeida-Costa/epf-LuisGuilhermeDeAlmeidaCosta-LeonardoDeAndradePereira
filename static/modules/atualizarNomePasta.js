const path = window.location.pathname;
const inputs = document.querySelector(".file-input")


if(path == "/filmes/store") {
    inputs.addEventListener('change', () => {
      const filenameSpan = inputs.parentNode.querySelector('.file-upload-filename');
        
        if (inputs.files && inputs.files.length > 0) {
            filenameSpan.textContent = inputs.files[0].name;
            filenameSpan.style.color = '#333';
        } else {
            filenameSpan.textContent = 'Nenhum arquivo selecionado';
            filenameSpan.style.color = '#666';
        }
    });
}

    
