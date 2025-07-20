document.addEventListener("DOMContentLoaded", () => {
  const articlesContainer = document.getElementById("articles-container");
  const eventsContainer = document.getElementById("events-container");

  const articles = [
    { title: "Understanding Femicide", desc: "An article discussing the causes and solutions to femicide in Kenya." },
    { title: "Community Voices", desc: "Survivor stories and how the community can intervene." }
  ];
  const events = [
    { title: "Self-Defense Training", desc: "Learn practical self-defense techniques.", date: "July 25, 2025" },
    { title: "Legal Rights Workshop", desc: "Know your rights against GBV.", date: "August 3, 2025" }
  ];

  articles.forEach(article => {
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `<h3>${article.title}</h3><p>${article.desc}</p><button onclick="alert('Open article: ${article.title}')">Read More</button>`;
    articlesContainer.appendChild(card);
  });
  events.forEach(event => {
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `<h3>${event.title}</h3><p>${event.desc}</p><small>${event.date}</small><br/><button onclick="alert('Register for: ${event.title}')">Register</button>`;
    eventsContainer.appendChild(card);
  });
});
function openModal(type) {
  const modal = document.getElementById("modal");
  const modalTitle = document.getElementById("modal-title");
  const modalBody = document.getElementById("modal-body");
  switch(type) {
    case 'pads':
      modalTitle.textContent = "Pads for Girls";
      modalBody.textContent = "Join our mission to provide pads to keep girls in school. You can volunteer or donate directly through our channels.";
      break;
    case 'rape':
      modalTitle.textContent = "What to Do in Case of Rape";
      modalBody.textContent = "1. Find a safe place. 2. Seek medical attention immediately. 3. Do not change clothes or shower. 4. Report to authorities or call our helpline.";
      break;
    case 'rights':
      modalTitle.textContent = "Legal Rights";
      modalBody.textContent = "Learn about your legal protections and steps to take when facing gender-based violence. We connect you with legal aid and guidance.";
      break;
    case 'safety':
      modalTitle.textContent = "Safety Guidelines";
      modalBody.textContent = "Practical safety tips: Share your location, avoid isolated areas, have emergency contacts ready, and trust your instincts.";
      break;
  }
  modal.style.display = "block";
}
function closeModal() {
  document.getElementById("modal").style.display = "none";
}
