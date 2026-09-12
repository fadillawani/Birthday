document.addEventListener("DOMContentLoaded", () => {

    const buttons = document.querySelectorAll(".primary-button");

    buttons.forEach((button) => {

        button.addEventListener("click", () => {

            document.body.classList.add("page-loading");

        });

    });

});

document.addEventListener("DOMContentLoaded", () => {

    const slides = document.querySelectorAll(".memory-slide");

    const previousButton =
        document.getElementById("memory-prev");

    const nextButton =
        document.getElementById("memory-next");

    const currentCounter =
        document.getElementById("memory-current");

    if (!slides.length) {
        return;
    }

    let currentIndex = 0;


    function showSlide(index) {

        slides.forEach((slide) => {
            slide.classList.remove("active");
        });

        slides[index].classList.add("active");

        currentCounter.textContent =
            String(index + 1).padStart(2, "0");
    }


    previousButton.addEventListener("click", () => {

        currentIndex--;

        if (currentIndex < 0) {
            currentIndex = slides.length - 1;
        }

        showSlide(currentIndex);
    });


    nextButton.addEventListener("click", () => {

        currentIndex++;

        if (currentIndex >= slides.length) {
            currentIndex = 0;
        }

        showSlide(currentIndex);
    });

});