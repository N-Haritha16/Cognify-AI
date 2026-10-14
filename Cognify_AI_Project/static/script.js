
const featureTitles = {
    "Question Answering": "Start with a question",
    "Concept Explanation": "Explain a concept",
    "Quiz Generation": "Generate a quiz",
    "Text Summarization": "Summarize your text",
    "Learning Path": "Build your learning path"
};

document.querySelectorAll(".feature-card").forEach((card) => {
    card.addEventListener("click", () => {
        const selectedFeature = card.dataset.feature;

        document.getElementById("feature").value = selectedFeature;
        document.getElementById("form-title").textContent =
            featureTitles[selectedFeature] || "Start learning";

        document.getElementById("workspace").scrollIntoView({
            behavior: "smooth",
            block: "start"
        });

        document.getElementById("prompt").focus({
            preventScroll: true
        });
    });
});
