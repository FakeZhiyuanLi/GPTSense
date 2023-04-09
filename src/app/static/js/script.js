//Event listeners for background color
const textareaWrapper = document.getElementById("text-divider");
const input = document.getElementById("input");
const form = document.getElementById("form");
const button = document.getElementById("button");
const output = document.getElementById("output");

const sections = document.getElementsByClassName("section");

input.addEventListener("focus", e => {
	textareaWrapper.style.backgroundColor = "#282b30";
});

input.addEventListener("blur", e => {
	textareaWrapper.style.backgroundColor = "#36393F";
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

	if (!output.classList.contains("fade-out")) {
		output.classList.add("fade-out");

		$(document).one("animationend webkitAnimationEnd oAnimationEnd MSAnimationEnd", output, () => {
			output.style.opacity = 0;
			output.classList.remove("fade-out");

			var xhr = new XMLHttpRequest();
			xhr.open("POST", "/", true);
			xhr.setRequestHeader('Content-Type', 'application/json');

			xhr.onreadystatechange = function() {
				if (xhr.readyState === 4) {
					display(xhr.responseText);
				}
			}

			xhr.send(JSON.stringify({
			    "value": input.value
			}));
		
			//dummySubmit();
		});
	}
});

function dummySubmit() {
 	const percent = Math.floor(Math.random() * 100);
 	display({value: percent});
}

function generateRGB(percent) {
	var red = 0;
	var green = 255;
	var ratio = 255 / 100;

	red += percent * ratio;
	green -= percent * ratio;


	return [red, green, 0];
}

// 0 -> human, 100 -> chatGPT
function display(data) {
	var result = JSON.parse(data).result;
	const percent = Math.floor(100 - (result*100));
	output.textContent = `${percent}%`;

	output.classList.add("fade-in");
	$(document).one("animationend webkitAnimationEnd oAnimationEnd MSAnimationEnd", output, () => {
		output.classList.remove("fade-in");
		output.style.opacity = 1;
	});

	const rgb = generateRGB(percent);
	output.style.textShadow = `0 0 7px #fff, 0 0 21px #fff, 0 0 50px rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`;

	for (var i = 0; i < sections.length; i++) {
		sections[i].style.boxShadow = `0 0 5px 5px rgba(${rgb[0]}, ${rgb[1]}, ${rgb[2]}, 0.3)`;
	}
}
