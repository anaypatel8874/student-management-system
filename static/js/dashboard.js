document.addEventListener("DOMContentLoaded", () => {
    const themeButton = document.getElementById("themeToggle");
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "dark") {
        document.body.classList.add("dark");
        updateThemeIcon(themeButton, true);
    }

    if (themeButton) {
        themeButton.addEventListener("click", () => {
            const isDark = document.body.classList.toggle("dark");
            localStorage.setItem("theme", isDark ? "dark" : "light");
            updateThemeIcon(themeButton, isDark);
        });
    }

    animateCounters();
    buildCharts();
    setupSearch();
    setupAddRowModal();
});

function updateThemeIcon(button, isDark) {
    if (!button) {
        return;
    }

    const icon = button.querySelector("i");

    if (!icon) {
        return;
    }

    icon.className = isDark ? "fa-solid fa-sun" : "fa-solid fa-moon";
}

function animateCounters() {
    const counters = document.querySelectorAll(".counter");

    counters.forEach((counter) => {
        const target = Number(counter.dataset.target || 0);
        const duration = 900;
        const startTime = performance.now();

        const tick = (now) => {
            const progress = Math.min((now - startTime) / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);

            counter.textContent = Math.round(target * eased);

            if (progress < 1) {
                requestAnimationFrame(tick);
            }
        };

        requestAnimationFrame(tick);
    });
}

function buildCharts() {
    if (typeof Chart === "undefined") {
        return;
    }

    Chart.defaults.color = "rgba(248,250,252,.78)";
    Chart.defaults.font.family = "Poppins, sans-serif";
    Chart.defaults.plugins.legend.labels.usePointStyle = true;

    const attendance = document.getElementById("attendanceChart");

    if (attendance) {
        new Chart(attendance, {
            type: "line",
            data: {
                labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
                datasets: [{
                    label: "Attendance",
                    data: [82, 91, 86, 95, 92, 98],
                    borderColor: "#06b6d4",
                    backgroundColor: "rgba(6,182,212,.18)",
                    borderWidth: 3,
                    fill: true,
                    pointBackgroundColor: "#f8fafc",
                    pointBorderColor: "#06b6d4",
                    pointRadius: 4,
                    tension: .42
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    x: {
                        grid: {
                            display: false
                        }
                    },
                    y: {
                        beginAtZero: false,
                        min: 70,
                        max: 100,
                        grid: {
                            color: "rgba(255,255,255,.08)"
                        },
                        ticks: {
                            callback: (value) => `${value}%`
                        }
                    }
                }
            }
        });
    }

    const student = document.getElementById("studentChart");

    if (student) {
        new Chart(student, {
            type: "doughnut",
            data: {
                labels: ["CSE", "IT", "ECE", "ME"],
                datasets: [{
                    data: [45, 20, 25, 10],
                    backgroundColor: ["#4f46e5", "#06b6d4", "#10b981", "#f59e0b"],
                    borderColor: "rgba(15,23,42,.72)",
                    borderWidth: 4,
                    hoverOffset: 8
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: "68%",
                plugins: {
                    legend: {
                        position: "bottom"
                    }
                }
            }
        });
    }
}

function setupSearch() {
    const searchInput = document.querySelector(".search-box input");
    const tableBody = document.querySelector("[data-table-body]");

    if (!searchInput || !tableBody) {
        return;
    }

    searchInput.addEventListener("input", () => {
        const query = searchInput.value.trim().toLowerCase();

        tableBody.querySelectorAll("tr").forEach((row) => {
            row.hidden = !row.textContent.toLowerCase().includes(query);
        });
    });
}

function setupAddRowModal() {
    const panel = document.querySelector(".management-panel");
    const addButton = document.querySelector(".js-add-row");
    const modal = document.querySelector("[data-add-modal]");
    const fieldsWrap = document.querySelector("[data-modal-fields]");
    const form = document.querySelector("[data-add-form]");
    const table = document.querySelector(".management-panel table");
    const tableBody = document.querySelector("[data-table-body]");

    if (!panel || !addButton || !modal || !fieldsWrap || !form || !table || !tableBody) {
        return;
    }

    const section = panel.dataset.section || window.location.pathname;
    const storageKey = `sms-added-rows-${section}`;
    const headings = Array.from(table.querySelectorAll("thead th")).map((heading) => heading.textContent.trim());

    loadSavedRows(storageKey, tableBody);

    addButton.addEventListener("click", () => {
        buildModalFields(fieldsWrap, headings);
        modal.hidden = false;
        document.body.classList.add("modal-open");

        const firstInput = fieldsWrap.querySelector("input");

        if (firstInput) {
            firstInput.focus();
        }
    });

    modal.querySelectorAll("[data-close-modal]").forEach((button) => {
        button.addEventListener("click", () => closeModal(modal, form));
    });

    modal.addEventListener("click", (event) => {
        if (event.target === modal) {
            closeModal(modal, form);
        }
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && !modal.hidden) {
            closeModal(modal, form);
        }
    });

    form.addEventListener("submit", (event) => {
        event.preventDefault();

        const values = headings.map((heading) => {
            const input = form.elements[`field-${slugify(heading)}`];
            return input ? input.value.trim() : "";
        });

        if (values.some((value) => value === "")) {
            form.classList.add("show-errors");
            return;
        }

        addTableRow(tableBody, values, true);
        saveRow(storageKey, values);
        closeModal(modal, form);
    });
}

function buildModalFields(container, headings) {
    container.innerHTML = "";

    headings.forEach((heading) => {
        const id = `field-${slugify(heading)}`;
        const field = document.createElement("label");
        field.className = "modal-field";
        field.htmlFor = id;
        field.innerHTML = `
            <span>${heading}</span>
            <input id="${id}" name="${id}" type="text" placeholder="Enter ${heading.toLowerCase()}" required>
            <small>${heading} is required.</small>
        `;
        container.appendChild(field);
    });
}

function addTableRow(tableBody, values, highlight) {
    const row = document.createElement("tr");

    if (highlight) {
        row.classList.add("new-row");
    }

    row.innerHTML = values.map((value) => `<td>${escapeHtml(value)}</td>`).join("");
    tableBody.prepend(row);

    if (highlight) {
        window.setTimeout(() => row.classList.remove("new-row"), 1200);
    }
}

function loadSavedRows(storageKey, tableBody) {
    const rows = JSON.parse(localStorage.getItem(storageKey) || "[]");

    rows.forEach((row) => {
        addTableRow(tableBody, row, false);
    });
}

function saveRow(storageKey, row) {
    const rows = JSON.parse(localStorage.getItem(storageKey) || "[]");
    rows.push(row);
    localStorage.setItem(storageKey, JSON.stringify(rows));
}

function closeModal(modal, form) {
    modal.hidden = true;
    document.body.classList.remove("modal-open");
    form.reset();
    form.classList.remove("show-errors");
}

function slugify(value) {
    return value.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
}

function escapeHtml(value) {
    const div = document.createElement("div");
    div.textContent = value;
    return div.innerHTML;
}
