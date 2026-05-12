let editingTaskId = null;

function formatTime(minutes) {
  if (!minutes) return "—";
  if (minutes < 60) return `${minutes}min`;
  const h = Math.floor(minutes / 60);
  const m = minutes % 60;
  return m ? `${h}h ${m}min` : `${h}h`;
}

function getStatusLabel(completed) {
  return completed
    ? '<span class="badge badge-done">Concluída</span>'
    : '<span class="badge badge-pending">Pendente</span>';
}

function renderTasks(tasks) {
  const list = document.getElementById("task-list");
  const empty = document.getElementById("empty-state");

  if (!tasks.length) {
    list.innerHTML = "";
    empty.style.display = "flex";
    return;
  }

  empty.style.display = "none";
  list.innerHTML = tasks
    .map(
      (task) => `
    <div class="task-card ${task.completed ? "task-done" : ""}" data-id="${task.id}">
      <div class="task-card-header">
        <div class="task-title-row">
          <button class="complete-btn ${task.completed ? "completed" : ""}"
            onclick="handleComplete(${task.id})" title="${task.completed ? "Concluída" : "Marcar como concluída"}">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <polyline points="20 6 9 17 4 12"/>
            </svg>
          </button>
          <span class="task-title">${escapeHtml(task.title)}</span>
        </div>
        <div class="task-actions">
          <button class="icon-btn edit-btn" onclick="openEditModal(${task.id})" title="Editar">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/>
              <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>
            </svg>
          </button>
          <button class="icon-btn delete-btn" onclick="handleDelete(${task.id})" title="Excluir">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="3 6 5 6 21 6"/>
              <path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/>
              <path d="M10 11v6M14 11v6"/>
              <path d="M9 6V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2"/>
            </svg>
          </button>
        </div>
      </div>
      ${task.description ? `<p class="task-desc">${escapeHtml(task.description)}</p>` : ""}
      <div class="task-meta">
        ${getStatusLabel(task.completed)}
        ${task.estimated_time ? `<span class="task-time"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="12" height="12"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> ${formatTime(task.estimated_time)}</span>` : ""}
        <span class="task-date">${new Date(task.created_at).toLocaleDateString("pt-BR")}</span>
      </div>
    </div>
  `
    )
    .join("");
}

async function loadTasks() {
  try {
    const tasks = await api.tasks.list();
    renderTasks(tasks);
    await loadStats();
  } catch (e) {
    showToast("Erro ao carregar tarefas", "error");
  }
}

async function loadStats() {
  try {
    const stats = await api.tasks.stats();
    document.getElementById("stat-total").textContent = stats.total;
    document.getElementById("stat-done").textContent = stats.completed;
    document.getElementById("stat-pending").textContent = stats.pending;
    document.getElementById("stat-time").textContent = formatTime(stats.total_estimated_time);

    const bar = document.getElementById("progress-bar");
    const pct = document.getElementById("progress-pct");
    const rate = stats.completion_rate;
    bar.style.width = `${rate}%`;
    pct.textContent = `${rate}%`;
  } catch (e) {
    console.error("Stats error", e);
  }
}

async function handleComplete(id) {
  try {
    await api.tasks.complete(id);
    await loadTasks();
    showToast("Tarefa concluída! 🎉", "success");
  } catch (e) {
    showToast("Erro ao concluir tarefa", "error");
  }
}

async function handleDelete(id) {
  if (!confirm("Tem certeza que deseja excluir esta tarefa?")) return;
  try {
    await api.tasks.delete(id);
    await loadTasks();
    showToast("Tarefa excluída", "info");
  } catch (e) {
    showToast("Erro ao excluir tarefa", "error");
  }
}

function openEditModal(id) {
  const card = document.querySelector(`.task-card[data-id="${id}"]`);
  if (!card) return;
  const title = card.querySelector(".task-title").textContent;
  const desc = card.querySelector(".task-desc")?.textContent || "";
  const timeMeta = card.querySelector(".task-time");
  let minutes = 0;
  if (timeMeta) {
    const txt = timeMeta.textContent.trim();
    const hMatch = txt.match(/(\d+)h/);
    const mMatch = txt.match(/(\d+)min/);
    minutes = (hMatch ? parseInt(hMatch[1]) * 60 : 0) + (mMatch ? parseInt(mMatch[1]) : 0);
  }

  editingTaskId = id;
  document.getElementById("modal-title-input").value = title;
  document.getElementById("modal-desc-input").value = desc;
  document.getElementById("modal-time-input").value = minutes;
  document.getElementById("modal-heading").textContent = "Editar Tarefa";
  document.getElementById("task-modal").classList.add("open");
  document.getElementById("modal-title-input").focus();
}

function openCreateModal() {
  editingTaskId = null;
  document.getElementById("modal-title-input").value = "";
  document.getElementById("modal-desc-input").value = "";
  document.getElementById("modal-time-input").value = "";
  document.getElementById("modal-heading").textContent = "Nova Tarefa";
  document.getElementById("task-modal").classList.add("open");
  document.getElementById("modal-title-input").focus();
}

function closeModal() {
  document.getElementById("task-modal").classList.remove("open");
  editingTaskId = null;
}

async function handleModalSubmit() {
  const title = document.getElementById("modal-title-input").value.trim();
  const description = document.getElementById("modal-desc-input").value.trim();
  const estimated_time = parseInt(document.getElementById("modal-time-input").value) || 0;

  if (!title) {
    showToast("O título é obrigatório", "error");
    document.getElementById("modal-title-input").focus();
    return;
  }

  try {
    if (editingTaskId) {
      await api.tasks.update(editingTaskId, { title, description, estimated_time });
      showToast("Tarefa atualizada!", "success");
    } else {
      await api.tasks.create({ title, description, estimated_time });
      showToast("Tarefa criada!", "success");
    }
    closeModal();
    await loadTasks();
  } catch (e) {
    showToast(e.message || "Erro ao salvar tarefa", "error");
  }
}

function escapeHtml(text) {
  const d = document.createElement("div");
  d.appendChild(document.createTextNode(text));
  return d.innerHTML;
}
