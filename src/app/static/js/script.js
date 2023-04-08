//Event listeners for background color
const textareaWrapper = document.getElementById("text-divider");
const input = document.getElementById("input");
const form = document.getElementById("form");
const button = document.getElementById("button");


input.addEventListener("focus", e => {
	textareaWrapper.style.backgroundColor = "#282b30";
});

input.addEventListener("blur", e => {
	textareaWrapper.style.backgroundColor = "#36393F";
});

form.addEventListener("submit", e => {
	e.preventDefault();
});

button.addEventListener("click", e => {
	const html = document.querySelector("html");
	const ripple = document.createElement("span");
	const rect = button.getBoundingClientRect();

	var scale;

	if (window.getComputedStyle(html).zoom > 1) {
		scale = 1;
	} else {
		scale = window.getComputedStyle(html).zoom;
	}

	ripple.setAttribute("class", "ripple");
	ripple.style.left = `${e.clientX / scale - rect.x}px`;
	ripple.style.top = `${e.clientY / scale - rect.y}px`;
	button.prepend(ripple);

	setTimeout(() => {
		ripple.remove();
	}, 1000);
});