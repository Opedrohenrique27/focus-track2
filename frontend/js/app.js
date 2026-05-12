function showToast(message, type = "info") {
  const container = document.getElementById("toast-container");
  const toast = document.createElement("div");
  toast.className = `toast toast-${type}`;

  const icons = {
    success: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="16" height="16"><polyline points="20 6 9 17 4 12"/></svg>`,
    error: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="16" height="16"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>`,
    info: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="16" height="16"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>`,
  };

  toast.innerHTML = `${icons[type] || ""}<span>${message}</span>`;
  container.appendChild(toast);

  requestAnimationFrame(() => toast.classList.add("show"));

  setTimeout(() => {
    toast.classList.remove("show");
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

document.addEventListener("DOMContentLoaded", async () => {
  // Init
  await loadTasks();
  await loadQuote();

  // Modal controls
  document.getElementById("new-task-btn").addEventListener("click", openCreateModal);
  document.getElementById("modal-close").addEventListener("click", closeModal);
  document.getElementById("modal-cancel").addEventListener("click", closeModal);
  document.getElementById("modal-save").addEventListener("click", handleModalSubmit);
  document.getElementById("refresh-quote").addEventListener("click", loadQuote);

  // Close modal on backdrop click
  document.getElementById("task-modal").addEventListener("click", (e) => {
    if (e.target.id === "task-modal") closeModal();
  });

  // Close modal on Escape
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeModal();
    if (e.key === "Enter" && document.getElementById("task-modal").classList.contains("open")) {
      if (document.activeElement.tagName !== "TEXTAREA") handleModalSubmit();
    }
  });

  // Filter tabs
  document.querySelectorAll(".filter-btn").forEach((btn) => {
    btn.addEventListener("click", async () => {
      document.querySelectorAll(".filter-btn").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      const filter = btn.dataset.filter;
      try {
        const tasks = await api.tasks.list();
        const filtered =
          filter === "all"
            ? tasks
            : filter === "pending"
            ? tasks.filter((t) => !t.completed)
            : tasks.filter((t) => t.completed);
        renderTasks(filtered);
      } catch (e) {
        showToast("Erro ao filtrar tarefas", "error");
      }
    });
  });
});
