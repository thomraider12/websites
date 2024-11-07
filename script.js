let lastScrollY = window.scrollY;

window.addEventListener("scroll", () => {
    const header = document.getElementById("header");

    if (window.scrollY > lastScrollY) {
        // Rolando para baixo, esconde o cabeçalho
        header.classList.add("hidden");
    } else {
        // Rolando para cima, mostra o cabeçalho
        header.classList.remove("hidden");
    }

    lastScrollY = window.scrollY;
});
