let labels = [];           // Liste des labels (ex: "Estimation 1", "Estimation 2", etc.)
let valeurs = [];          // Liste des valeurs estimées
let chart = null;          // Référence au graphique Chart.js

async function estimer() {
  const m2 = document.getElementById("m2").value;
  const chambres = document.getElementById("chambres").value;
  const centre = document.getElementById("centre").value;

  const response = await fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      Surface_m2: m2,
      Nb_Chambres: chambres,
      Distance_Centre: centre
    })
  });

  const data = await response.json();
  document.getElementById("resultat").textContent = `Prix estimé : ${data.prix_estime} k€`;

  // Ajouter les données dans les tableaux
  labels.push(`Estimation ${labels.length + 1}`);
  valeurs.push(data.prix_estime);

  // Mettre à jour ou créer le graphique
  majGraphique();
}

function majGraphique() {
  const ctx = document.getElementById('graphique').getContext('2d');

  if (chart) {
    chart.destroy(); // Supprimer l'ancien graphique s’il existe
  }

  chart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Prix estimés (k€)',
        data: valeurs,
        backgroundColor: 'rgba(54, 162, 235, 0.6)'
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btn-estimer").addEventListener("click", estimer);
});

