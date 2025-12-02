const path = window.location.pathname;
const inputs = document.querySelectorAll(".file-input")


if(path == "/filmes/store") {
    inputs.forEach(element => {
        element.addEventListener('change', () => {
            const filenameSpan = element.parentNode.querySelector('.file-upload-filename');
                if (element.files && element.files.length > 0) {
                    filenameSpan.textContent = element.files[0].name;
                    filenameSpan.style.color = '#333';
                } else {
                    filenameSpan.textContent = 'Nenhum arquivo selecionado';
                    filenameSpan.style.color = '#666';
                }
        });
    })
}

    
