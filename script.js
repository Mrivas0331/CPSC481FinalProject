const startBtn = document.getElementById("start-btn");
const topHalf = document.querySelector(".top-half");
const bottomHalf = document.querySelector(".bottom-half");

startBtn.addEventListener("click", () => {
    topHalf.classList.add("top-slide-out");
    bottomHalf.classList.add("bottom-slide-out");

    setTimeout(() => {
        window.location.href = "./chat.html"
    }, 700);
});