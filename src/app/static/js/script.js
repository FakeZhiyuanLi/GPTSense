//Event listeners for background color
const textareaWrapper = document.getElementById("text-divider");
const input = document.getElementById("input");
const form = document.getElementById("form");
const button = document.getElementById("button");
const output = document.getElementById("output");
const historyContainer = document.getElementById("history-container");
const historyWrapper = document.getElementById("history-wrapper");
const historyWidget = document.getElementsByClassName("overtop-widget")[2];

var historyCache;

const sections = document.getElementsByClassName("section");

input.addEventListener("focus", e => {
	textareaWrapper.style.backgroundColor = "#282b30";
});

input.addEventListener("blur", e => {
	textareaWrapper.style.backgroundColor = "#36393F";
});

button.addEventListener("click", e => {
	if (!output.classList.contains("fade-out") && !output.classList.contains("fade-in") && input.value.trim() !== "") {
		output.classList.add("fade-out");

		$(output).one("animationend webkitAnimationEnd oAnimationEnd MSAnimationEnd", output, () => {
			output.style.opacity = 0;
			output.classList.remove("fade-out");
// /*
			var xhr = new XMLHttpRequest();
			xhr.open("POST", "/", true);
			xhr.setRequestHeader('Content-Type', 'application/json');

			xhr.onreadystatechange = function() {
				if (xhr.readyState === 4) {
					display(xhr.responseText);
				}
			}

			xhr.send(JSON.stringify({
			    "value": input.value.trim()
			}));
// */		
			// dummySubmit();
		});
	}

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

function dummySubmit() {
 	const percent = Math.random();
 	display(JSON.stringify({result: percent}));
}

function generateRGB(percent) {
	var red = 0;
	var green = 255;
	var ratio = 255 / 100;

	red += percent * ratio;
	green -= percent * ratio;


	return [red, green, 0];
}

function generateHistoryTab(data) {
	const rgb = generateRGB(data.percent);

	if (document.getElementById("starter-history")) {
		document.getElementById("starter-history").remove();
	}

	historyWidget.classList.add("history-widget");
	historyContainer.style.justifyContent = "start";

	const tab = document.createElement("div");
	tab.setAttribute("class", "history-tab");
	tab.style.boxShadow = `0 0 5px 5px rgba(${rgb[0]}, ${rgb[1]}, ${rgb[2]}, 0.3)`;

	const historyScoreText = document.createElement("h1");
	historyScoreText.textContent = data.percent + "%";
	historyScoreText.classList.add("history-score");
	historyScoreText.classList.add("text");
	historyScoreText.style.textShadow = `0 0 7px #fff, 0 0 21px #fff, 0 0 50px rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`;

	const historyContentWrapper = document.createElement("div");
	historyContentWrapper.classList.add("history-content-wrapper");

	const historyContent = document.createElement("h2");
	historyContent.textContent = shortenContent(data.content);
	historyContent.classList.add("text");
	historyContent.classList.add("history-content");
	historyContent.style.textShadow = `0 0 7px #fff, 0 0 21px #fff, 0 0 50px rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`;

	historyContentWrapper.appendChild(historyContent);

	tab.appendChild(historyScoreText);
	tab.appendChild(historyContentWrapper);
	historyWrapper.style.opacity = 0;

	historyWrapper.prepend(tab);

	historyWrapper.classList.add("fade-in");
	$(historyWrapper).one("animationend webkitAnimationEnd oAnimationEnd MSAnimationEnd", historyWrapper, () => {
		historyWrapper.style.opacity = 1;
		historyWrapper.classList.remove("fade-in");
	});

	tab.addEventListener("click", e => {
		navigator.clipboard.writeText(historyCache[data.id].content).then(() => {
			const copiedText = document.createElement("h2");
			const rect = tab.getBoundingClientRect();

			copiedText.classList.add("text");
			copiedText.classList.add("copied-text");

			copiedText.textContent = "Copied!";
			copiedText.style.left = `${e.clientX - (rect.x + 24)}px`;
			copiedText.style.top = `${e.clientY - (rect.y + 2)}px`;
			tab.appendChild(copiedText);

			$(copiedText).one("animationend webkitAnimationEnd oAnimationEnd MSAnimationEnd", copiedText, () => {
				copiedText.remove();
			});

		}, () => {
		});
	});
}

function shortenContent(content) {
	const max = 150;
	if (content.length > max) {
		return content.substring(0, max) + "...";
	}
	return content;
}

// 0 -> human, 100 -> chatGPT
function display(data) {
	var result = JSON.parse(data).result;
	const percent = Math.floor(100 - (result*100));
	output.textContent = `${percent}%`;

	output.classList.add("fade-in");
	$(output).one("animationend webkitAnimationEnd oAnimationEnd MSAnimationEnd", output, () => {
		output.classList.remove("fade-in");
		output.style.opacity = 1;
	});

	const rgb = generateRGB(percent);
	output.style.textShadow = `0 0 7px #fff, 0 0 21px #fff, 0 0 50px rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`;

	for (var i = 0; i < sections.length; i++) {
		sections[i].style.boxShadow = `0 0 5px 5px rgba(${rgb[0]}, ${rgb[1]}, ${rgb[2]}, 0.3)`;
	}

	if (historyCache == null) {
		historyCache = [];
	}

	var historyData = {
		percent: percent,
		content: input.value,
		id: historyCache.length
	};

	historyCache.push(historyData);

	if (historyCache.length > 10) {
		const widgets = document.getElementsByClassName("history-tab");
		widgets[widgets.length - 1].remove();
		historyCache.shift();
	}

	localStorage.setItem("history", JSON.stringify(historyCache));
	generateHistoryTab(historyData);
}
