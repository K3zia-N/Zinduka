const modal = document.getElementById("modal");
const modalTitle = document.getElementById("modal-title");
const modalDescription = document.getElementById("modal-description");

function showDetails(section) {
    let title, description;

    switch(section) {
        case 'pads':
            title = "Pads for Girls";
            description = "Support menstrual hygiene by donating pads or volunteering in distribution drives to help keep girls in school and empowered.";
            break;
        case 'feeding':
            title = "Feeding Children";
            description = "Join us in feeding programs that provide nutritious meals to children in underserved communities, fighting hunger and malnutrition.";
            break;
        case 'trees':
            title = "Tree Planting Drives";
            description = "Participate in tree planting activities to promote environmental conservation and combat climate change in your local communities.";
            break;
        case 'health':
            title = "Community Health Camps";
            description = "Be part of health camps that offer free medical checkups, counseling, and basic treatment for families who lack access to healthcare.";
            break;
        default:
            title = "";
            description = "";
    }

    modalTitle.textContent = title;
    modalDescription.textContent = description;
    modal.style.display = "block";
}

function closeModal() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
