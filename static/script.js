document.addEventListener("DOMContentLoaded", function() {
    const ageInput = document.getElementById("age");
    const glucoseInput = document.getElementById("glucose");
    const bmiInput = document.getElementById("bmi");
    const feedbackDiv = document.getElementById("dynamic-feedback");

    // Function to provide real-time feedback
    function provideFeedback() {
        let feedbackMessage = "";

        const age = parseInt(ageInput.value);
        const glucose = parseInt(glucoseInput.value);
        const bmi = parseFloat(bmiInput.value);

        if (age > 50) {
            feedbackMessage += "As you're above 50, the risk of hypertension increases. Consider regular checkups.<br>";
        }
        if (bmi > 30) {
            feedbackMessage += "Your BMI is on the higher side. This is one of the important factors for the risk of hypertension. Consider consulting a healthcare provider.<br>";
        }
        if (glucose > 140) {
            feedbackMessage += "High fasting glucose level is associated with a higher risk of hypertension. Consider managing your glucose levels.<br>";
        }

        // Update feedback div with dynamic feedback
        if (feedbackMessage) {
            feedbackDiv.innerHTML = `<div style="color: orange; font-weight: bold;">${feedbackMessage}</div>`;
        } else {
            feedbackDiv.innerHTML = "";
        }
    }

    // Attach event listeners to form inputs
    ageInput.addEventListener("input", provideFeedback);
    glucoseInput.addEventListener("input", provideFeedback);
    bmiInput.addEventListener("input", provideFeedback);
});
