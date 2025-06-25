// src/components/modules/CommunityHub.jsx
import React, { useState, useEffect } from "react";

const CommunityHub = () => {
  const [events, setEvents] = useState([]);

  // Simulate fetching events from an API or database
  useEffect(() => {
    const fetchEvents = async () => {
      const data = [
        {
          title: "Self-Defense Workshop",
          date: "2025-07-15",
          description: "Free self-defense training in Nakuru. Open to all genders, ages 15+.",
        },
        {
          title: "Community Awareness March",
          date: "2025-08-03",
          description: "March to raise awareness against femicide and gender-based violence.",
        },
        {
          title: "Activist Training Series",
          date: "Every Saturday, August 2025",
          description: "Learn how to organize, advocate, and support survivors in your community.",
        },
        {
          title: "Youth Advocacy Forum",
          date: "2025-09-10",
          description: "A platform for young voices to push for policy changes.",
        },
      ];
      setEvents(data);
    };

    fetchEvents();
  }, []);

  return (
    <section className="bg-gray-100 text-black py-12 px-6 md:px-20" id="community-hub">
      <div className="max-w-5xl mx-auto">
        <h2 className="text-3xl md:text-4xl font-bold mb-6 text-red-600 text-center">
          Community Hub
        </h2>
        <p className="text-lg mb-8 text-center">
          Engage with our community through upcoming events, workshops, and campaigns.
        </p>

        <div className="grid md:grid-cols-2 gap-8">
          {events.map((event, index) => (
            <div key={index} className="bg-white p-6 rounded shadow">
              <h3 className="text-2xl font-semibold mb-2">{event.title}</h3>
              <p className="text-gray-700 mb-2">📅 {event.date}</p>
              <p className="text-gray-600">{event.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default CommunityHub;
