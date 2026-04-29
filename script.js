async function start() {
    const title = document.getElementById("title");
    const startBtn = document.getElementById("start");
    startBtn.addEventListener("click", () => {
        title.classList.add("fade-out");
    });
}