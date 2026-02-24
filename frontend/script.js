async function matchResume() {
    const fileInput = document.getElementById("resume").files[0];
    const jobDesc = document.getElementById("jobDesc").value;

    if (!fileInput || !jobDesc) {
        alert("Please upload resume and paste job description");
        return;
    }

    const formData = new FormData();
    formData.append("resume", fileInput);
    formData.append("job_description", jobDesc);

    const response = await fetch("https://ai-resume-checker-xfzx.onrender.com/match", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    document.getElementById("resultBox").style.display = "block";
    document.getElementById("result").innerText =
        data.match_score + "%";
}