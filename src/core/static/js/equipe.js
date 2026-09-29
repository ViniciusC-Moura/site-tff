document.querySelectorAll('[data-carrossel]').forEach((carrossel) => {
    const slides = [...carrossel.querySelectorAll('.carrossel-slide')];
    const controles = carrossel.querySelector('.carrossel-controles');
    if (slides.length < 2 || !controles) return;

    const indicadores = [...carrossel.querySelectorAll('.carrossel-indicador')];
    let atual = 0;

    function mostrar(indice) {
        atual = (indice + slides.length) % slides.length;
        slides.forEach((slide, index) => {
            slide.hidden = index !== atual;
            indicadores[index].setAttribute('aria-current', String(index === atual));
        });
    }

    carrossel.querySelector('.carrossel-anterior').addEventListener('click', () => mostrar(atual - 1));
    carrossel.querySelector('.carrossel-proxima').addEventListener('click', () => mostrar(atual + 1));
    indicadores.forEach((indicador, index) => {
        indicador.addEventListener('click', () => mostrar(index));
    });
    carrossel.addEventListener('keydown', (event) => {
        if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
            event.preventDefault();
            mostrar(atual + (event.key === 'ArrowRight' ? 1 : -1));
        }
    });

    mostrar(0);
    controles.hidden = false;
});
