const API_BASE = "/api/v1";

async function request(method, path, body = null) {
  const opts = {
    method,
    headers: { "Content-Type": "application/json" },
  };
  if (body !== null) opts.body = JSON.stringify(body);
  const res = await fetch(`${API_BASE}${path}`, opts);
  if (res.status === 204) return null;
  const data = await res.json();
  if (!res.ok) throw new Error(data.detail || "Request failed");
  return data;
}

const api = {
  tasks: {
    list: () => request("GET", "/tasks/"),
    create: (data) => request("POST", "/tasks/", data),
    update: (id, data) => request("PUT", `/tasks/${id}`, data),
    complete: (id) => request("PATCH", `/tasks/${id}/complete`),
    delete: (id) => request("DELETE", `/tasks/${id}`),
    stats: () => request("GET", "/tasks/stats"),
  },
  quotes: {
    random: () => request("GET", "/quotes/random"),
  },
};
